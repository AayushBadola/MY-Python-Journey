#looping over a sequence 
print("Printing entire data: \n")
names = ["Dave", "Grey", "Sara", "Ash", "Pokemon"] #list
for name in names:
    print(name)

print("\n")

# stopping loop when reaching certain condition 
print("Stop when reach sara: \n")
for name in names:
    if name == "Sara":
        break

    else :
        print(name)

print("\n")
print("skipping sara: \n")
#skipping a certain part in data , using continue we skip that specific part / we allow the loop to continue
for name in names:
    if name == "Sara":
        continue
    else:
        print(name)

print("\n")
#loop for a range of number 
print("Loop values from 0->4: \n")
for value in range(5):# range from 0 -> 5, the upper end of range is NOT included, increment value by 1
      print(value)

print("\n")

#loop for a specific range of number , SAY from 2->5, the upper end of range is NOT included , increment value by 1
print("Loop values from 2->4: \n")
for value in range(2,5):
    print(value)
print("\n")

# loop for a specifc range of number and increment values by "n", so if 0->10 and increment 2 we get , 0,2,4,6,8
print("Loop for values from range 0->10 with increment \"2\" : \n")
for value in range(0,10,2): # range(start,stop,increment by)
    print(value)
print("\n")





