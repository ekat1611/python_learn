class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return (self.capacity - v) >= 0

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v


a = MoneyBox(10)
print(a.add(8))
print(a.capacity)
print(a.add(1))
print(a.capacity)
