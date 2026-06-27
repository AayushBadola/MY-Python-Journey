import numpy as np 

# creating a numpy array 
array_0 = np.array('A') # just stores a single charector hence a 0 dimension array , no row , no col 


# stores one axis of elements, therefore a 1-D array.
# NumPy does not distinguish between row and column in 1-D arrays.
array_1 = np.array([1,2,3,4]) 

# ###################  A TRUE COLUMN VECTOR IS 2D 
array_column = np.array([
    [1],
    [2],
    [3],
    [4]
])


array_2 = np.array([[1,2,3,4], ['A','B','C','D']])# 2 D array say [1,2,3,4] is row 1 and ['A','B','C','D'] is row2

# Note : for creating any N-D array we need nested array so []<- main list   [ []<- row 1 ]
# [[] <- row 1 , []<- row 2 . . . . . [] <- row N ] -> it creates a 2-D matrix with N rows and M columns
# here M columns is the ammount of data in each row 

# if we do [ [ []<- inside row 1 ] <- row 1 , [ []<- inner row 2 ]<-row2] then it creates a cube of data so 3D 

array_3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])

# here there are 27 number and how many squares DOES A CUBE HAS ? -> 3X3X3 -> 27
# so think of each number as a square inside a 3X3X3 rubics cube 

#################### dimension of each array ##################

print(array_0.ndim) # prints diminsion of array_0 -> it should be 0 dimension

print(array_1.ndim) # prints dimension of array_1 -> should be 1

print(array_2.ndim) # dimension of array_2 -> 2

print(array_3.ndim) # dimension of array_3 -> 3


############### shape the array take ############

print(array_0.shape) # shape is ()
                    # empty tuple because it is a scalar (0-D array)

print(array_1.shape) 
# shape (4,)
# one axis containing 4 elements
# NumPy does not treat this as a row or column vector


print(array_2.shape) # has a shape of matrix with 2 rows and 4 columns so (2,4)

print(array_3.shape) # has shape of a cube with a dimension of 3,3,3 so (3,3,3)

############################### ACCESSING VALUE FROM N-D ARRAY ###########################

# to access value we need to provide the specific address of that value

##### 1-D test array accessing

test_1_D = np.array([1,2,3,4])
print(test_1_D[2]) # so index 2 that holds value 3 

test_2_D = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

############### 2-D test array accessing

print(test_2_D[0][0]) # row 0 and column 0 so value 1 

print(test_2_D[0][1]) # row 0 column 1 that holds value 2

# generally in 2D array ->  arr[row][col]

############### 3-D test array accessing

test_3_D = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        # think of it as matrix 1
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
        # think of it as matrix 2 
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
        # think of it as matrix 3 
    ]
])

# so its 
# [matrix1]
# [matrix2]
# [matrix3]
# it would make a cube as we already have it stored planely in matrix and stacking matrix we get "height"

print(test_3_D[0][0][0]) # it like this matrix 0 -> row 0 of matrix 0 -> col 0 of matrix 0 
# hence it prints 1

print(test_3_D[2][2][1]) # matrix 3 -> row 3 -> col 2 -> 26

################## getting entire rows of 2D array 
print(test_2_D[0,:]) # prints all the column values of the row 0

################## getting entire columns from 2D array 
print(test_2_D[:,0]) # prints all the row values from column 0


########################### updating values for N-D array ########################

# for any array we can overwrite/ update the value by assigning new value to the index

for val in test_1_D: # prints all value inside array 
    print(val)

print("Value before updation: ", test_1_D[1])
test_1_D[1] = -2 # original value is 2 , changing it to -2
print("Value after updation: ",test_1_D[1])

######################## zero matrix ########################

array_zero = np.zeros((3,3), dtype = int) # general form -> np.zero((row,col))
# creates a matrix with all 0 values of 3 rows and 3 columns
print("\n")
print(array_zero)

####################### one matrix #########################
array_ones = np.ones((2,3), dtype = int) # general form -> np.ones((tuple of shape that is row,col), dtype = "datatype")
print("\n")

print(array_ones) 

## SPECIAL ONES MATRIX -> n x n ones matrix is a IDENTITY MATRIX 

###################### Matrix with all same custom values #################
array_custom = np.full((3,3), 99)
# creates a 3X3 matrix with all values being 99

print("Testing \n")
array_test = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        # think of it as matrix 1
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
        # think of it as matrix 2 
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
        # think of it as matrix 3 
    ]
])

print("entirety of matrix 2 ")
print(array_test[1,:,:]) # provides me the 2nd layer that is matrix 2 

