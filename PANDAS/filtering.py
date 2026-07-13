import pandas as pd

df = pd.read_csv("data\data.csv")

######## KEEPING THE ROWS THAT MATCH A CONDITION #########
# for this case lets say pokemon whose height >2

tall_pokemon = df[df["Height"] > 2]
print(tall_pokemon,"\n\n")
# df["Height"] returns the Height column (a Series)
# df["Height"] > 2 compares every value with 2 and returns
# a Series of True/False values.
# Passing that Series inside df[...] keeps only the rows
# where the condition is True.

# Hence:
# df[df["Height"] > 2]

##### similarly for heavy pokemon we can say pokemon who are more than 100kg
# since all our data is in kg we only have to put the numeric value as 100
# so by the above format we need to "Select all rows with col= 'Weight' " 
# after selection we need those which are >100 so df["Wight"] > 100
# now we put this "Value condition of rows in data frame" 
# hence we get 
# df[ df["Weight"]>100 ]

chunky_pokemon = df[ df["Weight"] > 100 ]
print(f"Pokemon whose weight is greater than 100kg:\n{chunky_pokemon}\n\n")

#### EXAMPLE 2 
# using the above format we will  select "Legendary" pokemon 
# lets say since they are legendary we want to "Hide" some of their column info
# hence we will select a condition for column that is "Legendary" == 1
# AND we will select only certain column like "Name", "Type1","Type2"

# same with above format for legendary status we need all row containing legendary col
# hence df["Legendary"]
# now we got the data of it we now compare it to 1
# df["Legendary"] == 1
# now we got the rows which contain legendary pokemon to access those we feed it to dataframe
# df[ df["Legendary"] == 1]

# now we need specific columns so we do df[row, ['col1', 'col2, 'col3' . . . .] ]

legendary_pokemon = df.loc[ df["Legendary"] == 1, ["Name","Type1","Type2"] ]

print(f"Legendary Pokemon are:\n{legendary_pokemon}\n\n")

######## comparing col data with strings #############

#in previous examples we are only comparing integer values so now we will do filtering based on string values
# lets day we need pokemon who can do water type attacks mainly 
# so their type 1 becomes "Water"
water_type_pokemon = df[ df["Type1"] == "Water" ]
print(f"Pokemon with main affinity of WATER:\n{water_type_pokemon}\n\n")

##### EXAMPLE 2 
# similary if we want pokemon which are fire + flying type 
# we would need the condition (Type1 == "Fire") and (type2 == "Flying")

fire_flying_pokemon = df [ (df["Type1"] == "Fire") & (df["Type2"] == "Flying") ]
# WHY USE & INSTEAD OF "and"?
# 1. "and" checks the whole column at once, gets confused by a list of rows, and crashes.
# 2. "&" checks row-by-row (element-wise), matching each individual row together.
# 3. Always wrap conditions in () when using & so Pandas knows where each check starts and ends.


print(f"Pokemon with fire + flying affinity:\n{fire_flying_pokemon}\n\n")

# IMORTANT : WE CAN SIMILARLY DO THAT FOR or operator ("|" <- this one)



