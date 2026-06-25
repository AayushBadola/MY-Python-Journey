# Tuples are immutable sequences.
# Once created, individual elements cannot be changed.

# Example:
# mytuple[0] = "New Value"  -> TypeError

# Tuples do not support:
# append()
# remove()
# pop()
# insert()

# However, we can create a NEW tuple and reassign the variable.

# Creating a tuple
mytuple = ("Aayush", 20, "CSE", True)

# Creating a tuple using constructor
mytuple2 = tuple(("Aayush", 20, "CSE", True))

# one element tuple 
test1 = ("Aayush") # NOT A TUPLE ITS A STRING
test2 = ("Aayush",) # its a tuple cuz it has a ","


# This does NOT modify the tuple.
# It creates a new tuple and reassigns the variable.
mytuple = ("Aayush", 20)

mytuple = ("Aayush", 20, "CSE")

# to update and play around with tuple values we need to create list of that tuple values
mylist = list(mytuple)
mylist.append('Bachelor')
print(mylist)

# Convert the modified list back into a tuple
# and reassign the variable
print("Original tuple: ",mytuple)
mytuple = tuple(mylist)
print("Updated Tuple using list as an intermediate step: ", mytuple)

