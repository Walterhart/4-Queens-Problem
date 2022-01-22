#Program will try to find N-queen solution for given csv file
import pandas as pd
from pandas import DataFrame

# This function will print out board
def printBoard(board, N):

    for i in range(N):
        for j in range(N-1):
            print(board[i][j], ", ", end='')
        print(board[i][N-1])

# This function will store solution into 'Solution.csv'
def  solutionSaved(board):
    printBoard(board,len(board[0]))
    df2=pd.DataFrame(board)
    df2.to_csv('Solution.csv',sep=',',index=False, columns=None, header=False)






# This function will print out starting board and load csv file into a data frame
def loadQueen():

    df= pd.read_csv("Input.csv", header=None)
    data=df.values.tolist()
    message1= "This is your starting board"
    line1="---------------------------------------------------------------"
    print(message1)
    print(line1)
    printBoard(data,len(data[0]))
    print(line1)

    return(data)




# Functions will check if there a conflict between queens
# It will check  same row, diagonal left, diagonal right
# then return True if no confict occurs
def isSafe(board, row, col, N ):

    for i in range(N):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N),
                    range(col, N)):
        if board[i][j] == 1:
            return False

    return True

# Function will  check for solution for the board
# by using recursion and going row by row then placing a queen down if
# isSafe is true
# If not function will backtrack to remove queen and try next row
def solveBoard(board,count):

    N=len(board[0])

    if count >= N:
        return True

    queen = False
    for i in range(N):
        if board[count][i] == 1:
            queen = True
            break

    if queen:
        if solveBoard(board, count+1) == True:
            return True

    elif not queen:
        for i in range(N):
            if isSafe(board, count, i,N):
                board[count][i] = 1
                if solveBoard(board, count + 1) == True:
                    return True

                board[count][i] = 0

    return False


# Check if the solution can be solve
# If solveBoard true will call solutionSaved
# If solveBoard return false will return no solution
def isSolution(board):

    print("\nSearching for a solution......")
    if solveBoard(board,0)==True:
         line2='---------------------------------------------------------------'
         message2="\nHere is board solution"
         message3="\nSolution has been saved"
         print(message2)
         print( line2)
         solutionSaved(board)
         print( line2)
         print(message3)

    else:
        print("\nNo solution")



#Drive code
board=[]
board=loadQueen()
isSolution(board)
