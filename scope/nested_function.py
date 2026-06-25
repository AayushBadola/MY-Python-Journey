#a normal function taking in an argument
def greeting(name):
    print(" RIGHT NOW Printing Name inside greeting: ", name)

# modified function calls greeting function with the input of "Dave"
def modified_geeting():
    greeting("Dave") # goes to greet function with input "Dave"
    print("RIGHT NOW I AM INSIDE modified greeting function !") # still inside modifed function

modified_geeting()

# TRUE NESTED FUNCTION 
name2 = "Dave"

def boss():
    color = "Blue" #color variable behaves as a global variable for all the functions defined
                   #inside the boss function, COLOR FUNCTION HERE IS "ENCLOSING SCOPE"
    def subordinate() :
        print("WE ARE INSIDE the subordinate function which is inside BOSS function \n")
        print("Printing Name inside subordinate function: ", name2, "\n")
        print("Printing Color inside subordinate function \n color is defined in BOSS fucntion: ",color,"\n")
    
    subordinate() # calling the subordinate funciton so we runt eh subordinate function inside boss
    

boss()
