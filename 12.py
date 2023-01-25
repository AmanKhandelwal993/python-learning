#inheritance in python 



print("#####################", end="\n\n")

print("Example-1")

## parent class
class vehicle:
    def __init__(self):
        print("This is a vehicle class")

## child class

class bike(vehicle):
    def __init__(self):
        print("This is a child class")

obj1 = vehicle()

obj2 = bike()



print("#####################", end="\n\n")

print("Example-2")

## parent class
class vehicle:
    def __init__(self):
        print("This is a vehicle class")

## child class

class bike(vehicle):
    def __init__(self):
        vehicle.__init__(self)
        print("This is a child class")

obj1 = vehicle()

obj2 = bike()




print("#####################", end="\n\n")

print("Example-3")

## parent class
class vehicle:
    def __init__(self,name,color):
        print("This is a vehicle class")
        self.name = name
        self.color = color

    def get_color(self):
        print(f"The color of {self.name} is {self.color} ")

## child class

class bike(vehicle):
    def __init__(self,name,color):
        vehicle.__init__(self,name,color)
        print("This is a child class")

print("#####################", end="\n\n")
print("Using Object of Vehicle Class")

obj1 = vehicle('KTM','Orange')

obj1.get_color()

print("#####################", end="\n\n")
print("Using Object of Bike Class")

obj2 = bike('KTM','Orange')
obj2.get_color()

print("#####################", end="\n\n")
print("Using Object of Bike Class")
obj3 = bike('Harley','Black')
obj3.get_color()




print("#####################", end="\n\n")

print("Example-4")

## parent class
class vehicle:
    def __init__(self,name,color):
        print("This is a vehicle class")
        self.name = name
        self.color = color

    def get_color(self):
        print(f"The color of {self.name} is {self.color} ")

## child class

class bike(vehicle):
    def __init__(self,name,color):
        vehicle.__init__(self,name,color)
        print("This is a child class")

## child class

class car(vehicle):
    def __init__(self,name,color,engine):
        vehicle.__init__(self,name,color)
        print("This is a child class")
        self.wheel = 4
        self.engine = engine

    def car_engine(self):
        print(f"The engine of {self.name} is {self.engine}")

print("#####################", end="\n\n")
print("Using Object of Vehicle Class")

obj1 = vehicle('KTM','Orange')

obj1.get_color()

print("#####################", end="\n\n")
print("Using Object of Bike Class")

obj2 = bike('KTM','Orange')
obj2.get_color()

print("#####################", end="\n\n")
print("Using Object of Bike Class")
obj3 = bike('Harley','Black')
obj3.get_color()

print("#####################", end="\n\n")
print("Using Object of car Class")

obj4 = car('Audi','Grey','V8')
obj4.car_engine()
obj4.get_color()

