class MultiFilter:

    @staticmethod
    def judge_half(pos, neg):
        if pos >= neg:
            return True

    @staticmethod
    def judge_any(pos, neg):
        if pos > 0:
            return True

    @staticmethod
    def judge_all(pos, neg):
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = list(funcs)
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for element in self.iterable:
            pos, neg = 0, 0
            for i in self.funcs:
                if i(element):
                    pos += 1
                else:
                    neg += 1
            if self.judge(self, pos=pos, neg=neg):
                yield element


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(MultiFilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(MultiFilter(mul2, mul3, mul5, judge=MultiFilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(MultiFilter(mul2, mul3, mul5, judge=MultiFilter.judge_all)))
# [0, 30]