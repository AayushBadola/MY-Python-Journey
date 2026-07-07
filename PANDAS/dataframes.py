# data frames are a tabular data structure and we can store whatever we want (basically excel)
# data frame is made of rows and columns 
import pandas as pd

data = {
    "Name" : ["spongebob", "patrick", "squidward"],
    "age"  : [30,32,50]
}

######################## creating a data frame df #########################
df = pd.DataFrame(data,index=["Emp1", "Emp2", "Emp3"])

# The DataFrame is a 2D table.
# Unlike NumPy arrays, different columns can store different data types.

# a data frame column is a series
#            Name  age
# Emp1  spongebob   30
# Emp2    patrick   32
# Emp3  squidward   50

####################### ACESSING VALUES IN DATA FRAMES ###############
# we can access it similar to a series using loc OR iloc

print(f"Accessing employee 1:\n{df.loc['Emp1']}\n") # gives us the "ROW" EMP1
print(f"Acessing the column of names:\n{df['Name']}")
# note: we can NOT use df.loc["Name"] to get the entire column 
# BUT WE CAN USE IT LIKE THIS : df.loc[:,"Name"]
print(f"Entire data frame:\n{df}\n")

print("Now By doing iloc and doing values 0,1,2 we get values of row 1,2,3 respectively \n")
print(f"Specific value using row 1 to get same result as emp 1:\n{df.iloc[0]}\n")

################## ADDING NEW COLUMN TO DATA FRAME #######################
print(f"Before adding column :\n{df}\n")
df["job"] = ["cook", "N/A", "Cashier"] # same concept as dictionary just extended to data frame

print(f"After adding new column:\n{df}\n")

################ ADDING NEW ROW TO DATA FRAME ############################
# we can create new rows using .loc we can add new rows BUT COMMON METHOD IS GIVEN BELOW : 
# we will create a new data frame and then concatinate the data frame 
# for that we will create a new data frame containing a list that contains a dict

new_row = pd.DataFrame([{
    "Name" : "Aayush",
    "age"  : 19,
    "job"  : "10X data engineer" # ;)
}]  , index= ["Emp4"]) # here in the 1st list we created a dict that will be added to our original to have 
                       # to have another row and after the 1st "list" we add the index that is Emp4

# updating the df 
print(f"Before concatination of the new row :\n{df}\n")
print(f"Now we concatinate the row :\n{new_row}\n")
df =  pd.concat([df, new_row])
print(f"After concatination and adding new row :\n{df}\n")

############### ADDING MULTIPLE ROWS TO A DATA FRAME ###################

# IMPORTANT : if want to add new rows MAKE SURE the column names match the original 
# other wise if there is a difference say Name and name then there will be another col called "name"

# if we want to add multiple rows we will create a list and in side that list create 
# what ever number of dictionary we need 
# if we need 4 new rows added we will create 4 dictionary inside the list 

df2 = pd.DataFrame({
    "Name" : ["Ash", "Misty", "Brock", "Pikachu"],
    "Job"  : ["Trainer", "Water gym", "Rock gym", "Traveller"],
    "Age"  : [10, 10, 15, 5]

}, index=["Partner 1", "Partner 2", "Partner 3", "Partner 4"])

# we will create a data frame that will be
               
#               Name        Job  Age
# Partner 1      Ash    Trainer   10
# Partner 2    Misty  Water gym   10
# Partner 3    Brock   Rock gym   15
# Partner 4  Pikachu  Traveller    5

# we now want to add 2 new rows by one operation so we can create a data frame containing those 2 rows and then concatinating it 

# say we want to add "Dawn" and "Sarena" so now we will create a data frame containing same cols Name, Job , Age and 2 rows 

new_rows = pd.DataFrame({
    "Name" : ["Sarena", "Dawn"],
    "Age"  : [10, 10],
    "Job"  : ["Trainer", "Trainer"]
} , index=["Partner 5", "Partner 6"])

# we created new rows 
#              Name  Age      Job
# Partner 5  Sarena   10  Trainer
# Partner 6    Dawn   10  Trainer

# now we concatinate it and combine we will get new rows 

print(f"Before concatinating and adding multiple rows:\n{df2}\n")
df2 = pd.concat([df2, new_rows]) # concated those 2 data frame and voila we get 2 new rows in 1 operation
print(f"After adding 2 rows in one go:\n{df2}\n")


