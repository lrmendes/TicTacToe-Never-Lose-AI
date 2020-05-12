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


#  Rule 0: Check IF Machine can Win [ IF needs 1 place to Win ]
def machineRule0():
    marked = 0
    
    for i in range(len(board)):
        # Check Machine Horizontal Win
        marked = 0
        check = []
        for a in range(len(board)):
            if (board[i][a] == 'O'):
                marked += 1
            elif (board[i][a] == '-'):
                check = [i,a]
            else:
                marked = 0
        if (marked == 2 and check != []):
            return check

        # Check Machine Vertical Win
        marked = 0
        check = []
        for a in range(len(board)):
            if (board[a][i] == 'O'):
                marked += 1
            elif (board[a][i] == '-'):
                check = [a,i]
            else:
                marked = 0
        if (marked == 2 and check != []):
            return check

    # Check Diagonal Win
    marked = 0
    check = []
    for i in range(len(board)):
        if (board[i][i] == 'O'):
            marked += 1
        elif (board[i][i] == '-'):
            check = [i,i]
        else:
                marked = 0
    if (marked == 2 and check != []):
        return check    

    # Check Inverse Diagonal Win
    marked = 0
    check = []
    cont = 0
    for i in range(len(board)-1,-1,-1):
        if (board[cont][i] == 'O'):
            marked += 1
        elif (board[cont][i] == '-'):
            check = [cont,i]
        else:
            marked = 0
        cont += 1
    if (marked == 2 and check != []):
        return check   

    return machineRule1()

#  Rule 1: Check IF Player can Win [ IF needs 1 place to Win ]
def machineRule1():
    marked = 0
   
    for i in range(len(board)):
         # Check Player Horizontal Win
        marked = 0
        check = []
        for a in range(len(board)):
            if (board[i][a] == 'X'):
                marked += 1
            elif (board[i][a] == '-'):
                check = [i,a]
        if (marked == 2 and check != []):
            return check

        # Check Player Vertical Win
        marked = 0
        check = []
        for a in range(len(board)):
            if (board[a][i] == 'X'):
                marked += 1
            elif (board[a][i] == '-'):
                check = [a,i]
        if (marked == 2 and check != []):
            return check

    # Check Player Diagonal Win
    marked = 0
    check = []
    for i in range(len(board)):
        if (board[i][i] == 'X'):
            marked += 1
        elif (board[i][i] == '-'):
            check = [i,i]
    if (marked == 2 and check != []):
        return check    

    # Check Player Inverse Diagonal Win
    marked = 0
    check = []
    cont = 0
    for i in range(len(board)-1,-1,-1):
        if (board[cont][i] == 'X'):
            marked += 1
        elif (board[cont][i] == '-'):
            check = [cont,i]
        cont += 1
    if (marked == 2 and check != []):
        return check   

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
            choise = machineRule0()

            if (choise):
                board[choise[0]][choise[1]] = 'O'

            res = isEnd()
            if (res):
                printBoard()
                print (res,"\n")
                return True
main()
        