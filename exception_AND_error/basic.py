# Exceptiona and error go hand in hand 
# for every error we create an except statement that if that error occurs then different part of code will 
# be run 

# "try" block is the actual block which contains the code which needs to runs and may cause error 
# "except" block is the block which runs when an error is occured 
# we can have except block run on specific error by specifying which error may occur 

#print(x)  there is no "x" defined so it will throw error as is, so the program will stop
# the error will be NameError
# since its throwing error we will put it in try block 
try:
    print(x)
except NameError:
    print("Variable X is not defined \n please define x")
    x = input("Please provide the value of x")
    print(x," is stored in x")


print("\n")

# trying divison by 0
a = 6
try: 
    print(a/0) # dvision by 0 is a no go and doesnt happen so error will be ZeroDivsionError

except ZeroDivisionError: # when error is thrown this block of code is run 
    print("Can not divide by 0 please change the denominator")


# when no error occures or we cant catch any error
try:
    print(a/2)

except NameError:
    print(" variable a is not defined")

except ZeroDivisionError:
    print("Cant not allow division by 0")

else: # when no error is found or caught 
    print("No errors ! \n")


# how to run a line of code even if error occurs but we want a specific code to run anyways 
# we use a keyword "Finally"

try:
    c/2
except NameError:
    print("There is an error !")

finally:
    print("Even if there is error or not i will run regardless")