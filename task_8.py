class Static:
    def __init__(self, x):
        self.x = x

    @classmethod
    def returning(cls,new_x):
        if new_x > 0:
            return False
        else:
            return True

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if self.returning(new_x):
            raise ValueError('NO')
        self.__x = new_x


# test_addoption.py = Static(-1)
# ValueError
test = Static(1)
print(test.x)
test.x = 2
print(test.x)
# 2
# test_addoption.py.x = -1
# ValueError