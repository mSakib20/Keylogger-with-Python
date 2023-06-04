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

        #Now checking if the move makes it a draw
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
    return
        








printBoard(tBoard)

