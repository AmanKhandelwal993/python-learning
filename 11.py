##### class


print("#####################", end="\n\n")

print("Example-1")


class sampleClass:
    name = 'defaut'
    age = '' 
    designation = 'Default'


### create object 

object1 = sampleClass()

print(object1.name)

object2 = sampleClass()

print(object2.name)

object1.name = 'Aman'

object2.name = 'Karthik'


print(object1.name)

print(object2.name)


###############################


print("#####################", end="\n\n")

print("Example-2")

class vehicle:
    def __init__(self,type='default',speed='default',mileage='default'):
        self.type = type
        self.speed = speed
        self.mileage = mileage
        print("the Vehicle class is initiated")

obj1 = vehicle()



###############################


print("#####################", end="\n\n")

print("Example-3")

class vehicle:
    def __init__(self,type='default',speed='default',mileage='default'):
        self.type = type
        self.speed = speed
        self.mileage = mileage
        print("the Vehicle class is initiated")
        print(f"speed : {speed}")
        print(f"type : {type}")
        print(f"mileage : {mileage}")

obj1 = vehicle('car','40','50')


#########################

print("#####################", end="\n\n")

print("Example-4")

class vehicle:
    def __init__(self,type='default',speed='default',mileage='default'):
        self.type = type
        self.speed = speed
        self.mileage = mileage
        print("the Vehicle class is initiated",end='\n\n')      
    
    def get_vehicle_features(test):
        print('display feature of vehicle')
        print(f"speed : {test.speed}")
        print(f"type : {test.type}")
        print(f"mileage : {test.mileage}")


obj1 = vehicle('car','40','50')

obj1.get_vehicle_features()


#########################

print("#####################", end="\n\n")

print("Example-5")

class vehicle:
    def __init__(self,type='default',speed='default',mileage='default'):
        self.type1 = type
        self.speed1 = speed
        self.mileage1 = mileage
        print("the Vehicle class is initiated",end='\n\n')      
    
    def get_vehicle_features(test):
        print('display feature of vehicle')
        print(f"speed : {test.speed1}")
        print(f"type : {test.type1}")
        print(f"mileage : {test.mileage1}", end='\n\n')

    def update_vehicle_feature(self,type='None',speed='None',mileage='None'):
        if type != 'None':
            self.type1 = type
        if speed != 'None':
            self.speed1 = speed
        if mileage != 'None':
            self.mileage1 = mileage 


obj1 = vehicle('car','40','50')

obj1.get_vehicle_features()

obj1.update_vehicle_feature('suv')

obj1.get_vehicle_features()

obj1.update_vehicle_feature('truck','20', '10')

obj1.get_vehicle_features()

obj1.update_vehicle_feature(speed = '50', type = 'electric-car' , mileage='100')

obj1.get_vehicle_features()

print(obj1.type1)

##### for delete the object of class

del obj1

### will give error 
### print(obj1.type1)



