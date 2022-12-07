class ExtendedStack(list):
    def sum(self):
        self.append(self.pop(-1) + self.pop(-1))

    def sub(self):
        self.append(self.pop(-1) - self.pop(-1))

    def mul(self):
        self.append(self.pop(-1) * self.pop(-1))

    def div(self):
        self.append(self.pop(-1) // self.pop(-1))
