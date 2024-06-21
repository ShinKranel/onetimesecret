### How to use
Docker-compose steps (will be added soon)
...

1. **Go to `127.0.0.1:8000/docs`.**

2. **`/generate` - to create secret.**\
Add secret message and secret_key(don't forget this key!).
In response you'll get link to a secret message, just copy part after "/secrets/".

3. **`/secrets/{secret_id}` - to read secret.**\
Paste the secret link in secret_id field,
then enter the secret_key to access the secret.

4. **`/secrets/{secret_id}/burn` - to delete secret.**\
If you want to delete secret without reading.