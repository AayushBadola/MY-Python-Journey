# literal ssignments
first_name = "Dave"
Last_name  = "Gray"

print(type(first_name)) # type() provides the type of value
#provides true as it checks for if given variable has same value as provided type  
print(isinstance(first_name, str)) 

# to assign a value we can also create a constructor 

pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza,str))


# CONCATINATION : joining 2 different strings

fullname = first_name + " " +Last_name
print (fullname)

# cast number to a string

decade = 1980 # it is an integer 
decade = str(1980) #using constructor to make value string

print(type(decade))