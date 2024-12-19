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


# This statement will take the random dealt cards from gameround and playershand and houses hand
# and then convert them into values that the program can understand
# The variable "playerhandvalue" could be renamed for clarity, however it remains as an artifact of previous coding ideas
    playersvalue = playerhandvalue(playershand)
    housesvalue = playerhandvalue(houseshand)

    print(f"\n Your hand is : {playershand}. \n The value of your hand is: {playersvalue}")
    print(f"\n Houses hand is: {houseshand[0]}. \n The value of the houses hand is: {housesvalue}")


    #the two lines below will immediately determine if the play wins or looses based on the slim chance
    # that a player immediately gets a value of 21 or higher
    if playersvalue == 21: 
        print ("Winner!, You've got Blackjack")

    elif playersvalue > 21:
        print ("Bust, You've lost!")

    else:
        while playersvalue < 21:
            playermove = input("Choose to Stand or Hit. Please type 'hit' or 'stand': ") .strip().lower() # Added strip and lower values to prevent a misinput 
            #if player capitalizes or adds a space in their answer
            if playermove == "hit": #This will randomly select a new card from the deck and give it to the player
                playershand.append(dealcard(deck))
                playersvalue = playerhandvalue(playershand) # this line will update the value of the players hand if they take a new card or "hit"
                print(f"Your hand is now: {playershand} (Your value is now: {playersvalue})")

                if playersvalue == 21: 
                    print ("Winner, You've got Blackjack")
                    
                elif playersvalue > 21:
                    print ("Bust, You've lost!")

            elif playermove == "stand":
                break
            #this line below ensures player only types either "Hit" or "Stand"
            #as these are the only acceptable inputs, nothing will happen if either is not inputed
            else:
                print("No imput detected, please only print 'Hit' or 'Stand'")


        print(f"\n houses hand is: {houseshand}")


        # This is a result of researching casinos, to simpify for a simple card game if the house (computer)
        # has a hand with a value less than 16, it will deal itself another card. This logic follows the policy
        # of most casinos which often train dealers to hit on either 16 or 17
        while housesvalue < 16: 
            houseshand.append(dealcard(deck))
            housesvalue = playerhandvalue(houseshand)
            print(f"house takes a card: {houseshand[-1]} (houses value is: {housesvalue})")


                
                

    


if __name__ == "__main__":

    deck = createdeck[:] # for the clarity of the code, the deck and "createdeck" functions are seperated
    random.shuffle(deck) # This with "shuffle" the deck to ensure cards are not repeated

gameround(deck)