# Redes Cloud Lab

Práctica independiente de integración y despliegue continuo para Redes, sexto semestre.

Cada push a `main` ejecuta siete pruebas, construye y comprueba una imagen Docker,
la publica en GitHub Container Registry y despliega el sitio en GitHub Pages.

El sitio publica su versión, commit y fecha de construcción en `version.json`.

Sitio: https://hexedsdev.github.io/redes-cicd-cloud-lab/

Imagen: `ghcr.io/hexedsdev/redes-cicd-cloud-lab:latest`

Pruebas locales: `python -m unittest discover -s tests -v`.
