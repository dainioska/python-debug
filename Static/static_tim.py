#Static and Class methods:

class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def getPopulation(cls):
        return cls.population 

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

new_person = Person('tim', 22)
print(new_person.getPopulation())
print(Person.getPopulation())
print(Person.isAdult(15))