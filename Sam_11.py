# Create a class Car which contains the following data members and member functions.
# Create three instances of the class. tCount variable should keep a record of the total Car
# manufactured. displayName and displayWeight method should display the name and
# weight of the Car instance. Using displaytCount() function print the total number of cars
# manufactured.
# Class Variable Instance Variable Methods
# tCount car_name __init__
# car_weight displayName
# displayWeight
# displaytCount


class Car:
    tCount = 0 # class variable to keep track of total cars manufactured
    
    def __init__(self, car_name, car_weight):
        self.car_name = car_name # instance variable to store car name
        self.car_weight = car_weight # instance variable to store car weight
        Car.tCount += 1 # increment total car count for each new instance created
    
    def displayName(self):
        print("Car name:", self.car_name)
        
    def displayWeight(self):
        print("Car weight:", self.car_weight, "kg")
        
    @classmethod
    def displaytCount(cls):
        print("Total number of cars manufactured:", cls.tCount)

# create three Car instances
car1 = Car("Sedan", 1200)
car2 = Car("SUV", 1800)
car3 = Car("Hatchback", 900)

# display car names and weights
car1.displayName()
car1.displayWeight()

car2.displayName()
car2.displayWeight()

car3.displayName()
car3.displayWeight()

# display total car count
Car.displaytCount()
