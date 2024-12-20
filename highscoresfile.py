# this file will work with a text file named "highscore.txt"it will be used to 
# track and save the ammount of chips each player has and use it to create
# a list of top chip amounts, serving as a highscore board

highscorefile = "highscores.txt"

# this code will create a new variable that reads a highscore to players after
# they quit the game or run out of chips
# this will use a dictionarie to track a players chips, wins, losses, ties
def highscorereading():
    highscores = {}
    