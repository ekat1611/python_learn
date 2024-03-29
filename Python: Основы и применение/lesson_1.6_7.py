classes_storage = {}


# функция возвращает False, если is_child не потомок для is_parent, и True если потомок
def check_parent(is_child, is_parent):
    if is_child not in classes_storage:
        return False
    if is_parent in classes_storage[is_child] or is_child == is_parent:
        return True
    # проходимся по предкам child класса
    for p in classes_storage[is_child]:
        # если у предка есть ещё предки, опускаемся "глубже" по рекурсии
        if len(classes_storage[p]):
            # если получаем True, возвращаем его же выше
            if check_parent(p, is_parent):
                return True
    return False


# считываем данные, чтобы записать их в словарь, структура {class: [A, B]}
for i in range(int(input())):
    string = input().split()
    # добавляем в classes_storage child-класс
    classes_storage[string[0]] = [string[2:][i] for i in range(len(string[2:]))]
    # добавляем в словарь всех предков с пустыми parents, т.к. они нам неизвестны
    for parent in range(len(string[2:])):
        if string[2:][parent] not in classes_storage:
            classes_storage[string[2:][parent]] = []

for i in range(int(input())):
    input_string = input().split()
    # идём проверять является ли полученный child-класс потомком полученного parent-class
    if check_parent(input_string[1], input_string[0]):
        print('Yes')
    else:
        print('No')


"""
Входные данные для отладки:
3
A : C B R
B : D E
R : Y
1 
E A
"""