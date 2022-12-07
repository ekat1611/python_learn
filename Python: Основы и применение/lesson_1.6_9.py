import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, x):
        super().append(x)
        self.log(msg = x)


x = LoggableList()
x.append("32432")