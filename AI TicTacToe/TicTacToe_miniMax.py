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

printBoard(tBoard)
