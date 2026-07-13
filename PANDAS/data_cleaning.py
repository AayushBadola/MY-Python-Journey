# data cleaning is a process of fixing the data or removing unwanted data 
# most of the work done by pandas is for data cleaning 

import pandas as pd

# IMPORTANT 
# for this chapter we will use the data.json file since its basically 
# json format -> data taken out by pandas -> data converted to data frame 
# the end data frame we work with same if we use data.csv or data.json

df = pd.read_json("data\data.json")
print(f"Result of Data frame created when importing data from JSON (same as CSV):\n{df}\n\n") 
# we will get the same result as we get in normal "data.csv"

###################### DROPPING / ERASING ALL VALUES IN A COLUMN ###############################

# if we drop legendary column we wont be able to distinguish weather the legendary == 1 or 0
# we are basically erasing the data of that column
df_dropped_Legendary = df.drop(columns="Legendary") # we have to specify we are dropping an entire column
print(f"Original dataframe :\n{df}\n\n")
print(f"Dataframe with legendary column DROPPED :\n{df_dropped_Legendary}\n\n")

print(f"By dropping the column the actual Dataframe (original) will not be changed" )
print(f"only a temporary \"VIEW\" will be created without the column LEGENDARY:\n{df}\n\n")

########################## DELEATING IRRELEVENT COLUMNS #############################

# in our data frame we have these columns and rows
''' 
      No        Name    Type1   Type2  Height  Weight  Legendary
0      1   Bulbasaur    Grass  Poison     0.7     6.9          0
1      2     Ivysaur    Grass  Poison     1.0    13.0          0
2      3    Venusaur    Grass  Poison     2.0   100.0          0
3      4  Charmander     Fire             0.6     8.5          0
4      5  Charmeleon     Fire             1.1    19.0          0
..   ...         ...      ...     ...     ...     ...        ...
145  146     Moltres     Fire  Flying     2.0    60.0          1
146  147     Dratini   Dragon             1.8     3.3          0
147  148   Dragonair   Dragon             4.0    16.5          0
148  149   Dragonite   Dragon  Flying     2.2   210.0          0
149  150      Mewtwo  Psychic             2.0   122.0          1
'''

# here we know that we dont need the column "No" and "Legendary" since the best info is height ,weight, types
# so we will select the columns we DONT want as a list ['Legendary','No']
# and we will pass this "list" into our df.drop() column 
unwanted_cols = ["Legendary","No"]
df_cleaner = df.drop(columns=unwanted_cols)

print(f"Data frame with irrelevent columns :\n{df}\n\n")
print(f"Data frame with only RELEVENT columns :\n{df_cleaner}\n\n")

####################### # HANDELLING MISSING VALS IN CERTAIN COLUMNS ##########################

# FOR say we only want to full values that is type 1 and type 2 and we dont want any row that is missing "Type2"
# we can remove the rows which dont have a value type2 or type2 is NULL 
'''
      No        Name    Type1   Type2  Height  Weight  Legendary
0      1   Bulbasaur    Grass  Poison     0.7     6.9          0
1      2     Ivysaur    Grass  Poison     1.0    13.0          0
2      3    Venusaur    Grass  Poison     2.0   100.0          0
3      4  Charmander     Fire             0.6     8.5          0
4      5  Charmeleon     Fire             1.1    19.0          0
..   ...         ...      ...     ...     ...     ...        ...
145  146     Moltres     Fire  Flying     2.0    60.0          1
146  147     Dratini   Dragon             1.8     3.3          0
147  148   Dragonair   Dragon             4.0    16.5          0
148  149   Dragonite   Dragon  Flying     2.2   210.0          0
149  150      Mewtwo  Psychic             2.0   122.0          1
'''
# in this data we can see veusaur charmander charmeleon have type2 missing or its NULL 
# so we dont want those pokemons 
# so we need to remove those specidic rows 
# to do so we use df.dropna() -> dropna mean DROP NULL or not appllicable rows 
# since the column in which NULL occurs we also have to specify it in form of subset = ["col1",col2 . . . .]

df_no_null_WRONG = df.dropna(subset=["Type2"]) # HERE it will not remove the rows since it remove rows with val NULL 
# OUR JSON DATASET CONTAINS EMPTY STRING that is "" IT IS NOT NULL !!
#  IMPORTANT :for this specific example we will use our csv data set

