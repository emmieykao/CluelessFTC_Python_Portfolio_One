import random

def main():
    entryList = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    playerLetter = getPlayerLetter()
    goesFirst = whoGoesFirst()
    print(f"Player 1 will be {playerLetter}'s.")
    print(f"{goesFirst}'s will go first.")
    if playerLetter == "X":
        cpuLetter = "O"
    else:
        cpuLetter = "X"
    if playerLetter != goesFirst:
        makeMove(entryList, cpuLetter, 0)
    while isBoardFull(entryList) == False:
        makeMove(entryList, playerLetter, getPlayerMove(entryList))
        print("")
        entryList[chooseRandomMove(entryList)] = cpuLetter
        draw(entryList)

def draw(board):
    """
    Input: board, a list of 9 elements.  Each element is a string with only one
    character. " "=empty, "O"=Player, "X"=Other Player.
    Output: No returns, print current board to screen.
    Purpose: Print current board to screen
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def getPlayerLetter():
    """
    Input: None
    Output: Return either "X" or "O"
    Purpose: Decide what letter the human player is using.
    """
    myRand = random.randrange(2)
    if myRand == 0:
        return "X"
    elif myRand == 1:
        return "O"
# You could do this randomly or ask the user what they want.
def whoGoesFirst():
    """
    Input: None
    Output: Return either "X" or "O".
    Purpose: Decide who goes first.
    """
    myRand = random.randrange(2)
    if myRand == 0:
        return "X"
    elif myRand == 1:
        return "O"

def playAgain():
    """
    Input: None
    Output: Reset any variables (board, others?) to their initial values.
    Purpose: To start over.  Develop this function last.
    """
    main()

def makeMove(board, letter, move):
    """
    Inputs: board, list of length 9 as in draw()
    letter, string of length 1, "X" or "O"
    move, integer in range(0,9)
    Output: Return board with that letter assigned to location move.
    Purpose: To apply the move to the board.
    """
    board[move] = letter
    draw(board)

def isWinner(board, letter):
    """
    Inputs: board, list of length 9 as in draw()
    letter, string of length 1, "X" or "O"
    Output: Boolean, True (that player has won) or False (that player has not
    won)
     Purpose: Decide if the player with that letter has won or not.
    """
    winner = False
    if board[0] == board[1] == board[2]:
        winner = True

def isSpaceFree(board, move):
    """
    Inputs: board, list of length 9 as in draw()
    move, a number in range(0,9)
    Outputs: Boolean, True (location at move is free) or False (location at move
    is not free)
    Purpose: Check if a move is legal or not, by checking if that space is free
    or not.
    """
    if board[move] == " ":
        return True
    else:
        return False

def getPlayerMove(board):
    """
    Inputs: board, list of length 9 as in draw()
    Outputs: integer in range(0,9) which represents a legal move.
    Purpose: To get a legal move from a player.
    """
    spaceSelected = int(input("Which space (0-8) would you like select?"))
    spaceFree = isSpaceFree(board, spaceSelected)
    while spaceFree == False:
        spaceSelected = int(input("Which space (0-8) would you like select?"))
        spaceFree = isSpaceFree(board, spaceSelected)
    return spaceSelected

def chooseRandomMove(board):
    """
    Inputs: board, list of length 9 as in draw()
    Outputs: integer in range(0,9) which represents a legal move.
    Purpose: Make a list of legal moves, then select one of them at random.
    """
    free = False
    while free == False:
        randMove = random.randrange(0,8)
        if board[randMove] == " ":
            free = True
        else:
            free = False
    return randMove
def isBoardFull(board):
    """
    Inputs: board, list of length 9 as in draw()
    Outputs: Boolean, True (board is full) or False (there is at least one free
    space).
    Purpose: Check if the game is over because the board is full (so game ends
    in a tie/draw).
    """
    for entry in board:
        if entry == " ":
            return False
main()
