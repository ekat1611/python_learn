class Magic:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.y - self.x)


test = Magic(3, 1)
print(len(test))
