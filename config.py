import secrets
config = {
    'secrets-app_secret_key': secrets.token_hex(2),
    'pin': secrets.token_hex(2)
}

pin = config['pin']
pin2 = config['secrets-app_secret_key']
print(f"Code is \033[93m{pin}\033[0m")
print(f"Code is \033[93m{pin}\033[0m")
print(f"Code is \033[93m{pin2}\033[0m")
print(f"Code is \033[93m{pin2}\033[0m")
