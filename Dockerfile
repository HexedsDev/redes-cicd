FROM nginx:stable-alpine
LABEL org.opencontainers.image.source="https://github.com/HexedsDev/redes-cicd"
LABEL org.opencontainers.image.description="Practica de Redes"
COPY site/ /usr/share/nginx/html/
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1
