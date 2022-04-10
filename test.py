class Vector:

    def __init__(self, *args):
        a = []
        for i in args:
            if isinstance(i, int):
                a.append(i)
        self.values = sorted(a)

    def __str__(self):
        if self.values:
            #если мы просто вставим self.values в join, то получим ошибку, так как с join можно соединять только
            #строковые значения. для этого мы создали генератор списка, в котором каждое значение self.values
            #преобразовали к строке
            b = [str(i) for i in self.values]
            return f"Вектор ({', '.join(b)})"
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            b = [i+other for i in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = [sum(i) for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            b = [i*other for i in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                b = [i[0]*i[1] for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')





a = Vector(1,2,43)
b = Vector(1, 2, 43)
print(a*b)
