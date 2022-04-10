# Поле для игры сапёр представляет собой сетку размером n \times mn×m.
# В ячейке сетки может находиться или отсутствовать мина.
# Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной,
# указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)
# Формат ввода:
# На первой строке указываются два натуральных числа 1 \le n,m \le 1001≤n,m≤100,
# после чего в nn строках содержится описание поля в виде последовательности точек '.' и звёздочек '*',
# где точка означает пустую ячейку, а звёздочка − ячейку с миной.
# Формат вывода:
# nn строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"),
# при этом число означает количество мин в соседних ячейках поля.

high, weight = map(int,input().split())
start_list = ['.' + input() + '.' for i in range(high)]
start_list.append('.'* (weight+2))
start_list.insert(0, '.'* (weight+2) )
total_list = []
count = 0
for i in range(1,high+1):
    for j in range(1,weight+1):
        if start_list[i][j] == '*':
            total_list.append("*")
        else:
            if start_list[i][j+1] == '*': count += 1
            if start_list[i+1][j] == '*': count+=1
            if start_list[i+1][j+1] == '*': count+=1
            if start_list[i-1][j] == '*': count+=1
            if start_list[i-1][j-1] == '*': count+=1
            if start_list[i][j-1] == '*': count+=1
            if start_list[i+1][j-1] == '*': count+=1
            if start_list[i-1][j+1] == '*': count+=1
            total_list.append(count)
            count = 0
    if len(total_list) != 0:
        print(*total_list, sep='')
    total_list.clear()
