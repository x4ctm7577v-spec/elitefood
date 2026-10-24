FROM caddy:2.8.4-alpine
COPY index.html /srv/index.html
COPY img /srv/img
COPY *.pdf /srv/
CMD caddy file-server --root /srv --listen :${PORT:-8080}
