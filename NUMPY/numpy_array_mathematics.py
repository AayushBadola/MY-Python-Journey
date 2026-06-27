import numpy as np

array_1 = np.array([1,2,3,4]) # some array to do operations 

# if we copy array_1 and say array_copy = array_1, then if we change 2-> -2 that change will be reflected on original
# hence we use the function .copy for creating a deep copy of it 

# copying the original to perform operations 
array_2 = array_1.copy()
 

############# adding some number to the entire numpy array ############
print(f"Array BEFORE addition of 2 : {array_2} \n")
# important: 
# if we just write array_2 +2 and not equate it to array_2 then it creates some other array storing array_2 + 2
# if we dont equate it the actual value is NEVER updated
array_2 = array_2 + 2 # every single element is increased by 2 
# [1,2,3,4] -> [3,4,5,6]

print(f"Array AFTER addition of 2 : {array_2} \n")

# subtraction is just oppisite of addition so 

print(f"Array BEFORE subtraction : {array_2} \n")
array_2 = array_2 - 2 # should change the array [3,4,5,6] back to [1,2,3,4]
 
print(f"Array AFTER subtraction of 2 : {array_2} \n")

#### we can do basic mathematic operations as such : array (operator) value and the calculation is applied to each 
# value of the array 

############# mathematic operation of 2 arrays #############
array_3 = array_1.copy() # copy of original that is [1,2,3,4]
array_4 = array_1.copy() # another array we will add to the array_3

array_result = array_3 + array_4  # it will make [1,2,3,4] + [1,2,3,4] = [(1+1), (2+2), (3+3), (4+4)] -> [2,4,6,8]

print(f"Array 1 we have  : {array_3} \n")
print(f"Array 2 we have  : {array_4} \n")

print(f"Adding both array we get: {array_result}")

############## getting sin values of all the element inside numpy array #########
# we can get any trigonometric values by passing a function 

# np."trigonometric expression" -> so we can get sin , cos , tan, arctan , arcsin,arccos

array_values = np.array([1,2,3,4])
array_sin_values = np.sin(array_values)

print(f"Raw values: {array_values} \n")
print(f"corresponding sin values : {array_sin_values}")

# the values passing inside the trigonometric function (in this case array_values) are treated as radians NOT degree



