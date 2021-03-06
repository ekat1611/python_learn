# На вход алгоритму подаётся строка, содержащая символы латинского алфавита.
# Эта строка разбивается на группы одинаковых символов, идущих подряд ("серии").
# Каждая серия характеризуется повторяющимся символом и количеством повторений.
# Именно эта информация и записывается в код: сначала пишется длина серии повторяющихся символов, затем сам символ.
# У серий длиной в один символ количество повторений будем опускать.

from itertools import groupby
text_str = input()

# cоздадим список строки без повторяющихся значений:
test_set = []
for i in range(len(text_str)):
    if text_str[i] not in test_set:
        test_set.append(text_str[i])

#  теперь отсортируем так, чтобы значения группировались по мере их вхождения:
text = []
for i in test_set:
    for j in text_str:
        if j == i:
            text.append(j)

#  теперь можем группировать значения, они будут в правильной последовательности:
test = [list(g) for k, g in groupby(text)]
print(test)

# теперь сделаем проверку на длину группы, если она равна 1 значению, то единицу выводить не будем
for i in range(len(test)):
    if len(test[i]) == 1:
        print(test[i][0], end='')
    else:
        print(len(test[i]), test[i][0], sep='', end='')

# пример того, как можно исключить повторяющиеся элементы с помощью groupby:
# from itertools import groupby
# x = input()
# print( [list(g) for k, g in groupby(sorted(x))])
# # ['A', 'B', 'C', 'D']

# Внимание!!! Если не отсортировать значения, то группировка будет работать не правильно!