#Creating a Tic Tac Toe Board 
tBoard = {1: ' ', 2: ' ', 3: ' ',
          4: ' ', 5: ' ', 6: ' ',
          7: ' ', 8: ' ', 9: ' '}

#Printing the board
def printBoard(tBoard):
    print("\n")
    print(tBoard[1] + "|" + tBoard[2] + "|" + tBoard[3])
    print("-+-+-")
    print(tBoard[4] + "|" + tBoard[5] + "|" + tBoard[6])
    print("-+-+-")
    print(tBoard[7] + "|" + tBoard[8] + "|" + tBoard[9])
    print("\n")

#Checking if the selected position/space in the board is free
def freeSpaceChecker(postion):
    if tBoard(postion) == ' ':
        return True
    return False

def insertLetter(playerMove, position):
    if freeSpaceChecker(position) == ' ':
        tBoard[position] = playerMove
        print(tBoard)

        #Now checking if the move makes it a draw/win 
        if drawChecker():
            print("It's a DRAW!!")
            exit()
        elif winnerChecker():
            if playerMove == 'X':
                print("Computer WINS!!")
                exit()
            else:
                print("Did you really just beat the AI??")
                exit()
        else:
            print("ERROR!!")
            print("Check your insertLetter():")
            return
    else:
        print("Invalid MOVE!!")
        print("\n")

        postion = int(input("Please enter a new postion this time!"))
        insertLetter(playerMove, position)
        return
        
#Cheking to see who wins the game X or O 
def winnerChecker():
    if (tBoard[1] == tBoard[2] and tBoard[1] == tBoard[3] and tBoard[1] != ' '):
        return True
    elif (tBoard[4] == tBoard[5] and tBoard[4] == tBoard[6] and tBoard[4] != ' '):
        return True
    elif (tBoard[7] == tBoard[8] and tBoard[7] == tBoard[9] and tBoard[7] != ' '):
        return True
    elif (tBoard[1] == tBoard[4] and tBoard[1] == tBoard[7] and tBoard[1] != ' '):
        return True
    elif (tBoard[2] == tBoard[5] and tBoard[2] == tBoard[8] and tBoard[2] != ' '):
        return True
    elif (tBoard[3] == tBoard[6] and tBoard[3] == tBoard[9] and tBoard[3] != ' '):
        return True
    elif (tBoard[1] == tBoard[5] and tBoard[1] == tBoard[9] and tBoard[1] != ' '):
        return True
    elif (tBoard[7] == tBoard[5] and tBoard[7] == tBoard[3] and tBoard[7] != ' '):
        return True
    else:
        return False

#Cheking to see if the game is DRAW  
def drawChecker():
    for key in tBoard.keys():
        if tBoard[key] == ' ':
            return False
    return True








printBoard(tBoard)

