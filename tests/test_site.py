import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / 'site/index.html').read_text(encoding='utf-8')
        cls.doc = Document(cls.html)

    def test_document_language_and_encoding(self):
        self.assertTrue(any(t == 'html' and a.get('lang') == 'es' for t, a in self.doc.nodes))
        self.assertTrue(any(t == 'meta' and a.get('charset') == 'utf-8' for t, a in self.doc.nodes))

    def test_mobile_viewport(self):
        self.assertTrue(any(t == 'meta' and a.get('name') == 'viewport' for t, a in self.doc.nodes))

    def test_local_styles_and_scripts_exist(self):
        count = 0
        for tag, attrs in self.doc.nodes:
            ref = attrs.get('src') if tag == 'script' else attrs.get('href') if tag == 'link' else None
            if ref and not ref.startswith(('https://', 'http://')):
                self.assertTrue((ROOT / 'site' / ref).is_file(), ref)
                count += 1
        self.assertEqual(count, 2)

    def test_unique_identifiers(self):
        ids = [a['id'] for _, a in self.doc.nodes if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {'version', 'commit', 'built-at'})

    def test_workflow_links_point_to_new_repository(self):
        links = [a.get('href', '') for t, a in self.doc.nodes if t == 'a']
        self.assertIn('https://github.com/HexedsDev/redes-cicd-cloud-lab/actions', links)
        self.assertNotIn('redes2web', self.html)

    def test_three_pipeline_stages(self):
        self.assertEqual(sum(t == 'article' for t, _ in self.doc.nodes), 3)
        self.assertIn('Desplegar', self.html)

    def test_release_uses_semantic_version(self):
        self.assertRegex((ROOT / 'VERSION').read_text().strip(), r'^\d+\.\d+\.\d+$')


if __name__ == '__main__':
    unittest.main(verbosity=2)
