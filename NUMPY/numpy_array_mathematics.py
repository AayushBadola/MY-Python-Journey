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
print(f"corresponding sin values : {array_sin_values}\n" )

# the values passing inside the trigonometric function (in this case array_values) are treated as radians NOT degree

########### creating a sequence of values for array #############
# we can create a sequnce of number using "arange" that is a-range
# where the parameters are arange(start , stop, step size)
sequence_array_step_2 = np.arange(0,10,2)
sequence_array_step_1 = np.arange(0,10,1)
# this will start from 0 end with 10 and step size of  2
print(f"Seuence array is with step size 2 : {sequence_array_step_2} \n")
print(f"Seuence array is with step size 1 : {sequence_array_step_1} \n")

############ sorting of numpy array ###################
# for sorting any numpy array we can call np.sort() function

# #################### sorting a single axis numpy array ###################
single_axis_arr = [10,1,5,92,11,432,101,95]

sorted_single_axis_arr = np.sort(single_axis_arr)
print(f"ORIGINAL single axis array: {single_axis_arr} \n")
print(f"sorted single axis array: {sorted_single_axis_arr} \n") # sorts just like normal array

# ################# sorting a N-D numpy array ##################
multi_dimension_arr = [[2,3,1],[-2,4,6],[0,7,9]] # a 3x3 array 
sorted_multi_dimension_arr = np.sort(multi_dimension_arr) # sorts entire array as a whole
# by default, np.sort sorts along the last axis (rows for a 2D matrix)

print(f"Original multidimension array: \n {multi_dimension_arr} \n")
print(f"Sorted multidimension array: \n {sorted_multi_dimension_arr} \n")

sorted_multi_dimension_arr_col = np.sort(multi_dimension_arr, axis=0) # sorts column 
# axis = 1 -> sort each row independently
# axis = 0 -> sort each column independently
print(f"Sorting multidimension across axis: \n {sorted_multi_dimension_arr_col} \n")

############### multiple indexing #############
# say for array [1,2,3,4,5] we have index 0,1,2,3,4
# if we create another "List" containing only the indexes we want say 1 AND 4
# we pas that array to the original one and we get those values on those indexes in a list 

val_arr = np.array([1,2,3,4,5])
indx_arr = np.array([1,4])
final_arr = val_arr[indx_arr]
print(f"FInal array with indx 1,4 : {final_arr} \n")

#### USING NP WHERE TO GET VALUES SATISFYING A CONDITION #############
# np where allows us to put the result of np.where[condition] inside the index value 
# so for [1,2,3,4,5,6], result = np.where[arr > 2] and print(arr[result]) we get values >2

arr = np.array([1,2,3,4,5,6])
result_index = np.where(arr>2)
print(f"Values inside arr greater than 2: {arr[result_index]} \n")

############### CONCATE NUMPY ARRAY ###################
# if we do numpy array 1 + numpy arr 2 then each of their element are added 

# basically we get 
# [1,2,3]
# [4,5,6]
# --------
# [5,7,9]

# to concate numpy array we need to use CONCATE 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
combined = np.concatenate((arr1,arr2)) # contacts those 2 -> [1,2,3,4,5,6]

print(f"Array 1: {arr1} \n")
print(f"Array 2: {arr2} \n")
print(f"Using normal \"+\" operation : {arr1 + arr2} \n")
print(f"Using concatination for numpy array: {combined} \n")

################ ROW STACKING #################
# we can stack rows to an original array BUT THIER SHAPE SHOULD BE SAME 


orignal_matrix = np.array([[1,2,3],
                          [4,5,6] ])

# BUT WE WANT [7.8.9] AS WELL SO WE DO VSTACK 

new_row = np.array([7,8,9])
new_matrix = np.vstack((orignal_matrix, new_row)) # since matrix is in form [ [row] [row]]
                                  # so we added [ [new row] ] so it fits in the matrix

print(f"Old matrix: \n{orignal_matrix} \n")
print(f"Row to be added: {new_row} \n")

print(f"New matrix after addition : \n {new_matrix}")

############## STACKING HORIZONTALLY #############3
# we stack horizontally the data we need so basically adding columns to a matrix 
# if i do [1,2,3,4] and horizontally stack [5,6,7] then it becomes [1,2,3,4,5,6,7]
# if we do vstack it on data with same shape then it becomes a matrix 

# if we do 
# [1,2,3]
# [4,5,6]
# and we add 
# [10] 
# [20]
# we get [1,2,3] [10] -> [1,2,3,10]
#        [4,5,6] [20] -> [4,5,6,20]

new_col = np.array([[10], [20]]) # 10 is row 1 and 20 is row 2 "SEE THE COMMA"

new_matrix_col = np.hstack((orignal_matrix, new_col))
print(f"Original matrix \n {orignal_matrix} \n")
print(f"New column: \n {new_col} \n")
print(f"Matrix with new cols: \n {new_matrix_col} \n")