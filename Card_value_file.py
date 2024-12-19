# This line brings in a random value, needed for a "Shuffled" deck to be used
import random

# This code turns the text value of cards into the values they respresent in blackjack, where cards are valued at 1-10, face cards at 10 and aces high at 11
def playerhandvalue(playerhand): 
    cardvalues = {
        'One' : 1, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10, 'Ace' : 11 }

# While the ace value is determined to be worth 11, the game of Blackjack dictates that the value of aces are either 1 or 10 depending on the hand of the player
# The code below will determine the value of an ace based on the value of a players hand (above or below 21)

value = sum(cardvalues[card.split(' ')[0]] for card in playerhand)

aces = sum(1 for card in playerhand if card.startswith('Ace'))

while value > 21 and aces > 0:
    value -= 10
    aces -= 1

return value 