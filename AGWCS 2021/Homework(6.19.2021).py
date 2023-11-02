class Parent():
    def __init__(self):
        self.name = "Amelia Wang"
        self.age = "37"

    def greeting(self):
        print("Hello. My name is " + self.name + ", and I am " + self.age + ". Pleased to meet you.")


class Child():
    def __init__(self):
        self.name = "EMMA"
        self.age = "6"

    def greeting(self):
        print("HI! IM " + self.name + " AND IM " + self.age + "! BYE!")

pant = Parent()
chl = Child()
for i in (pant, chl):
    print()
    i.greeting()
print()
