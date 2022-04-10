# На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором:
# a \texttt{ operator } ba operator b, где вместо \texttt{operator}operator могут использоваться следующие слова:
# plus, minus, multiply, divide для, соответственно, сложения, вычитания, умножения и целочисленного деления.
# Формат ввода:
# Одна строка, содержащая выражение вида a \texttt{ operator } ba operator b, 0 \le a,b\le10000≤a,b≤1000.
# Оператор может быть plus, minus, multiply, divide.
# Формат вывода:
# Строка, содержащая целое число -− результат вычисления.
import operator
operators = {"plus":operator.add, 'minus':operator.sub, 'multiply':operator.mul, 'divide':operator.floordiv}
string = input().split()
string[1] = operators[string[1]]
print(string[1](int(string[0]),int(string[2])))
# синтаксис использования оператора:
# operator.name(operand1, operand2)
# operator.add(1,2) -- результат 3