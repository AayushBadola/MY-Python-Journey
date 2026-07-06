# pandas is used for data cleaning and manipulation unlike numpy which mostly focus on arrays 
# allows us to work with structured data like csv files 
import pandas as pd #<-- most comoon "nickname"

# a series is a single array (1-D) which can hold int,string,float ANYTHING and MIXED !! 
# we can create a series by calling a constructor that is "pd.Series(data)"

data = [101,102,104]

series = pd.Series(data)
print(series)
print(type(series))

print("Here the index is 0, 1, 2 \n") # we can change the indexwhich we see in terminal 
                                   # we can make it such that its a,b,c OR something in that sense 
                                   # this "index" in series is called a label

series_new_label  = pd.Series(data, index=["a","b", "c"]) # now index is a,b,c 
print(f"New series with new index : \n{series_new_label} \n")

# we can make bigger strings be index of the series # so we can make those 101,102,104 be apartments

series_bigger_label = pd.Series(data, index=["Apartment 1", "Apartment 2", "Apartment 3"])
print(f"Series with new bigger label is : \n {series_bigger_label} \n")

######### ACCESSING VALUES IN SERIES #############
# values in series are accessed by using the value that "label" holds
# for that we CAN USE series_name[label value or name]
# we use series_name.loc[label value or name] <-- more structured 

print(f"Locating specific value in aprtment 1: {series_bigger_label.loc['Apartment 1']} \n")
print(f"Similarly value / room number fo apartment 3 : {series_bigger_label.loc['Apartment 3']}\n ")
# INSIDE F STRING NEVER USE DOUBLE QUOTES SINCE IT THINKS ITS PART OF IT AND HENCE IT ENDS 
# PREMATURELY 

# we can also use normal indexing that is 0,1,2,3,4,5 . . . . 
# we can use normal indexing using .iloc[index number]

############# UPDATING VALUES IN SERIES ############
# TO update the value inside series we use the same concept as in arrays or numpy arrays or lists

# we do arr[index] = new values

source = [100,101,103,104,105]
original_series = pd.Series(source, index=["label1", "label2", "label3", "label4", "label5"])

# now we can update it in 2 ways 
# 1 -> we can do direct indexing or label , series[label], series[index = 0,1,2,3,4 . . . .]
# 2 -> we can do using iloc and loc -> series.loc["label"] OR series.iloc[ACTUAL INDEX]

# FOR STRUCTURED APPROACH WE WILL USE THE DEDICATED FUNCTIONS

print(f"Original series is given as :\n{original_series}\n")
# updating the original series 
print("changing value 105 ->  106")
original_series.loc["label5"] = 106 # updated the value the lbel5 holds
print(f"Changed the series using \" .loc\" function :\n{original_series}\n")

print("changing the value 104 -> 105 using \".iloc \" number based indexing \n")
print(f"Original series :\n {original_series}\n")
original_series.iloc[3] = 105 # as in updated series [100,101,102,103,104,106] 104 is at index 3
print(f"Updated series using \" .iloc\" changed 104-> 105:\n{original_series}\n")
 

########## FILTER IN SERIES ##########
# filter concept is similar or same as that in numpy 
# we can do series_name[series_name <some condition>]
# now copy of series will be made containing only the values which satisfy that <condition>

data_source = [1,2,3,4,5,6]
num_series = pd.Series(data_source, index=["val1", "val2", "val3","val4","val5","val6"]) # created a series of the data_source 

even_nums = num_series[ num_series %2 == 0] # added a condition for even numbers

print(f"Original series:\n{num_series}\n")
print(f"Series containing only even numbers of original series:\n{even_nums}\n")


######### PASSING DICTIONARY TO SERIES #########
# we know a dictionary contains key->value pairs 
# so we dont really have a need to add index specifically 
# the index label is basically the originally created key in the dictionary 

calories ={
    "day 1" : 1750,
    "day 2" : 2140,
    "day 3" : 2000
}

# day number is the keys and int are the values

# converting it to a series 
calories_series = pd.Series(calories) # no need for index labelling
## now we can access it using the keys that is series,loc[keys] or series[label]

print(f"Using key day 2 to print the calories: {calories_series.loc['day 2']}")
# similarly we can use updation 



