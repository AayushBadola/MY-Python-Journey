import random

print(" ")
userinput = int(input("Enter... \n 1 for rock \n 2 for paper \n 3 for scissor \n \n"))

while (userinput <1 or userinput > 3) :
    print("Please enter the given values \n \n")
    userinput = int(input("Enter... \n 1 for rock \n 2 for paper \n 3 for scissor \n \n"))

computerchoise = random.randint(1,3)

if userinput == computerchoise and userinput == 1:
    print("I choose rock\n its a tie")

elif userinput == computerchoise and userinput == 2:
    print("I choose paper\n its a tie")

elif userinput == computerchoise and userinput == 3:
    print("i choose scissor \n its a tie")



if userinput == 1 and computerchoise == 2:
    print("I choose paper \n I win")

elif userinput == 1 and computerchoise == 3:
    print("I choose scissor \n you win")

elif userinput == 2 and computerchoise == 1:
    print("I choose rock \n you win")

elif userinput == 2 and computerchoise == 3:
    print("I choose scissor \n I win")

elif userinput == 3 and computerchoise == 1:
    print("I choose rock \n I win")

elif userinput == 3 and computerchoise == 2:
    print("I choose paper \n you win")



