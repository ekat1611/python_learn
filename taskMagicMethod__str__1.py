class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        if gender != 'male' and gender != 'female':
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
print(p2.gender)
