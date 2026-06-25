# set stores ONLY unique values

# duplicates are automatically removed
# while creating or updating the set

my_list = list([1,2,3,4,5,6,66,2,3])
print("List: ",my_list, "\n")

#even for the same values in list it provides the unique values and disregards the duplicate
my_set = {1,2,3,4,5,6,66,2,3}
print("Set : ",my_set, "\n")

#lenth of set is total number of UNIQUE elements -> set ={1,1,1,1,1,1} -> length = 1
#since there is only 1 unique element that is 1 rest of 1s are duplicate

print(len(my_set), "\n") # 7 unique elements so len = 7

# true = 1, false = 0
# if set = {1,true,33, 3, 0, false} -> we get -> {1, 33, 3, 0} since we got 1 so true is ignored 
# since true is considered 1 so its a duplicate, we got 0 before false so it got ignored 

num_set = {1,True,33, 3, 0, False, 3}
print(num_set, "\n")

#check if value is in set 
print(5 in num_set, "\n") # gives false sicne its not in set 

print(1 in num_set, "\n") # true since 1 is unique value and is inside the set

# add a new unique element to set BUT we can also add an element to set which is already present 
# if set = {1, 5, 2, 88, 2} then we can add -> a new element OR an existing element , say "5" AGAIN
print("set before updating: ",num_set, "\n")
num_set.add(10) # we dont know where it will appear since sets are unordered
print("Set after updating using the \".add\" command: ", num_set, "\n") 

# we can also add a "set" to a set using the update command
# sets are unordered
# so we do not know where it will appear
intermediate_set = {50,90,0,-100}
print("Set befroe suing update command:", num_set, "\n")
num_set.update(intermediate_set)
print("Set after updating using \"update method\": ",num_set, "\n")


# creating new set using 2 or more different sets (or the same)
set1 = {5,2,-5,22}
set2 = {2,-5,100,55}

set_combined = set1.union(set2)
print("combination of set1 {5,2,-5,22} and set2 {2,-5,100,55} \nwhile keeping unique elements : ", set_combined, "\n")

# keeping only duplicated (only having teh values which are same in set 1 and set 2 in combined set)

set_combined = set1.intersection(set2)
print("combination of set1 {5,2,-5,22} and set2 {2,-5,100,55} \nwhile keeping elements same in both sets: ", set_combined, "\n")

# only have elements which do have a duplicate in another set so {1,2,3} {2,3,4} -> {1,4}, since {2,3} are in both set, 
# it updates set1 to {1,4} instead of creating a new set called set_combined
set1 = {1,2,3}
set2 = {2,3,4}
set1.symmetric_difference_update(set2)
print("Combined set with only numbers which are fully unique and not duplicates : ", set1, "\n")

