class Robot:
    population = 0

    def __init__(self, name):
        Robot.population += 1
        self.name = name
        print (f'Робот {self.name} был создан')

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(cls.population, ', вот сколько нас ещё осталось',sep = '')


a = Robot('name')
a.destroy()
a.say_hello()
a. how_many()