class Person: 
	def __init__(self, name, age, job):
		self.name = name
		self.age = age
		self.job = job
	def birthday(self):
		self.age =+1

class Dog:
    __hungry = 0
    __tired = 0

    def __init__(self, name, weight, height):
        self.__name = name
        self.__weight = weight
        self.__height = height

    def bark(self):
        self.__hungry+=1
        self.__tired+=1

    def eat(self):
        self.__hungry = 0


    def speak(self):
        print("hungry: " + str(self.__hungry) + " tired: " + str(self.__tired))
