# This is the main file in which the player will interact with the computer in a player vs. house (computer) game of blackjack
# The player will compete to get the highest amount of "Chips" which is a currency they can bet with
# To motivate the player, the goal of this game is to get the highest amount of "Chips" this will be the players highscore
# The game will end once the player runs out of "Chips"

print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
print("♣-♦-♥-♠- Welcome to Python BlackJack -♠-♥-♦-♣")
print("|-------------------------------------------|")

import random

# These call up seperate files for the value of a players hand and
# The creation of a deck of cards
from Card_value_file import playerhandvalue
from Final_project_card_generation import createdeck

# This will represent a player being dealt a card from the deck
def dealcard(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# This starts the round of blackjack, Dealing two cards to both the player and 
# "house" (The computer) 
def gameround(deck):
    playershand = [dealcard(deck),dealcard(deck)]
    houseshand = [dealcard(deck),dealcard(deck)]

# This print statement will show the player the value of their two cars
    print(f"\nyour hand is : {playershand}")
    print(f"houses hand is: {houseshand[0]}")

# This statement will take the random dealt cards from gameround and playershand and houses hand
# and then convert them into values that the program can understand
# The variable "playerhandvalue" could be renamed for clarity, however it remains as an artifact of previous coding ideas
    playersvalue = playerhandvalue(playershand)
    housesvalue = playerhandvalue(houseshand)

    #the two lines below will immediately determine if the play wins or looses based on the slim chance
    # that a player immediately gets a value of 21 or higher
    if playersvalue == 21: 
        print ("Winner, Blackjack")

    elif playersvalue > 21:
        print ("You lose, bust")

    else:
        while playersvalue < 21:
            playermove = input("stand or hit")
            if move == "hit": #This will randomly select a new card from the deck and give it to the player
                playershand.append(dealcard(deck))
                print(f" your hand is now: {playershand}")

                if playersvalue == 21: 
                    print ("Winner, Blackjack")
                    
                elif playersvalue > 21:
                    print (You lose, bust)

            elif move == "stand":
                break
            else:
                print("No imput detected, please only print 'Hit' or 'Stand"")
                

                
                

    


if __name__ == "__main__":

    deck = createdeck[:] # for the clarity of the code, the deck and "createdeck" functions are seperated
    random.shuffle(deck) # This with "shuffle" the deck to ensure cards are not repeated

gameround(deck)