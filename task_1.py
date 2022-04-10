# Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения,
# которые повторяются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Формат ввода:
# Одна строка с целыми числами, разделёнными пробелом.
# Формат вывода:
# Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться, порядок вывода может быть произвольным.

string = sorted(input().split())
total = []
for i in range(len(string)):
    if string.count(string[i]) > 1:
        if string[i] not in total:
            total.append(string[i])
        string.pop(i)
        string.insert(1,0)
print(*total)



# from itertools import groupby
# lst = sorted(input().split())
# for i, j in groupby(lst):
#     if len(list(j)) > 1:
#         print(i, end=' ')



# a = input().split()
# b = set(a)
# print(*[i for i in b if a.count(i) > 1])