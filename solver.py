N=9  #declare variable hold num of rows or cols

def isSafe(sudoku, row, col, num):  #fuction to check is it ok to assign a num in given rows and cols
    for i in range(9):
        if sudoku[row][i]==num:  #check in rows
            return False

    for i in range(9):
        if sudoku[i][col]==num:  #check in cols
            return False

    startRow=row-row%3  #chech same num exists in 3*3 grid
    startCol=col-col%3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow+i][startCol+j]==num:
                return False
    return True  #executes if none of above condition is satsified

def solveSudoku(sudoku, row, col):   #function to solve sudoku
    if row==N-1 and col==N:  #base conditon since we use recursion
        return True

    if col==N:
        row+=1
        col=0

    if sudoku[row][col]>0:
        return solveSudoku(sudoku, row, col+1)

    for num in range(1,N+1):
        if isSafe(sudoku, row, col, num): #if ok to assign num we assign in sudoku
            sudoku[row][col]=num

            if solveSudoku(sudoku,row,col+1): #check for possibility with next column
                return True



        sudoku[row][col]=0 #reassign 0 at given position since our assumption was wrong
    return False

def solver(sudoku):  #function to solve sudoku if solvable
  if solveSudoku(sudoku, 0, 0):  #take sudoku as arguement and solve starting form 0,0
      return sudoku
  else:
      return"no"
