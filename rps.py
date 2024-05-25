from random import randrange


def showScoreboard():
    print("")
    print(f"Game: {gameScore} | User: {userScore}")
    print("")

def addHistory(userChoice, gameChoice, winner):
    result = ["user", userChoice, "game", gameChoice, winner]
    history.append(result)
    
def showHistory():
    for item in history:
        print("".join(item).format(":<20"))
        
def showTotalPlays():
    print(f"Total Plays: {totalPlays}")
    print("")
    
def showEndOfGame():
    print("")
    showScoreboard()
    showTotalPlays()
    showHistory()
    print("")
    print("Game Over!")
    print("")
    
rock = "🗿"
paper = "📄"
scissors = "✂️"
history = []

userScore = 0
gameScore = 0
totalPlays = 0


choices = ["rock", "paper", "scissors"]

playAgain = True

while playAgain:


    showScoreboard()

    userChoice = input(f"rock {rock}, paper {paper}, scissors? {scissors} ")

    if userChoice in choices:

        playAgain = True
        totalPlays += 1

        gameChoice = choices[randrange(2)]

        # three outcomes that result in a draw
        if gameChoice == userChoice:
            print("both players have chosen", gameChoice, "...DRAW!")
            addHistory(userChoice, gameChoice, "none")

        # six outcomes that result in a winner
        elif gameChoice == "rock" and userChoice == "paper":
            msg = f"{paper} covers {rock} .. User Win!"
            addHistory(userChoice, gameChoice, "user")
            userScore += 1
            print(msg)

        elif gameChoice == "rock" and userChoice == "scissors":
            msg = f"{rock} dulls {scissors} ... Game Wins!"
            addHistory(userChoice, gameChoice, "game")
            gameScore += 1
            print(msg)

        elif gameChoice == "paper" and userChoice == "rock":
            msg = f"{paper} covers {rock} ... Game Wins!"
            addHistory(userChoice, gameChoice, "game")
            gameScore += 1
            print(msg)

        elif gameChoice == "paper" and userChoice == "scissors":
            msg = f"{scissors} cut {paper} ... User Wins!"
            addHistory(userChoice, gameChoice, "user")
            userScore += 1 
            print(msg)

        elif gameChoice == "scissors" and userChoice == "rock":
            msg = f"{rock} dulls {scissors} ... User Wins!"
            addHistory(userChoice, gameChoice, "game")
            userScore += 1
            print(msg)
            
        elif gameChoice == "scissors" and userChoice == "paper":
            msg = f"{scissors} cut {paper} ... Game Wins!"
            addHistory(userChoice, gameChoice, "game")
            gameScore += 1
            print(msg)

        else:
            print("invalid data!")
else:
    playAgain = False


showEndOfGame()
