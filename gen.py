import secrets

secret_key = secrets.token_hex(16)
print(secret_key)

#used to generate the screte key used in app.py