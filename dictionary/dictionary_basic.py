# dictionary is a key value pair storage 
# name = {
#     key1 : [value1,val2]
#     key2 : value2,
#     key3 : value3
# }

# keys -> can be string or integer 
# value -> can be string or integer

# creating dictionary using curly brackets/ elementry method

student = {
    "Name" : "Aayush",
    "Class" : "CSE",
    "Enrollment" : 58
}

# creating dictionary using constructor call

student2 = dict(Name = "Aayush", Class = "CSE", Enrollment = 58)

print("Created manually using elementry method : \n")
print(student, " \n")
print("Created by calling dict constructor: \n")
print(student2, "\n")

#len of dictionary is number of keys it has 
print("Length of dictionary : ",len(student2), "\n") # it has 3 keys so len = 3

#access items of dictionary 
# #print(dictionary_name[key])
# or
# print(dictionary_name.get(key))

print("Value of class: ",student2["Class"], "\n") # IT WILL GIVE CSE 

# "List" all the keys / show all the keys inside a list
print("All the keys in student2: ", student2.keys(), "\n")

#above provides an output dict_keys(['Name', 'Class', 'Enrollment']) where this is type "dict_keys"
#think its an object providing a realtime view of all the keys in the dictionary

# list of key-value pairs as tuples
print("ALL key - value pairs: ",student2.items(), "\n")

# verify if a key exist in dictionary
print("Does key 'Class' exist? ", "Class" in student2, "\n")

print("CSE" in student2["Class"], "\n")

# updating/altering dictionary 
student2["Name"] = "Neo"
# also updation using update method
student2.update({"Class": "EE"})

# adding new value to dictionary 
print("Before adding new vlaue: " ,student2, "\n")
student2["Section"] = "A"
print("After adding new value: ",student2, "\n")

# adding new value to dictionary using update command
student2.update({"Marks" : 30})
# if we use / update a key which is not there python creates that key-value pair

#remove items from dictionary , POP() needs an argument / key which needs to be removed 
print("Before removal : ", student2, "\n")
student2.pop("Section")
print("After removal: ", student2, "\n")

# list and tuple vales in dictionary 

basic = {
    "Class" : (["CSE", "ECE"], ["CS", "AI"], ["AIML","CSEM" ]),
    "Names" : (["Grey", "JJ"],["Alex", "Saul"], ["Sara", "Tony"])
}

print(basic)

# clearing an entire dictionary to create a empty dictionary that is basic = { }
print("Before clearing the dictionary", basic, "\n")
basic.clear()
print("After clearing dictionary: ", basic, "\n")

#delete dictionary 
del student

#bad copy of dictionary , when we do dict1 = dict_MAIN it creates a REFRENCE TO dict
# WHEN DOING THIS it creates a bad copy of dict_main where any change of dict1 will change dict_main

dict_MAIN = {'Name': 'Aayush', 'Class': 'CSE', 'Enrollment': 58}
dict1 = dict_MAIN

print("Main dictionary: ", dict_MAIN, "\n")
print("Bad copy dictionary: ", dict1, "\n")

dict1.update({"Name" : "Neo"})
print("Update dict1 \"Name\" : \"Neo\" ",dict1, "\n")
print("Original also updated as copy is updated : ", dict_MAIN, "\n")


#perfect copy of dictionary uses FUNCTION : dict1 = dict_MAIN.copy() we use method ".copy()"
# any change done to perfect copy will NOT be transfered to MAIN dictionary
dict_MAIN = {'Name': 'Aayush', 'Class': 'CSE', 'Enrollment': 58}
dict_perfect_copy = dict_MAIN.copy()


print("Main dictionary: ", dict_MAIN, "\n")
print("Perfect copy: ",dict_perfect_copy, "\n")
dict_perfect_copy.update({"Name" : "Neo"})
print("Change to perfect copy : Name = \"Neo\" ")
print("Pefect copy after change: ", dict_perfect_copy, "\n")
print("Main copy remained unchanged:", dict_MAIN, "\n")

# we can also create a perfect copy using a constructor 
dict_perfect_copy_2 = dict(dict_MAIN) # any change done to perfect copy will NOT be done to main