print("All the 2nd row fomr all the 3 matrices \n")
print(array_test[:,1,:]) # provides me the 2nd row of all the matrices
# this above function works like this 
#   [row from matrix 1]
#   [row form matrix 2]
#   [row from matrix 3]

print("All the 2nd columns fomr all the 3 matrices \n")
print(array_test[:,:,1]) # provides me the 2nd column of all the matrices 
# this above function works like this 
#   [col from matrix 1]
#   [col form matrix 2]
#   [col from matrix 3]

###################### creating an array "Similar" to an original array ###################

# similar to np.full((shape), value)
# here instead of shape we pass an array whose shape we want to use 

# let the original array be original_array
original_array = np.array([
    [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ],
    [
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R']
    ],
    [
        ['S', 'T', 'U'],
        ['V', 'W', 'X'],
        ['Y', 'Z', 'AB']
    ]
])

array_like_original = np.full_like(original_array, 12) # creates an array of 3x3x3 with all values being 12

print("Array like original with 3X3X3 \n \n")
print(array_like_original)
print("\n")

####################### ARRAY WITH RANDOM "DECIMAL" NUMBERS ##############
# we can use the random module using the numpy module 
# it can be called using numpy.random.rand()
# it generates numbers from 0->1

random_array = np.random.rand(3,3,3,3)

print("Randomly generated array \n \n")
print(random_array,"/n")

# get same shape as some original array but with random generated values 0->1

################### IMPORTANT REVELATION #################
# random_array_like_original = np.random.rand(original_array.shape) WILL NOT WORK AS .shape will give tuple
# but the random.rand() takes in individual argument so random.rand(3,3) NOT random.rand((3,3))
# to overcome this we use random.rand(*original_array.shape) it will unpack the values from tuple 
random_array_like_original = np.random.rand(*original_array.shape)
print("Random array like with same shape as some original array \n")
print(random_array_like_original, "\n")

###################### ARRAY WITH RANDOM "INTEGER" NUMBERS ##############
# we cna create the randomarray using the same function 
# random.rand() just replace rand -> randint
print("Random array generated with numbers 2->10 integer numbers: ")
random_int_array = np.random.randint(2,10,size=(3,3)) # 2->10 random values 
                                                        # size = 3x3 

print(random_int_array, "\n")

########################## creating an identity matrix ###################
# since matricesare 2D hence its shape is nXn where n is integer 
# function is used as np.identity(n)
# identity matrix where diagonal elements are all 1 and else 0 
matrix_identity = np.identity(3) # creates a 3X3 identity matrix
print("3X3 identity matrix : \n")
print(matrix_identity, "\n")

########################## REPITITION OF ARRAY ###########################
# to repeat an array we need np.repeat(array which will be repeated , how many times to repeat,)
some_array = np.array([[1,2,3]]) # Note : IT WONT WORK FOR JUST ONE LIST BUT FOR NESTED LIST, or a 2D array 
repeated_array = np.repeat(some_array,  3, axis = None)
print("Array after repeating [1,2,3]: \n")
print(repeated_array)

# BY DEFAULT AXIS = NONE
# numpy by deault flattens the array and repeats the elements 
#[1,2,3] -> [1,1,1,2,2,2,3,3,3] go along the column direction and repeat the elements 

# same case for axis = 1

# [1,2,3] if we do axis = 0 we go row wise and repeat 
# hence [1,2,3]
    #   [1,2,3]
    #   [1,2,3]

############################# CREATE PATTERN #####################
# to create a pattern 

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# here we can see its 5X5 array with outer elemnts as 1 
# with 9 being odd one out at index 2,2

# create a ones matrix and fill inside with 0 and then update the 2,2 index with value 9 

array_pattern = np.ones((5,5), dtype=int) 
# created array 
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
####################### method 1 ########################3
# here we assign those row col with val 0
# later we assign 2,2 = 9
array_pattern[1:4,1:4] =  0# for numpy array its array[row,col]
# here we get row 2->5 and col 2-> 5 
array_pattern[2,2] = 9
print("The pattern is : \n")
print(array_pattern, "\n")


############### method 2 ##########
# overlapping different arrays 
# create 1 matrix 

array_pattern_2 = np.ones((5,5), dtype=int)
# create intermediate matrix of 0 with size 3,3
intermediate_array = np.zeros((3,3), dtype = int)

# overlap those 2 array so we get the 0 values for 1:4,1:4

array_pattern_2[1:-1, 1:-1] = intermediate_array # selecting every single element in original

# create teh odd one out value 9 at 2,2 
array_pattern_2[2,2] = 9
print("Pattern with alternate method: \n")
print(array_pattern_2, "\n")

