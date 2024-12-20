# this file will work with a text file named "highscore.txt"it will be used to 
# track and save the ammount of chips each player has and use it to create
# a list of top chip amounts, serving as a highscore board

highscorefile = "highscores.txt"

# this code will create a new variable that reads a highscore to players after
# they quit the game or run out of chips
# this will use a dictionary to track a players chips, wins, losses, ties
def highscorereading():
    highscores = {}
    try:
        with open(highscorefile, "r") as file:
            for line in file:
                if ':' in line:
                    player, score = line.strip().split(":")
                    highscore[player] = int(score)
    except FileNotFoundError:
        pass
    return highscores