df_csv = pd.read_csv("data\data.csv")
df_no_null_CORRECT = df_csv.dropna(subset = ["Type2"])
print(f"Data frame which contains null values in type 2:\n{df}\n\n")
print("------------------------ DATA FRAME 1 AFTER DROPNA WORKING ON EMPTY STRING (NO CHANGE)---------------------------\n")
print(df_no_null_WRONG,"\n\n")
print("-------------------------DATA FRAME AFTER DROPNA WORKING ON ACTUAL NULL VALUES (NULL VAL ROWS REMOVED)----------------------------\n")
print(f"{df_no_null_CORRECT}")


################################ CHANING MISSING VALUES TO A STANDARD VALUE ##############################

# we know some values in col :Type2 are empty or are of empty string (the fucntion we are going to use replaces actual empty values not "" )
# to do that we need actual NULL values so we will again use our CSV DATASET

# to replace the null values we use df.fillna which MEANS FILL NULL 
# for this we pass a dictionary containing the column : "Default data"
# IMPORTANT : USE A "DICTIONARY" in for {"Type2" : "None"}
df_fill_null = df_csv.fillna({"Type2": "None"})
print(f"data frame with NULL values :\n{df_csv}\n\n ")
print(f"Changed null values to 'None' : \n{df_fill_null}\n\n")



################################### FIXING IN CONSISTANT VALUES #################################
# say for type1 that are MAIN ATTRIBUTES OF A GRASS POKEMON we want to show case those attributes in capital 
# for  EXAMPLE 
# we want 

'''
      No        Name    Type1   Type2  Height  Weight  Legendary
0      1   Bulbasaur    GRASS  Poison     0.7     6.9         0
1      2     Ivysaur    GRASS  Poison     1.0    13.0         0
2      3    Venusaur    GRASS  Poison     2.0   100.0         0
3      4  Charmander    Fire    None     0.6     8.5          0
4      5  Charmeleon    Fire    None     1.1    19.0          0

'''
# here we can DEFINETLY SEE THE MAIN ATTRIBUTE OF POKEMON 
# to do that we the function df["Col1"].replace({"Grass": GRASS}) we changed Grass -> GRASS
# we needto pass a DICTIONARY

df_grass_focused = df_csv["Type1"].replace({"Grass" : "GRASS"})

#   IMPORTANT SAY WE WANT THE ENTIRE TYPE1 TO BE CAPITAL TO SHOW THE MAIN ATTRIBUTE OF POKEMON 
# for that we jsut need to update the entire column 
# for that we jsut need df["col"] = Value we want to replace 

# df_type1_capital = df_csv["Type1"].upper() WONT WORK SINCE TYPE1 IS A SEIRES NOT A STRING SO CONVERT IT TO A STRING THEN UPPER 
df_type1_capital = df_csv["Type1"].str.upper() # now we have all the values in Type1 in string individually so now we can make them upper

print(f"Original Data frame is : \n{df_csv}\n\n")
print(f"Data frame with only TYPE1 having Grass values becoming CAPITAL :\n{df_grass_focused}\n\n")
print(f"Data frame with FOCUS ON TYPE1 vlaues and chaning all type1 to capital:\n{df_type1_capital}\n\n")


####################### we have another data set contaning duplicate values (BY DEFAULT) ########################
# BY DEAFULT IF WE CALL THE FUNCTION df.drop_duplicate() it automatically searches rows whose all values are same and deleates the other 

# if we have
'''  
       No        Name    Type1   Type2  Height  Weight  Legendary
0      1   Bulbasaur    Grass  Poison     0.7     6.9          0
1      2     Ivysaur    Grass  Poison     1.0    13.0          0
2      3    Venusaur    Grass  Poison     2.0   100.0          0
3      2     Ivysaur    Grass  Poison     1.0    13.0          0

'''

# then it will BY DEAFULT delete the 2nd one Ivysaur not the 1ST OCCURANCE !

# IF WE DO df.drop_duplicate(keep="first") it will keep the 1st occurance delete the later occurances 
# IF WE DO df.drop_duplicate(keep="last") it will delete the previous occurances and keep the last occurance 

df_contain_duplicate = pd.read_csv("data\data_with_duplicates.csv") # data containing some duplicate rows 

df_no_duplicate = df_contain_duplicate.drop_duplicates() # deletes the rows containing EXACT SAME VALUE AS SOME OTHER ROW 

print(f"Original Data frame containig the duplicate rows :\n{df_contain_duplicate}\n\n")
print(f"Data frame containing NO DUPLICATES :\n{df_no_duplicate}\n\n")
