from simplecrypt import *

# считываем файл с информацией (в байтах)
with open("/Users/user/Downloads/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
# считываем файл с паролями построчно (в байтах)
with open("/Users/user/Downloads/passwords.txt", "rb") as psw:
    for password in psw.readlines():
        try:
            x = decrypt(password=password[:-1], data=encrypted)
            print(x)
        except DecryptionException:
            print("Не судьба")

