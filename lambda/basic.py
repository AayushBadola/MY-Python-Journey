# LAMBDA FUNCTIONS

# lambda functions are small anonymous functions
# anonymous = function has no name

# normal function

# def add_2(num):
#     return num + 2

# lambda equivalent

add_2 = lambda num : num + 2

# lambda input  : operation/result
# lambda num    : num + 2

print(add_2(3))


# lambda can take multiple arguments

sum = lambda a,b : a+b

# a,b are inputs
# a+b is returned automatically

print(sum(3,5))


########################################################
# MAP
########################################################

# map applies a function to EVERY element
# of an iterable (list, tuple, set etc)

numbers = [3,2,4,6,1,0,8,7]

# square every number

squared_numbers = map(
    lambda num : num*num,
    numbers
)

# map returns a map object
# convert to list to see output

print(list(squared_numbers))

# example

# numbers = [1,2,3]

# lambda num : num*num

# becomes

# [1,4,9]


########################################################
# FILTER
########################################################

# filter keeps ONLY the values
# which satisfy a condition

# lambda must return:
# True  -> keep value
# False -> remove value

odd_num = filter(
    lambda num : num%2 != 0,
    numbers
)

print(list(odd_num))

# example

# numbers = [1,2,3,4,5]

# condition:
# num%2 != 0

# result:
# [1,3,5]

# NOTE:
# your code had:

# lambda num : num*num

# this is wrong for filter

# because filter expects:
# True or False

# not a squared number


########################################################
# REDUCE
########################################################

from functools import reduce

# reduce combines all elements
# into ONE final value

numbers2 = [1,2,3,4,5,6]

total = reduce(
    lambda acc,curr : acc + curr,
    numbers2
)

print(total)

# acc = accumulator
# curr = current value

# working:

# acc=1 curr=2
# 1+2 = 3

# acc=3 curr=3
# 3+3 = 6

# acc=6 curr=4
# 6+4 = 10

# acc=10 curr=5
# 10+5 = 15

# acc=15 curr=6
# 15+6 = 21

# final result = 21


##################### summary #######################

# lambda
# -> create small anonymous function

# map
# -> apply function to every element

# filter
# -> keep only elements satisfying condition

# reduce
# -> combine all elements into one final result