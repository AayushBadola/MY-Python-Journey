# say we have a class vehical 
class Vehical(): # () -> indicates it doesnt inherit from any class
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def moves(self):
        print(f" { self.make } moves along . . . ")

# class inheriting the Vehical class

class airplane(Vehical):
    def moves(self):
        print(f"{self.make} flys along . . . ")

# now we want that we dont want to only provide 2 parameters
# for vehicals say chopper we need a fly_id but vehical class doesnt have it so we have override it

class chopper(Vehical):
    def __init__(self, make,model,fly_id):
        super().__init__(make,model) # we are inheriting the entire init from vehical
                                          # so we are writing it again 
        self.fly_id = fly_id # we have added another parameter
    
    def moves(self):
        print(f"{self.make} with id {self.fly_id} hovers along . . . " )
    

my_vehical = Vehical("Tesla", "Model 3") # Parent class haivng 2 parameters
my_plane = airplane("Cessana", "Skyhawk") # child class with no overriding so 2 parameters
my_chopper = chopper("Airbus", "ACH160", "ABACH160DI2026") # child calss with 3 parameter overriding

my_vehical.moves()
my_plane.moves()
my_chopper.moves()

print("######################################################### \n \n")
# iterating through each object 
for vehical in (my_vehical, my_plane,my_chopper):
    vehical.moves()
    print(vehical.make)
    print(vehical.model)