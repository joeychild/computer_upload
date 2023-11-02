#Problem 1
class Car():

    def __init__ (self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.price = price
    
    def yearPassed(self):
        self.year += 1

    def drive(self):
        self.mileage += 100
    def __init__ (self):
        self.color = "red"
class Truck():

    def __init__ (self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.price = price
    
    def yearPassed(self):
        self.year += 1

    def drive(self):
        self.mileage += 100
    def __init__ (self):
        self.company = "Amazon Prime"
class Motorcycle():

    def __init__ (self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.price = price
    
    def yearPassed(self):
        self.year += 1

    def drive(self):
        self.mileage += 100
    def renewLicense():
        print("I have renewed my license.")

#Problem 2
class Vehicle:

    def __init__ (self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.price = price
    
    def yearPassed(self):
        self.year += 1

    def drive(self):
        self.mileage += 100

class Car(Vehicle):
    def __init__ (self):
        self.color = "red"
class Truck(Vehicle):
    def __init__ (self):
        self.company = "Amazon Prime"
class Motorcycle(Vehicle):
    def renewLicense():
        print("I have renewed my license.")

#Problem 3
class Parent():
    def __init__ (self):
        self.language = "Chinese"
        self.intelligence = 350
        self.eyeColor = "black"

    def learn(self):
        self.intelligence += 10
    
    def information(self):
        print("Language(s): " + str(self.language), "Intelligence: " + str(self.intelligence), "Eye color: " + self.eyeColor, sep = " -- ")

class Child(Parent):
    def learnLanguage(self, language):
        self.language = self.language, language

    def __init__ (self):
        Parent.__init__(self) 
        self.intelligence = 100

pant = Parent()
chld = Child()

pant.information()
pant.learn()
pant.information()
print()

chld.information()
chld.learnLanguage("English")
chld.information()
