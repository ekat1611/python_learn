n = int(input())
path = ''
namespaces = {
    "global": {
        "parent": None,
        "variables": ["w"]
    },
    "test": {
        "parent": "global",
        "variables": ["w"]
    },
    "cat": {
        "parent": "test",
        "variables": ["w", "s"]
    },
    "tree": {
        "parent": "cat",
        "variables": ["w"]
    },
}


def get_path(dct, element, space):
    global path
    if element not in dct[space]["variables"]:
        if dct[space]["parent"] is not None:
            parent = dct[space]["parent"]
            path = parent
            return get_path(dct=namespaces, element=element, space=parent)
        else:
            return None
    return path


for i in range(n):
    action = input().split()
    if action[0] == 'create':
        namespaces[action[1]] = {"parent": action[2], "variables": []}
    if action[0] == 'add':
        namespaces[action[1]]["variables"].append(action[2])
    if action[0] == 'get':
        # если в переданном пространстве нет нужной переменной
        if action[2] not in namespaces[action[1]]["variables"]:
            final_path = get_path(dct=namespaces, element=action[2], space=action[1])
            print(final_path)
        # если в переданном пространстве есть нужная переменная, выводим это пространство
        else:
            print(action[1])
        path = ''


"""
1
get tree w // вернёт tree
get tree s // вернёт cat
"""