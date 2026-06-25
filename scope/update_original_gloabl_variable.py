# if a global variable is read inside a function
# Python allows it automatically

# example:
# count = 1
#
# def test():
#     print(count)
#
# output = 1


# if we ASSIGN to a variable inside a function
# Python assumes it is a NEW LOCAL variable

# example:
# count = 1
#
# def test():
#     count = 2
#
# global count remains 1
# local count inside function becomes 2


# therefore updating a variable inside a function
# does NOT automatically update the global variable

# global count = 1
#
# function count = 2
#
# these become two separate variables


# to modify the global variable from inside a function
# we use the "global" keyword

# example:
#
# count = 1
#
# def test():
#     global count
#     count = 2
#
# now the original global variable is modified


# after calling test():
#
# global count = 2
#
# because function directly updated the global variable


# IMPORTANT:
# global is NOT written as:
# global count = 2
#
# WRONG ❌
#
# instead:
#
# global count
# count = 2
#
# CORRECT ✅

count = 1

def updation():
    print("I am inside function")
    count = 2 # it creates a variable named count NOT THE ORIGINAL COUNT 
    print("Value of count inside function: ",count)

updation()

print("I am in Global now ")
print("Value of count globally: ", count)

############updating the global value#########

# we know count = 1 GLOBALLY 

def updating_gloal():
    global count 
    count += 1 # updates count = 1
    print("I am inside the function")
    print("Value of count after updating inside function: ", count)

updating_gloal()

print("Count Global Value : ", count)


