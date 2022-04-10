#
# #task № 1
#
# class City:
#
#     def __init__(self,city):
#         city = city.lower().split()
#         self.name = [(i[0].upper() + i[1:]) for i in city]
#         self.name = (' '.join(self.name))
#
#     def __str__(self):
#         return self.name
#
#     def __bool__(self):
#         g = 'eyuioa'
#         if self.name[-1] in g:
#             return False
#         return True
#
# p1 = City('new york')
# print(p1)  # печатает "New York"
# print(bool(p1))  # печатает "True"
# p2 = City('SaN frANCISco')
# print(p2)  # печатает "San Francisco"
# print(p2 == True)  # печатает "False"


#task № 2

class Quadrilateral:

    def __init__(self, width, height = None):
        self.width = width
        if height is None:
            self.height = self.width
        else:
            self.height = height

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        if self.width == self.height:
            return True
        return False


q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"

