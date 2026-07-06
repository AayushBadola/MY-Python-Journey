# data frames are a tabular data structure and we can store whatever we want (basically excel)
# data frame is made of rows and columns 
import pandas as pd

data = {
    "Name" : ["spongebob", "patrick", "squidward"],
    "age"  : [30,32,50]
}

######################## creating a data frame df #########################
df = pd.DataFrame(data,index=["Emp1", "Emp2", "Emp3"])

# df formed will be a matrix 

#            Name  age
# Emp1  spongebob   30
# Emp2    patrick   32
# Emp3  squidward   50

####################### ACESSING VALUES IN DATA FRAMES ###############
# we can access it similar to a series using loc OR iloc

print(f"Accessing employee 1:\n{df.loc['Emp1']}\n") # gives us the "ROW" EMP1

print(f"Entire data frame:\n{df}\n")

print("Now By doing iloc and doing values 0,1,2 we get values of row 1,2,3 respectively \n")
print(f"Specific value using row 1 to get same result as emp 1:\n{df.iloc[0]}\n")

################## ADDING NEW COLUMN TO DATA FRAME #######################
print(f"Before adding column :\n{df}\n")
df["job"] = ["cook", "N/A", "Cashier"] # same concept as dictionary just extended to data frame

print(f"After adding new column:\n{df}\n")
