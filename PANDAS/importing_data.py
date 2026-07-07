# IF we already have a structured csv data then we can import / use that data and do the operations on it 
# for importing data we can 
# 1. have the actual data in our working directory 
# 2. we can have the actual "full" address of the data
# WE CAN ALSO USE JSON DATA IF WE WANT TO 

import pandas as pd

######### READING A CSV FILE #############
# to read a csv we need to use "read_csv()" function
df_csv = pd.read_csv("data\data.csv") # we care reading our data which is in our working direcotry 
                             # if we dont have it there we need to provide the entire path to it 

# now we have basically "stored" the entire values in our df variable or data frame
# IMPORTANT : if we print the "df" as is then we will get first 5 row and last 5 
# if we want to print the entire rows we need to use to "to_string" function 

# print first 5 last 5 rows we just need to do print(df)
# to print entire thing we need print(df.to_string())

########### READING A JSON FILE ##########
df_json = pd.read_json("data\data.json")

########### SELECTING ALL DATA IN COLUMN #############
print(df_csv["Name"])
print("\n\n\n")
 # prints the entire data in the column "Name"
# TO PRINT ENTIRE THING WE WILL DO df_csv["Name"].to_string() that will print out the entire column 
print(f"selecting the weight of the pokemon :\n{df_csv['Weight']}\n ")


############# SELECTING MULTIPLE COLUMNS AT ONCE #################
