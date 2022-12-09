# хранилище всех классов
classes_storage = {}
# хранилище исключений, которые уже встречались
input_exceptions = []
# хранилище исключений, предки которых уже были переданы ранее
extra_exceptions = []


# функция возвращает False, если полученный класс не потомок ранее полученных классов и True, если потомок
def check_parent(is_child, is_parent):
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


# считываем классы для проверки
for i in range(int(input())):
    current_exception = input()
    # проходимся по массиву ранее полученных исключений с целью проверки, является ли полученный класс чьим-то потомком
    for input_exception in input_exceptions:
        # если оказывается что полученный класс чей-то потомок, записываем его в extra_exceptions и прерываем обход
        if check_parent(current_exception, input_exception):
            extra_exceptions.append(current_exception)
            print(current_exception)
            break
    if current_exception not in extra_exceptions:
        input_exceptions.append(current_exception)


"""
Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Output: 
FileNotFoundError
"""