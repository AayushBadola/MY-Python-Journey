import pandas as pd

df = pd.read_csv("data\data.csv")

######## KEEPING THE ROWS THAT MATCH A CONDITION #########
# for this case lets say pokemon whose height >2

tall_pokemon = df[df["Height"] > 2]
print(tall_pokemon)
# df["Height"] returns the Height column (a Series)
# df["Height"] > 2 compares every value with 2 and returns
# a Series of True/False values.
# Passing that Series inside df[...] keeps only the rows
# where the condition is True.

# Hence:
# df[df["Height"] > 2]
