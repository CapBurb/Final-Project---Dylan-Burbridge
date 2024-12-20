# This is the main file in which the player will interact with the computer in a player vs. house (computer) game of blackjack
# The player will compete to get the highest amount of "Chips" which is a currency they can bet with
# To motivate the player, the goal of this game is to get the highest amount of "Chips" this will be the players highscore
# The game will end once the player runs out of "Chips"

import random

# These call up seperate files for the value of a players hand and
# The creation of a deck of cards and the highscore counter
from Card_value_file import playerhandvalue
from high_scoresfile import readhighscores, updatehighscores
from Final_project_card_generation import createdeck



# This will represent a player being dealt a card from the deck
def dealcard(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# This starts the round of blackjack, Dealing two cards to both the player and 
# "house" (The computer) 
def gameround(deck, chips):
    playershand = [dealcard(deck),dealcard(deck)]
    houseshand = [dealcard(deck),dealcard(deck)]


# This statement will take the random dealt cards from gameround and playershand and houses hand
# and then convert them into values that the program can understand
# The variable "playerhandvalue" could be renamed for clarity, however it remains as an artifact of previous coding ideas
    playersvalue = playerhandvalue(playershand)
    housesvalue = playerhandvalue(houseshand)

    print(f"\n Your hand is: \n {playershand}. \n The value of your hand is: {playersvalue}")
    print(f"\n Houses hand is: \n ['{houseshand[0]}'],[Unknown card].")


    #the two lines below will immediately determine if the play wins or looses based on the slim chance
    # that a player immediately gets a value of 21 or higher
    if playersvalue == 21: 
        print ("\nWinner!, You've got Blackjack!")
        chips += 100
        return chips

    elif playersvalue > 21:
        print ("\nBust, You've lost!")
        chips -= 75
        return chips

    else:
        while playersvalue < 21:
            playermove = input("\n Choose to Stand or Hit. Please type 'hit' or 'stand': ") .strip().lower() # Added strip and lower values to prevent a misinput 
            #if player capitalizes or adds a space in their answer
            if playermove == "hit": #This will randomly select a new card from the deck and give it to the player
                playershand.append(dealcard(deck))
                playersvalue = playerhandvalue(playershand) # this line will update the value of the players hand if they take a new card or "hit"
                print(f"\nYour hand is now: {playershand} \nThe value of your hand is now: {playersvalue}")

                if playersvalue == 21: 
                    print ("\nWinner, You've got Blackjack!")
                    chips += 100
                    return chips
                    
                elif playersvalue > 21:
                    print ("\nBust, You've lost!")
                    chips -= 75
                    return chips

            elif playermove == "stand":
                break
            #this line below ensures player only types either "Hit" or "Stand"
            #as these are the only acceptable inputs, nothing will happen if either is not inputed
            else:
                print("\nNo input detected, please only print 'Hit' or 'Stand'")


        print(f"\n The Houses hand is now: {houseshand} \nThe value of the Houses hand is: {housesvalue}")


        # This is a result of researching casinos, to simpify for a simple card game if the house (computer)
        # has a hand with a value less than 16, it will deal itself another card. This logic follows the policy
        # of most casinos which often train dealers to hit on either 16 or 17
        while housesvalue < 16: 
            houseshand.append(dealcard(deck))
            housesvalue = playerhandvalue(houseshand)
            print(f"\n The Houses hand is now : {houseshand}, \nThe value of the Houses hand is: {housesvalue}")

# This will compare the scores of the final game and show if the house won, tied or lost
        print(f"\nGame results:\n \nYour hand is: {playershand} \nThe value of your hand is: {playersvalue}")
        print(f"\nThe Houses hand is: {houseshand} \nThe value of the Houses hand is: {housesvalue}")           


#these lines compare the value of the players total cards vs the value of the houses total cards
# it also will print to show the players if they win tie or lose
    if housesvalue > 21 or playersvalue > housesvalue:
        print("\nYou've won this round!")
        chips += 100 
        return chips           
    elif playersvalue == housesvalue:
        print("\nIt's a tie, push to next round.")
    else:
        print("\nThe house always wins. \n Better luck next round.") # Hidden game reference here
        chips -= 75
        return chips
    

    

if __name__ == "__main__":

    print("|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
    print("♣-♦-♥-♠- Welcome to Python BlackJack -♠-♥-♦-♣")
    print("|-------------------------------------------|")

    print("\nYou will start with 200 chips. \n If you win a round you will gain 100 chips. \n If you lose a round you will lose 75 chips.")
    
    chips = 200 
    # This is the starting chip variable, which will update based on the game rules above

    while chips > 0:
        print(f"\n You have: {chips} chips left.")
        userplay = input("\nWould you like to begin a round? (Yes/No): ") .strip().lower() # To allow users to choose if they want to start a game or not
        if userplay == "yes":
            deck = createdeck[:] # for the clarity of the code, the deck and "createdeck" functions are seperated
            random.shuffle(deck) # This with "shuffle" the deck to ensure cards are not repeated
            chips = gameround(deck,chips)
        elif userplay == "no":
            print("\nSmart, Gambling is bad for you.") # Life advice
            break # If the player types "no" a break is used to end the game
        else:
            print("\nPlease type 'yes' or 'no'.") # to ensure that only the required input is accepted

    if chips < 0:
        print("\n You are all out of chips. Game over and better luck next time!")
