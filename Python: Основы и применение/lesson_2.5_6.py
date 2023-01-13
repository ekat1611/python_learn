# Замыкания

def mod_checker(x, mod=0):
    return lambda y: y % x == mod


# здесь переменной test присваивается значение lambda y: y%x == mod. То есть, фактически test - это lambda функция
test = mod_checker(3, 1)
# здесь происходит вызов lambda функции с атрибутом 4, т.е. получается lambda 4: 4%3 == 1
print(test(4))
