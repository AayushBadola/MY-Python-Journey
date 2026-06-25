# basic operations on a file 
# r = Read
# a = append
# w = write
# x = create

# there will be error if we read a file that doesnt exist 

file3 = open("names.txt")
file2 = open("names.txt")
file = open("names.txt") # opening the file named names.txt , 
# note  : since its in same directory we dont need path otherwise we need to provide full path for it 

print(file.read()) # we now access the opened file and read it with read() 

# we can also read certain "ammount" of information 
# in names.txt we have multiple names but we want to read frist 3 charector so we do file.read(n)

print("####################### reading first 3 charector ##################### \n \n")
print(file2.read(3))


# reading dile line by line
print("####################### reading file line by line ##################### \n \n")

print(file3.readline()) # reads line 1 
print(file3.readline()) # reads line 2 
print(file3.readline()) # reads line 3 
# readline does NOT read the entire file or charector it reads the entire line 1 or 2 or 3 . . .


## everytime we open a file or use f.open() we NEED to close the file in the end using f.close()
file.close()
file2.close()
file3.close()

## we can create a NEW file using APPEND (a)


file_creation = open("new_name.txt", "a" ) # "a" means append and creates a new file named new_names.txt
# if we read it we wont get anything since its empty 


# adding data in file using WRITE 
# if we read it we wont get anything since its empty 
file_creation.write("Joahana") # adds Joahana to empty file BUT IS NOT UPDATED TILL WE CLOSE THE FILE

file_creation.close() # now all the updated data is inside file_creation 


file_creation = open("new_name.txt") # we opened the file again to access its contents 
print(file_creation.read()) # now we are reading its contents 



