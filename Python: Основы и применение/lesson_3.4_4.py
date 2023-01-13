import json
classes_storage = json.loads(input())
result_dct = {}


# функция проверяет, есть ли переданный класс в хранилище классов
def check_class_in_classes_storage(class_name) -> bool:
    for cls in range(len(classes_storage)):
        if class_name in classes_storage[cls]["name"]:
            return True
    return False


# функция добавляет переданный класс в хранилище классов
def add_class_into_classes_storage(class_name):
    classes_storage.append({"name": class_name, "parents": []})


# функция возвращает словарь с искомым классов
def find_class_in_storage(class_name) -> dict:
    for cls in range(len(classes_storage)):
        if classes_storage[cls]["name"] == class_name:
            return classes_storage[cls]


# функция возвращает False, если is_child не потомок для is_parent, и True если потомок
def check_parent(is_child, is_parent):
    if is_parent["name"] in is_child["parents"]:
        return True
    # проходимся по предкам child класса
    for p in is_child["parents"]:
        # если предка нет в словаре, добавляем его
        if not check_class_in_classes_storage(p):
            add_class_into_classes_storage(p)
        # вызываем рекурсию со всеми предками
        if check_parent(find_class_in_storage(p), is_parent):
            return True
    return False


# проходим по словарям с классами и по очереди проверяем их на родство
for parent in range(len(classes_storage)):
    count = 1
    for child in range(len(classes_storage)):
        if check_parent(classes_storage[child], classes_storage[parent]):
            count += 1
    result_dct[classes_storage[parent]["name"]] = count


# выводим результат в нужном виде
for key in sorted(result_dct):
    print(key, ":", result_dct[key])


"""Input: 
[{"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}] 

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}] 


Output:
A : 3
B : 1
C : 2
"""