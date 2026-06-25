from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

# prints value which relates to 2 
print(RPS(2))

# just prints the term RPS.PAPER
print(RPS.PAPER)

# PRINTS RPS.PAPER
print(RPS['PAPER'])

# PRINTS THE VALUE COREELATING TO RPS.PAPER 
print(RPS.PAPER.value)

# to remove the term RPS. usign 2 methods
print(str(RPS(2)).replace("RPS.", ""))

print(RPS(2).name)


