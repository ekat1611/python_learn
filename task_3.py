# Напишите функцию get_int(start_message, error_message, end_message), принимающую три строки в качестве аргументов.
# Функция должна запрашивать у пользователя ввод до тех пор, пока не будет введено целое число
# (строка, принимаемая функцией int без ошибок).
# Перед первым запросом ввода должен быть выведен аргумент start_message,
# после каждого ошибочного ввода нужно выводить значение строки error_message
# и при удачном вводе нужно вывести строку end_message и вернуть полученное целое число из функции.
# Каждое выводимое сообщение должно находиться на отдельной строке.

x = ''
def get_int(start_message,error_message,end_message):
    global x
    print(start_message)
    x = input()
    while x.isdigit() == False and x[0] != '-':
        print(error_message)
        x = input()
    print(end_message)
    return x

x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
print(type(x))