"""
    Definition: gets an input of rock, paper, or scissors
    Author: Emmie Kao
    Date: Fall 2021
"""
import random

def getNameAndNumGames():
    """
        Inputs: None
        Outputs: String of user's name
                 Int number of wins the user wants to play until
        Purpose: Gets the inputs needed to start the program (name, # wins),
                 prints an encouraging message
    """
    name = input("What is your name? ")
    acceptableInt = False
    while not acceptableInt:
        try:
            numGames = int(input("How many wins should we play until? "))
        except ValueError:
            #if the input is not an integer, the program won't run
            print("Please enter an integer!")
        else:
            #if the input is less than 0, the program won't run
            if numGames <= 0:
                print("Please enter a POSITIVE integer!")
            elif numGames > 0:
                acceptableInt = True

    print(f"Let’s see who can win {numGames} games first! Good luck.")
    return (name, numGames)

def getChoice():
    """
        Inputs: None
        Outputs: String choice "rock", "paper", or "scissors"
        Purpose: gets an input to use in the game
    """
    print("Next round: ")
    acceptableInput = False
    while not acceptableInput:
        chosenMove = input("Pick one of rock, paper, or scissors: ")
        #Input MUST be rock, paper, or scissors, or else the program won't run.
        if chosenMove.lower() == "rock":
            acceptableInput = True
        elif chosenMove.lower() == "paper":
            acceptableInput = True
        elif chosenMove.lower() == "scissors":
            acceptableInput = True
        else:
            print(f"Whoops! {chosenMove} isn't a valid choice. Try \
again.")
    return chosenMove.lower()

def getComputerMove():
    """
        Inputs: None
        Outputs: The computer's move in the game
        Purpose: To generate a random move for the computer to make
    """
    compMove = random.randrange(0,3)
    if compMove == 0:
        return ("rock")
    elif compMove == 1:
        return ("paper")
    elif compMove == 2:
        return ("scissors")

def calculateWinner(playerOneChoice, playerTwoChoice):
    """
        Inputs: a move from Player 1 and a move from Player 2
        Outputs: an integer representing the winner of the game
        Purpose: to calculate the winner of the game
    """
    if playerOneChoice == "rock" and playerTwoChoice == "scissors":
        return(1)
    elif playerOneChoice == "rock" and playerTwoChoice == "paper":
        return (2)
    elif playerOneChoice == "rock" and playerTwoChoice == "rock":
        return (0)
    elif playerOneChoice == "paper" and playerTwoChoice == "rock":
        return (1)
    elif playerOneChoice == "paper" and playerTwoChoice == "scissors":
        return (2)
    elif playerOneChoice == "paper" and playerTwoChoice == "paper":
        return(0)
    elif playerOneChoice == "scissors" and playerTwoChoice == "paper":
        return (1)
    elif  playerOneChoice == "scissors" and playerTwoChoice == "rock":
        return (2)
    elif playerOneChoice == "scissors" and playerTwoChoice == "scissors":
        return (0)

def printWins(playerName, playerWins, computerWins):
    """
        Inputs: Two integers, one for the player's wins and one for the
        computer's wins
                One string forthe user's name
        Outpust: None, but prints out the current scoreboard
        Purpose: To tell the user the current scores
    """
    print(f"{33*'-'}")
    print(f"{playerName}: {playerWins}  Computer: {computerWins}")
    print(f"{33*'-'}")

def main():
    userName, numWins = getNameAndNumGames()
    userWins = 0
    compWins = 0
    numPlayed = 0

    while userWins < numWins and compWins < numWins:
        print("")
        userChoice = getChoice()
        compChoice = getComputerMove()
        print(f"{userName} picks {userChoice} and Computer picks {compChoice}.")
        #print out the winner
        if calculateWinner(userChoice, compChoice) == 1:
            print(f"...{userName} wins!")
            userWins += 1
        elif calculateWinner(userChoice, compChoice) == 2:
            print("...Computer wins!")
            compWins += 1
        elif calculateWinner(userChoice, compChoice) == 0:
            print ("...A tie.")
        printWins(userName, userWins, compWins)
        numPlayed += 1
    print("")
    if userWins > compWins:
        print(f"{userName} beat Computer:")
        print(f"...won {numWins} in {numPlayed} rounds of rock-paper-scissors.")
    else:
        print(f"Computer beat {userName}:")
        print(f"...won {numWins} in {numPlayed} rounds of rock-paper-scissors.")
    print("")
main()
