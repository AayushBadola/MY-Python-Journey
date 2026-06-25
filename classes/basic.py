# classes are blueprint for object 
class Vehical:
    def __init__(self, make,model):
        self.make = make
        self.model = model
    def moves(self):
        print("Moves along.....")

my_car = Vehical('Honda', 'Base') # creates an object of class vehical, forces to have 2 argument
my_car.moves() # provides us the predefined function from the class

my_new_car = Vehical('Tesla', 'model3')
my_new_car.moves()

print(my_new_car.make) # info about company
print(my_new_car.model) #info about model we provdes as argument when making the object 


class airplane(Vehical): # ariplane class now has the behaviour of the vehical class
                         # airplane class "inherits" the vehical class
    def moves(self):
        print("Flies along ...")

class chopper(Vehical): # similar to airplane class
    def moves(self):
        print("Hovers along . . .")

my_airplane = airplane("Cessna", "skyhawk") # taking the same parameter as vehical
my_chopper = chopper("Airbus", "ACH 160")

my_airplane.moves()
my_chopper.moves()





