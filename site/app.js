fetch('version.json', { cache: 'no-store' })
  .then(response => {
    if (!response.ok) throw new Error('Metadatos no disponibles');
    return response.json();
  })
  .then(build => {
    document.getElementById('version').textContent = build.version;
    document.getElementById('commit').textContent = build.commit.slice(0, 12);
    document.getElementById('built-at').textContent = build.built_at.replace('T', ' ').replace('+00:00', ' UTC');
  })
  .catch(() => {});
