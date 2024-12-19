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

if __name__ == "__main__":
    deck = createdeck[:]
    random.shuffle(deck) # This with "shuffle" the deck to ensure cards are not repeated

gameround(deck)