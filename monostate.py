class Mono:
    shared_dict = {}

    def __init__(self):
        self.__dict__ = self.shared_dict


d = Mono()
w = Mono()
d.d = 22
print(w.__dict__)

