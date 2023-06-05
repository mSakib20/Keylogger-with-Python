#Creating a Tic Tac Toe Board 
tBoard = {1: ' ', 2: ' ', 3: ' ',
          4: ' ', 5: ' ', 6: ' ',
          7: ' ', 8: ' ', 9: ' '}

player = 'O'
computer = 'X'

#Printing the board
def printBoard(tBoard):
    print(tBoard[1] + "|" + tBoard[2] + "|" + tBoard[3])
    print("-+-+-")
    print(tBoard[4] + "|" + tBoard[5] + "|" + tBoard[6])
    print("-+-+-")
    print(tBoard[7] + "|" + tBoard[8] + "|" + tBoard[9])
    print("\n")

#Checking if the selected position/space in the board is free
def freeSpaceChecker(position):
    if tBoard[position] == ' ':
        return True
    return False

def insertLetter(letter, position):
    if freeSpaceChecker(position):
        tBoard[position] = letter
        printBoard(tBoard)

        #Now checking if the move makes it a draw/win 
        if drawChecker():
            print("It's a DRAW!!")
            exit()
        if winnerChecker():
            if letter == 'X':
                print("Computer WINS!!")
                exit()
            else:
                print("Did you really just beat the AI??")
                exit()
        return
    else:
        print("Invalid MOVE!!")
        print("\n")

        position = int(input("Please enter a new postion this time!"))
        insertLetter(letter, position)
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
    
#Cheking to see who wins the game X or O (backgroud check for the AI to decide the best move)
def winner(mark):
    if (tBoard[1] == tBoard[2] and tBoard[1] == tBoard[3] and tBoard[1] == mark):
        return True
    elif (tBoard[4] == tBoard[5] and tBoard[4] == tBoard[6] and tBoard[4] == mark):
        return True
    elif (tBoard[7] == tBoard[8] and tBoard[7] == tBoard[9] and tBoard[7] == mark):
        return True
    elif (tBoard[1] == tBoard[4] and tBoard[1] == tBoard[7] and tBoard[1] == mark):
        return True
    elif (tBoard[2] == tBoard[5] and tBoard[2] == tBoard[8] and tBoard[2] == mark):
        return True
    elif (tBoard[3] == tBoard[6] and tBoard[3] == tBoard[9] and tBoard[3] == mark):
        return True
    elif (tBoard[1] == tBoard[5] and tBoard[1] == tBoard[9] and tBoard[1] == mark):
        return True
    elif (tBoard[7] == tBoard[5] and tBoard[7] == tBoard[3] and tBoard[7] == mark):
        return True
    else:
        return False
    


#Cheking to see if the game is DRAW  
def drawChecker():
    for key in tBoard.keys():
        if tBoard[key] == ' ':
            return False
    return True

def humanPlayerMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter(player, position)
    return

def computerPlayerMove():
    position = int(input("Enter a position for 'X': "))
    insertLetter(computer, position)
    return

#Code for the AI to calulate the best move for the node
def aiMovexxx():
    bestScore = -999
    bestMove = 0
                
    for key in tBoard.keys():                       #looping through all the empty spaces inside the dictionary and calculating the minimax for each key
        if tBoard[key] == ' ':
            tBoard[key] = computer    
            score = miniMax(tBoard, False)
            tBoard[key] == ' '                      #after getting the value for 'score' replacing the key with an empty string
            if score > bestScore:                   
                bestScore = score                   #keeping track of the 'bestScore'
                bestMove = key                      #setting the currect key as the postion for the 'tBoard'
    insertLetter(computer, bestMove)                #inserting computer letter (X) in the board at the place which may lead to the victory
    return

#same exact replica of aiMovexxx() bt if I run it with the aiMovexxx() the AI doesnt work!! I WANNA PULL MY HAIR
def aiMove():
    bestScore = -999
    bestMove = 0

    for key in tBoard.keys():
        if tBoard[key] == ' ':
            tBoard[key] = computer
            score = miniMax(tBoard, False)
            tBoard[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    insertLetter(computer, bestMove)
    return 



def miniMax(tBoard, maximizing):
    if winner(computer):
        return 1
    elif winner(player):
        return -1
    elif drawChecker():
        return 0
    
    if maximizing:
        bestScore = -999

        for key in tBoard.keys():
            if tBoard[key] == ' ':
                tBoard[key] = computer
                score = miniMax(tBoard, False)
                tBoard[key] = ' '
                
                if score > bestScore:
                    bestScore = score
        return bestScore
    
    else:
        bestScore = 999
        for key in tBoard.keys():
            if tBoard[key] == ' ':
                tBoard[key] = player
                score = miniMax(tBoard, True)
                tBoard[key] = ' '
                
                if score < bestScore:
                    bestScore = score
        return bestScore

#Driver starts here
print("\n")
printBoard(tBoard)

#Creating a game loop
while not winnerChecker():
    #aiMovexxx
    aiMove()
    humanPlayerMove()
    #computerPlayerMove()
