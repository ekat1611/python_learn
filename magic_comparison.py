# Магические методы сравнения:
# __eq__ отвечает за ==
# __ne__ отвечает за !=
# __lt__ отвечает за <
# __le__ отвечает за <=
# __gt__ отвечает за >
# __ge__ отвечает за >=
# Их все реализовывать не надо, достаточно выбрать __eq__ и ((__lt__ и __le) или (__gt__ и __ge__).
# Так как Питон переворачивает знак,если не находит такую операцию, мы можем получить весь функционал,
# используя лишь 3 реализации

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return other.a == self.a and other.b == self.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other
        # or return other.area == self.area or self.area < other.area


r = Rectangle(1,2)
d = Rectangle(3,4)
print(r>d)
print(r<d)
print(r==d)
print(r!=d)
print(r>=d)
print(r<=d)