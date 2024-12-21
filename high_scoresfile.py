# this file will work with a text file named "highscore.txt"it will be used to 
# track and save the ammount of chips each player has and use it to create
# a list of top chip amounts, serving as a highscore board

highscorefile = "highscore.txt"

# this code will create a new variable that reads a highscore to players after
# they quit the game or run out of chips
# this will use a dictionary to track a players chips, wins, losses, ties
def highscorereading():
    highscores = {}
    try:
        with open(highscorefile, "r") as file: # this uses "r" as a read only file
            for line in file:
                if ':' in line:
                    player, score = line.strip().split(":") 
                    highscores[player] = int(score)
    except FileNotFoundError:
        pass
    return highscores # this will return the highscore values

def writehighscores(highscores): # this will store the players name next to their highscore 
    # in a dictionary and write to said text file
    with open(highscorefile, "w") as file:
        for player, score in highscores.items():
            file.write(f"{player}:{score}\n") # this is the line responsible for writing the highscores to
            # the text file "highscores.txt"

def updatehighscore(playername,score): #this section of code is responsible for comparing
    # the score of a player to the highscore and determining if the list of highscores should be updated (written to)
    highscores = highscorereading()
    if playername not in highscores or score > highscores[playername]:
        highscores[playername] = score
        writehighscores(highscores) #this will write the new highscore to the text file
        return True
    return False