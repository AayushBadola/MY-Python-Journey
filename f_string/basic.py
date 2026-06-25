# used to write dynamic values inside the entire string
# we dont need to write print("String1" + variable1 + "string2" + variable2 . . . )

age = 19
name = "Aayush"

# method 1
print("Hello My name is ", name, " i am ", age, " Years old")
print("\n")


#method 2 (using f strings)
print(f"Hello My name is {name} i am {age} years old")
print("\n")
# insied stirngs we use a keyword "f" and to add the variable value to string we use
# "string 1 string 2 string 3 .... {variable 1} .... {variable2}"


# method 3 -> using "+" symbol BUT if data type is NOT string we have to convert it into string
print("Hello my name is " + name + " I am " + str(age) + " years old")
print("\n")
#method 4 -> NOT USING F STRING BUT ADDING VARIBALE BASED ON FORMAT 
# "string 1 string2..... {}....string3......{}".format(var1,var2,var3)
#here var 1 goes to 1st curly braces , 2nd goes to 2nd and so on

message = "Hello my name is {} , i am {} years old".format(name,age)
#after name the 1st curly braces gets value of name 
# after am and before years curly braces we get value of age
print(message)



