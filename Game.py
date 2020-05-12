# TicTacToe IA Never Lost

board = [ ["-","-","-"],
          ["-","-","-"],
          ["-","-","-"] ]

def verifyPlace( place ):
    count = 0
    for i in range(len(board)):
        for b in range(len(board[i])):
            count += 1
            if ( count == place):
                if (board[i][b] == "-"):
                    return [i,b]
                else:
                    return False
    return False

def printBoard():
    print("\n**************************************")
    print("Current Board | Choose A Place by it own Number")
    count = 0
    for i in range(len(board)):
        for b in range(len(board[i])):
            print(board[i][b], " ", end = '')
        print("\t\t", end= '')
        for b in range(len(board[i])):
            count = count+1
            print(count, " ", end = '')
        print()
    print("**************************************")

def isEnd():
    filled = 0
    cont = len(board) - 1
    markedD = 0
    markedID = 0
    for i in range(len(board)):
        markedH = 0
        markedV = 0
        for a in range(len(board[i])):

            # Check TIE
            if (board[i][a] != "-"):
                filled += 1
      
            # Check Horizontal Win
            if (board[i][a] == 'O'):
                markedH += 1

            # Check Vertical Win
            if (board[a][i] == 'O'):
                markedV += 1

            # IF H/V Win -> Return
            if (markedH == 3 or markedV == 3):
                return "Machine Wins"        
            
        # Check Diagonal Win
        if (board[i][i] == 'O'):
            markedD += 1

        # Check Inverse Diagonal Win
        if (board[i][cont] == 'O'):
            markedID += 1

        # IF D/ID Win -> Return
        if (markedD == 3 or markedID == 3):
            return "Machine Wins"  

        cont = cont - 1

    # IF Tie -> Return
    if (filled == 9):
        return "Tie"
    else:
        return False


#  Rule 1: Check IF Machine or Player can Win [ IF needs 1 place to Win ]
def machineRule1(marker):
    markedD = 0
    markedID = 0
    checkD = []
    checkID = []
    cont = 0
    for i in range(len(board)):
        markedH = 0
        markedV = 0
        checkV = []
        checkH = []
        for a in range(len(board)):
            # Check Horizontal Win
            if (board[i][a] == marker):
                markedH += 1
            elif (board[i][a] == '-'):
                checkH = [i,a]

            # IF Horizontal Win -> Return
            if (markedH == 2 and checkH != []):
                return checkH;      

            # Check Vertical Win
            if (board[a][i] == marker):
                markedV += 1
            elif (board[a][i] == '-'):
                checkV = [a,i]  

            # IF Vertical Win -> Return
            if (markedV == 2 and checkV != []):
                return checkV;        
            
        # Check Diagonal Win
        if (board[i][i] == marker):
            markedD += 1
        elif (board[i][i] == '-'):
            checkD = [i,i]

        # IF Diagonal Win -> Return
        if (markedD == 2 and checkD != []):
            return checkD;   

        # Check Inverse Diagonal Win
        if (board[i][cont] == marker):
            markedID += 1
        elif (board[i][cont] == '-'):
            checkID = [i,cont]

        # IF Inverse Diagonal Win -> Return
        if (markedID == 2 and checkID != []):
            return checkID;   

        cont = cont - 1

    if (marker == "O"):
        return machineRule1('X')
    else:
        return machineRule2()

# Rule 2: IF the center is open -> fill the center
def machineRule2():
    if (board[1][1] == '-'):
        return [1,1]
    else:
        return machineRule3()

# Rule 3: IF player fill a corner -> fill the opposite corner
def machineRule3():
    if(board[0][0] == 'X' and board[2][2] == '-'):
        return [2,2]
    if(board[0][0] == '-' and board[2][2] == 'X'):
        return [0,0]
    if(board[0][2] == 'X' and board[2][0] == '-'):
        return [2,0]
    if(board[2][0] == 'X' and board[0][2] == '-'):
        return [0,2]
    return machineRule4()

# Rule 4: If pla 
def machineRule4():
    if ( (board[0][0] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[2][0] == 'X') ):
        if(board[0][1] == '-'):
            return [0,1]
        elif(board[1][0] == '-'):
            return [1,0]
        elif(board[1][2] == '-'):
            return [1][2]
        elif(board[2][1] == '-'):
            return [2][1]
    return machineRule5()

# Rule 5: If none of the previous rules were used, fill in any a corner. 
def machineRule5():
    if(board[0][0] == '-'):
        return [0,0]
    if(board[0][2] == '-'):
        return [0,2]
    if(board[2][0] == '-'):
        return [2,0]
    if(board[2][2] == '-'):
        return [2,2]
    return machineRule6()

# Rule 5: If none of the previous rules were used, fill the first availabe place. 
def machineRule6():
    for i in range(len(board)):
        for a in range(len(board)):
            if (board[i][a] == '-'):
                return [i,a]
    return False

def main():
    endgame = False
    errorInput = False
    while(endgame != True):
        if not (errorInput):
            printBoard()
        print("\nEnter Your Chosen Place: ", end='')
        place = int(input())
        pos = verifyPlace(place)
        if not pos:
            print("Error: Enter a valid value (1-9) for an unfilled place.\n")
            errorInput = True
        else:
            board[pos[0]][pos[1]] = 'X'
            errorInput = False

            # Run Machine IA
            choise = machineRule1('O')

            if (choise):
                board[choise[0]][choise[1]] = 'O'

            res = isEnd()
            if (res):
                printBoard()
                print (res,"\n")
                return True
main()