users = ['Dave', 'John', 'Sara']

data = ['dave', 42, True]

empty = []

# prints entire lists
print(users)

# check if value is in list
print('Dave' in users)

#indexing in list 
print(users[0]) # provides teh first value in list

print(users[1]) # provides 2nd value in list

# check for a position of value in list

print(users.index('Sara'))
print(data.index(42))

# print specific things frmo a list print(users[from:to:step]) OR print(users[from:to])
print(users[0:3:2]) # start is starting , next thing we take start + step if its less than end

#length of list 
print(len(data)) # length of list = numebr of item in list

# add more item in list
users.append('Elsa') # we can also do users += 'Elsa'

print(users)

# append doesnt take 2 values to add more than 1 value use extend
print('Old data: ', data)
data.extend(['Robert', 2, False, 'New coder'])
print('New data: ' , data)


# inserting new values at specific locations <list_name>.insert(position, value)

#original users = ['Dave', 'John', 'Sara', 'Elsa']
print("old users : ",users)
users.insert(2,'bob') # we can also use users[2:2] = ['bob', 'alex']
# ON 2nd index bobby is added and sara is gone to 3rd index elsa is gone to 4th index 

print("New users: ", users)

## removing specific value from list, needs specific value 
users.remove('bob') 
print(users)

#remvoe specific value from, and needs index also it stores the popped value
users.pop(3)
print(users) 

#delete specifc value from list , needs specific index adn does not store delted value 
del users[0]

#making teh list empty 
print("Old value: ", data)
data.clear()
print("New value: ", data)

#sorting a list , list is sorted for string alphabet wise , for integer,float,double its acending
numlist = [4,10,22,1,-40,2,90,12,45]
print("Old val: " , numlist)
numlist.sort()
print("sorted val: ", numlist)

#sorting a list even with having upper value and lower values
users.sort(key=str.lower)
print(users)

#sorting numbers for descending 
numlist.sort(reverse=True)
print(numlist)

#to sort the list only once and change it back after emthod is called
testlist = [21,30,90,11,-49,42,43,46,23]
print("Origianl : ", testlist)

print("current method call: ",sorted(testlist, reverse=True)) # sorts in decending order
print("After global sorted method call: ", testlist)

#create a list using a list constructor
mylist = list([1,143,22,34,88,35])
print(mylist)

#list copy shallow 
numscopy = mylist.copy()
nums2copy = list(mylist)

print("original's copy: ", numscopy)
numscopy.sort()
print("Original's copy after sort: ",numscopy)
print("Original remains untouched: ", mylist)
#here if there are nested lists that is [[val1,val2], [val3,val4]] then when deleting or adding value, it iwll change original list 
