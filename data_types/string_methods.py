first = "dave "
last = "grey"

#change value to all lower
print(first.lower())

#cahnge value to all upper
print(first.upper())

#find length of string, len also counts the spaces inside strings, 1 tab is 4 spaces
print(len(first))

#start is upper others are lower
print(first.title())

# replaces the specific word in the variable first with aayush 
print(first.replace("dave ", "aayush"))

# removes all the white spaces and the inbetween as well say aayush badola -> aayushbadola
print(first.strip)

#removes all white space form left side
print(first.lstrip)

#removes all white spaces fomr right side
print(first.rstrip())

# centers the string using the given figuer 
print( "hello".center(20,"#"))



# last value of string 
print(last[-1]) # last variable is last = "grey" so lsat value = y

# first value of string 
print(last[0]) # last variable is last = "grey" so first value = g