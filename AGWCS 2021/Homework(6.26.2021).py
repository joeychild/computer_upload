from abc import ABC

class child(ABC):
    def age(self):
        pass

class Tim(child):
    def age(self):
        print("I am 7.")

class Jill(child):
    def age(self):
        print("I am 2.")

class Gennifer(child):
    def age(self):
        print("I am 15.")

t = Tim()
j = Jill()
g = Gennifer()

for i in (t, j, g):
    i.age()