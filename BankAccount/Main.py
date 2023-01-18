from string import digits
list_pass = open('test_passwords.txt')
list_passwords = list_pass.read()
list_passwords = list_passwords.split()


class BankAccount:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def contain_digit(new_password):
        for digit in digits:
            if digit in new_password:
                return True
        return False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if new_password in list_passwords:
            raise ValueError('Пароль должен быть уникальным!')
        if type(new_password) != str:
            raise TypeError('Пароль должен быть строкой!')
        if not BankAccount.contain_digit(new_password):
            raise ValueError('Пароль должен содержать цифры!')
        self.__password = new_password


man = BankAccount('man', 'maste1')
man.password = 'maste1'
print(man.password)
man.password = 'dfd1'
print(man.password)




