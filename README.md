## How to use
### Run with docker
Make sure that you have [docker](https://www.docker.com/get-started/) installed.
1. Rename `.env-example` file to `.env`.
2. Rename `.env-non-dev-example` file to `.env-non-dev`.
3. In the `.env` file, change the values of the `DB_NAME`, `DB_USER`, `DB_PASS` variables to your db data.
4. In the `.env-non-dev` file, change the values of the `POSTGRES_PASSWORD`, `PGADMIN_DEFAULT_EMAIL`,
`PGADMIN_DEFAULT_PASSWORD`, `DB_PASS` variables on your own.
5. Run `docker compose up`

API - `127.0.0.1:8080/docs`\
pgadmin4 - `127.0.0.1:5051/`

---

### Run manually
Requirements: \
PostgreSQL \
pgadmin4 - if you want :)

1. Use command `docker compose up`
2. Use this command in your "projects" directory `git clone https://github.com/ShinKranel/onetimesecret.git`
3. Rename `.env-example` file to `.env`.
4. In the `.env` file, change the values of the `DB_NAME`, `DB_USER`, `DB_PASS` variables to your db data.
5. Choose interpreter or make it with inside project. 
6. Execute the `pip install -r requirements.txt` command in the terminal.

API - `127.0.0.1:8000/docs`\
pgadmin4 - `127.0.0.1:5050/`

---

1. **`/generate` - to create secret.**\
Add secret message and secret_key(don't forget this key!).
In response you'll get link to a secret message, just copy part after "/secrets/".
Secret will be burn after 7 days!

2. **`/secrets/{secret_id}` - to read secret.**\
Paste the secret link in secret_id field,
then enter the secret_key to access the secret.

3. **`/secrets/{secret_id}/burn` - to delete secret.**\
If you want to delete secret without reading.