# scope of variable is where and what functions the variable belongs to 
#if variable is outside of all functions then its global and every function can access it

# every function can READ global variables
# but modifying them requires 'global'

name = "Dave"
print("Name variable : ", name) # available to print

def greet():
    print("Printing name inside greet function: ", name)

greet() # prints the name dave as its accessable by all functions 

def modified_greet():
    color = "Blue"
    print("Printing name inside modified greet: " ,name , "\n Color specified in modified greet: ", color )

modified_greet() # prints both "Blue" and "Dave" as color = blue is specific to this function
# it also prints dave as name variable is global 

####################################### test function will not work ###############################
# def test_greet(): testing if color variable will work in another function
#     print("Inside test function name : ", name)
#     print("inside Test function color :", color)  will give error since color DOES NOT belong to it

# test_greet()

###################################### TEST FUNCTION END ##########################################


