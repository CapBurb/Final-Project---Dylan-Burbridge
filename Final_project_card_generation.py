
# this file is the "Deck Creation file" it is responsible for creating a deck of 52 cards to mimic that of the decks used in blackjack.

# this section of code creates two variables, the cardsuits which coorespond to the four suits of a deck
# and the cardvalues from one to ten as well as four face cards 
cardsuits = ['Diamonds', 'Hearts','Clubs','Spades']
cardvalues = [ 'One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']



# this line pairs the cardsuits to the cardvalues to create four sets of 14 unique cards for a deck total of 52 cards (no jokers)
createdeck = [f"{value} of {suit}" for suit in cardsuits for value in cardvalues]

