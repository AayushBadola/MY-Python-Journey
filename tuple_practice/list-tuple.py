# List containing tuples
# List = mutable (can change)
# Tuple = immutable (cannot change)

# here data is list but the values that is the () inside the list are tuple 
# we can create or remove the ENTIRE tuple that is (name,aayush) or add ("section", "A")
#WE can NOT remove "Aayush" since its part of tuple 
# so WE CAN NOT MODIFY A "PART" OF A TUPLE 
data = [
    ("name", "Aayush"), 
    ("age", 20)
]


print("Original List:")
print(data)

# Add a new tuple
# Allowed because we are modifying the list

data.append(("city", "Delhi"))

print("\nAfter Adding Tuple:")
print(data)

# Remove an entire tuple
# Allowed because we are modifying the list

del data[1]

print("\nAfter Removing Tuple:")
print(data)

# Replace an entire tuple
# Allowed because we are replacing a list element

data[0] = ("name", "Rahul")

print("\nAfter Replacing Tuple:")
print(data)

# NOT Allowed
# Tuples are immutable

# data[0][1] = "Rohan"

# Error:
# 'tuple' object does not support item assignment