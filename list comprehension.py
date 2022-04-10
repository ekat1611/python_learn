list_start = ["оттава", "москва", "пекин", "полоцк", "версаль", "дели", "каир"]
sogl = 'аеиоуюя'
# первая переменная - то, что мы вносим в новый список, затем идёт 2 цикла for:
# один идёт по словам в изначальном списке
# второй идёт по буквам в словах
# это можно сравнить с переменными i и j при обходе вложенных списков
list_total = [letter for word in list_start for letter in word if letter not in sogl]
list_2 = [[j for j in i if j not in sogl] for i in list_start]

print(list_total)
print(*list_2)