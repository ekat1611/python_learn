class Vector:
    def __init__(self, *args):
        self.all = list(args)
        self.values = []
        for i in self.all:
            if isinstance(i,int):
                self.values.append(i)
        del self.all
        self.values = sorted(self.values)

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор {tuple(self.values)}'
        else:
            return 'Пустой вектор'


v1 = Vector(1,11,4)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"