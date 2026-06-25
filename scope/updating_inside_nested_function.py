# similar concept to updating global variable 
# refer to "update_original_global_variable.py"
# this method is similar to above mentioned just only used for nested functions 
# here the key word is changed from global -> nonlocal


def boss():
    color = "Blue"
    print("Color before updation in BOSS: ", color)
    def subordinate():
        color = "Red" # creates a varibale named color which is NOT the same one as color in boss
        print("Inside Subordinate function COLOR: ", color)
    
    subordinate()
    print("I am outside sibordinate and inside BOSS function the color is: ", color)
    print("Color is not updated !")


boss()

################## ACTUALLLY UPDATING THE VARIABLE ##############
print("################## ACTUALLLY UPDATING THE VARIABLE ################# \n")
def main():
    MAIN_COLOR = "red"
    print("Color in MAIN: ", MAIN_COLOR)
    def sub():
        nonlocal MAIN_COLOR # means we are now using MAIN_COLOR from main funciton
        MAIN_COLOR = "Blue" # updating the main color inside sub fucniton but change done to main
        print("Inside nested funciton the color is : ", MAIN_COLOR)
    
        sub() 
    print("Outside Nested funciton the COLOR IS : ",MAIN_COLOR)

main()