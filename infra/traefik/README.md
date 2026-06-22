Traefik reverse proxy scaffold

Place these files on the server (example `~/traefik`) and update `traefik.yml` with your email.

Deploy commands (on server):

```bash
# set permissions for ACME storage
chmod 600 acme.json

# start Traefik
docker compose up -d
```

Notes:
- Traefik will obtain Let's Encrypt certificates automatically for routers you enable with labels.
- Update services to expose themselves to Traefik by adding Docker labels and using `traefik.http.routers.<name>.rule=Host(`your.domain.com`)` and `traefik.http.routers.<name>.entrypoints=websecure`.
