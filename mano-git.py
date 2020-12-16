#testavimas git

class Git:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def read(self,name):
        print(name)

    def __str__(self):
        return self.name +', '+ str(self.age)
        
a = Git("alio",22)
b = Git("blabla",33)
print(a)
print(b)
