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
# to have multiple columns we have to pass a "list" contaning the column names 
# hence for any data frame we have to do 
#  df[    ["Col1", "col2", "col3" . . . .]   ]
print(f"SELECTING MULTIPLE COLUMNS FROM DATA FRAME:\n{df_csv[ ['Name', 'Weight', 'Height'] ]}\n")


############## SELECTING ALL DATA IN 1 ROW OF DATA FRAME #################

# we are basically printing one row with indx = 0
# for that we can use ".iloc" or if we have a label we can use ".loc"

print(f"Printing row 1 with all the data:\n{df_csv.iloc[0]}\n")

## IMPORTANT : we can also serve one of the column(unique) to serve as the index / label
#              for that we have to use or update the df_csv when we read the data to 
##################     df_csv = df.read_csv("filename", index_col= "Column name")  ###############


################## SELECTING SPECIFIC ROWS WITH SPECIFIC COLUMNS ######################

# from our previous chapter of selecting multiple columns we will use how we select multiple cols
# first in selecting specific row we select the row we want to select and pass the list with our cols
# so basically 
# df.iloc["row", ["col1","col2","col3" . . . ] ]
# IMPORTANT : WHEN SELECTING SPECIFIC ROW + SEPCIFIC COLS WE USE LOC SINCE ".iloc" need numeric arguments
print(f"Selecting row 1 with only 3 columns:\n{df_csv.loc[0, ['Name', 'Height', 'Weight']]}")

####################### SELECTING MULTIPLE ROWS ####################

# to select multiple rows we use the same technique in numpy arrays or any other 
# we simply to "start row:end row" END ROW IN NOT INCLUSIVE LIKE NUMPY 
# IMPORTANT : FOR THE NOT INCLUSIVE PART OF ("End row") THAT ONLY HAPPENS IN "iloc"
# for "loc" the (start) and (end) are inclusive

print(f"Selecting multiple rows with all cols:\n{df_csv.loc[0:5]}\n")


#################### SELECTING MULTIPLE ROWS WITH SPECIFIC COLUMNS ############

# to select multiple rows we use the above format but in loc since ".iloc" take numeric argument 
# to select multiple columns we again use the concept of "selecting multiple columns"
# we pass the columns we want in a list 

# so for cols we want we pass another argument to "loc" like this loc[row1:rown , ["col1","col2" . . .] ]

print(f"Selecting multiple rows and specific columns:\n{df_csv.loc[0:5, ['Name','Height','Weight'] ] }\n")

# IMPORTANT THE SAME CONCEPT OF STEP ALSO APPLIES 
# START:END : STEP 

############################## POKEDEX BASIC ###########################
'''
⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋

'''

df_csv = pd.read_csv("data\data.csv", index_col="Name") # now the label is by the name column
pokemon = input("Enter the Name of pokemon you want to search: ").capitalize()

try:
    print(df_csv.loc[pokemon])
except KeyError:
    print(f"Couldnt Find pokemon {pokemon}")

