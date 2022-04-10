class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    # current_balance = my_balance
    @my_balance.setter
    def my_balance(self,new_balance):
        if not isinstance(new_balance, (int,float)):
            raise ValueError ("Баланс должен быть числом")
        self.__balance = new_balance

    @my_balance.deleter
    def my_balance(self):
        del self.__balance

    # my_balance = current_balance.setter(my_balance)
    # my_balance = my_balance.deleter(delete_balance)

katya = BankAccount(11)
# print(katya.get_balance())
print(katya.my_balance)
katya.my_balance = 33
print(katya.my_balance)
# katya.my_balance()
del katya.my_balance
# katya.my_balance
