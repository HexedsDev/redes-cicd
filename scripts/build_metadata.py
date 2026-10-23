import json
import os
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = {
    'version': (root / 'VERSION').read_text().strip(),
    'commit': os.environ.get('GITHUB_SHA', 'local'),
    'built_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'repository': os.environ.get('GITHUB_REPOSITORY', 'HexedsDev/redes-cicd'),
}
(root / 'site/version.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
print(json.dumps(data, indent=2))
