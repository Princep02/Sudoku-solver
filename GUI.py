from tkinter import*
from solver import solver

root=Tk()
root.title("Sudoku Solver")  # windows title
root.geometry("324x550")  # dimension of window using geometry method

label=Label(root,text="Fill in the numbers and click solve").grid(row=0,column=1,columnspan=10)
#breifing usage of program.

errLabel=Label(root,text="",fg="red")  #error if sudoku is not solvalabe
errLabel.grid(row=15,column=1,columnspan=10,pady=5)  #grid method to place the label

solvedLabel=Label(root,text="",fg="green")  #success label after successfully solving the sudoku
solvedLabel.grid(row=15,column=1,columnspan=10,pady=5)

cells={}  #reating empty dictionary where we store each cell of the input grid

def ValidateNumber(P):  #method to validate the number is sigle digit
    out= (P.isdigit() or P=="")and len(P)<2
    return out

reg=root.register(ValidateNumber)  #register the function to the windows

def draw3x3Grid(row,column,bgcolor): #divide the 9*9 grid into 3*3 grid
    for i in range(3):  #indicate rows
        for j in range(3):  #indicate columns
            e=Entry(root,width=5,bg=bgcolor,justify="center",validate="key",validatecommand=(reg,"%P")) #entry widget to enter the num and validate it
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i+1,column+j+1)]=e

def draw9x9Grid():  
    color="#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if color=="#D0ffff":
                color="#ffffd0"
            else:
                color="#D0ffff"

def clearValues():  #this clear values in each cell of the grid
    errLabel.configure(text="")  #clear the error
    solvedLabel.configure(text="") #clear success label
    for row in range(2,11):  #iterate through rows and column
        for col in range(1,10):
            cell=cells[(row,col)]
            cell.delete(0,"end")  #delete method to delete from entry widget

def getValues():
    board=[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")  /clear label if any
    for row in range(2,11):  #iterate over rows
        rows=[] #create empty list
        for col in range(1,10):  #iterate over columns
            val=cells[(row,col)].get()  #using entry widget get method get values of cell
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))  #else appent integer values

        board.append(rows)
    updateValues(board)

btn=Button(root, command=getValues, text="Solve", width=10)  #using btn widget create button to solve
btn.grid(row=20,column=1,columnspan=5,pady=20)

btn=Button(root, command=clearValues, text="Clear", width=10) #using btn widget create button to clear
btn.grid(row=20,column=5,columnspan=5,pady=20)

def updateValues(s): #update value function to update the solved sudolu values in cell and display
    sol=solver(s)    #call solver function
    if sol !="no":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")  #delete existing values from the cell
                cells[(rows,col)].insert(0,sol[rows-2][col-1])  #insert method to insert value at 0th index
        solvedLabel.configure(text="Sudoku solved!")   #text
    else:
        errLabel.configure(text="No solution exists for this sudoku") #error if not solved
        


draw9x9Grid()
root.mainloop()   #to launch the instance of crated window
            
