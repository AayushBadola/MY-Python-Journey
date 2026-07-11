# aggregation is reduction of data or compression of data
# we use aggregation to create a summary of multiple data into one value 

# example we have data as {1,2,3,4,5,6} now we need the avg -> (1+2+3+4+5+6)/6 -> 3.5
# we need the max of data -> 6
# we need minimum of data -> 1
# we are getting one single value as the result thus giving us some sort of intuition about data 
# say from minimum and max we can know from which value data start and what value the data ends 
# and there are only values between 1->6

import pandas as pd

df = pd.read_csv("data\data.csv", index_col="Name")

print("--------------- LOADED ALL THE POKEMON FROM KANTO REGION---------------\n\n")

print("------------------ AGGREGATE FUNCTIONS WHICH USES ENTIRE DATAFRAME---------------\n\n")

################ FINDING MEAN PER COLUMN ##############
 # here since our data contians a mix of string and numeric 
 # we need to specify what mean of data we wan that is numeric_only = True

mean_numeric_data = (df.mean(numeric_only=True))
print(f"Mean of data with numeric columns :\n{mean_numeric_data}\n\n")

################ SUMMATION OF ALL DATA PER NUMERIC COL ###############

# here we will sum or add all the data per column
# so its like this 

# EXAMPLE :
# height weight legendary 
#   15     120     1 
#   19     93      0
#   5      56      1
# -------------------------
#   39     269     2

sum_numeric_data = (df.sum(numeric_only=True))
print(f"Summation of all the data per column :\n{sum_numeric_data}\n\n")
print("from this above data we know there are a total of 4 legendary in this dataset \n\n")

#################### MINIMUM VALUES IN EACH COL #############
min_numeric_data = (df.min(numeric_only=True))
print(f"Minimum value in each column containing numeric values: \n{min_numeric_data}\n\n")\

#################### MAX VALUES IN EACH COL ##################

# again same concept we can find minium values for only cols with numeric values
# hence we are stating numeric values = True since we only wants cols with numeric values 

max_numeric_data = (df.max(numeric_only=True))
print(f"Max vlaue in each column containing numeric values: \n{max_numeric_data}\n\n")

######################## COUNT TOTAL VALUES IN EACH COLUMN  ################

# IMPORTANT : FOR COUNTING WE DONT NEED ONLY NUMERIC VALUES IN PANDAS COUNTS ROW WISE 

count_vals = df.count()
print(f"Counting values per column , TYPE2 SOME VALS ARE NULL SO IT WILL BE LESS THAN 150 :\n{count_vals}\n\n")

################################# AGGREGATE FUNCTION PER COLUMN #################################

# in previous chapters we were doing aggregate function on the entire dataset hence we used to get all cols
# in this we will apply aggregate functions per column 

# to select a column we do df["Column Name"].Aggregatefunction()

# SAME AS AGGREGATE FUNCTIONS WORKING FOR WHOLE DATAFRAME BUT INSTEAD OF df WE USE df["column Name"]

print("---------------------- GROUPING DATA BASED ON values or conditions ---------------------------")

######################### GROUPING DATA BASED ON COLUMNS #######################
# for any data we can group it based on certain factors 

# say we want to know the mean of column weight but also we want it structured so that its mean per type1
# we we would need this type of data 
# type1        mean weight 
# poison         40
# flying         80
# fire           75

# and so on 
# for that we need to use "groupby("Column Name")" condition 

group_type1 = df.groupby("Type1") # the data in which we want to group them / seprate them (based on their type1)
mean_weight_per_type1 = group_type1["Weight"].mean()
print(f"Mean Weight per Type1 Affinity Pokemon:\n{mean_weight_per_type1}\n\n")

group_legendary = df.groupby("Legendary") # data sepration based on pokemon which are legendary and which are not
mean_height_legendary = group_legendary["Height"].mean()

print(f"Mean Height of Legendary and non Legendary :\n{mean_height_legendary}\n\n")







