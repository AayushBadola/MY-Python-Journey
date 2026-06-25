#function having access to the scope of its parent function 
# after the parent function has returned something 
# requires the nested funtions 

# in essance closure is when a nested function is able to change the values of parent function 
# AND parent function returns something (IN this case it returns the play_game)

def parent(person_name):
    coin = 3
    def play_game():
        nonlocal coin # now we are accessing the coin variable of parent function 
        coin = coin - 1 # if we play the game we use some coin so original gets subtracted 

        if (coin>1):
            print("\n " + person_name + str(coin) + " coins left")
        elif coin == 1:
            print("\n " + person_name + str(coin) + " coin left")
            
        else :
            print("\n" + person_name + "Has no coins left")
        
    return play_game


Dave = parent("Dave") # creates a specific person having those above attributes , has 3 coins
Tommy = parent("Tommy") # has 3 coins , they dont share the same ammount of coins 

# if dave plays 2 times he has 1 coin left 
# if tommy plays 1 times he has 2 coins, those 2 are independant 

Dave()
Dave()
Tommy()
    
