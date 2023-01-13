from simplecrypt import *

# считываем файл с паролями построчно (в байтах) и файл с информацией (в байтах)
with open("/Users/user/Downloads/passwords.txt", "rb") as psw, open("/Users/user/Downloads/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    for password in psw.readlines():
        try:
            # метод rstrip() нужен для того, чтобы убрать переносы на конце строк (/n)
            # альтернатива password=password[:-1]
            password = password.rstrip()
            x = decrypt(password=password, data=encrypted)
            print(x)
        except DecryptionException:
            print("Не судьба")

