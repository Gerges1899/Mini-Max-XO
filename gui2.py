import tkinter
from tkinter.font import Font
from tkinter import messagebox

board=[['_','_','_'],['_','_','_'],['_','_','_']]

class move:
    def __init__(self, row, col):
        self.row = row
        self.col = col


gerges = tkinter.Tk()
gerges.geometry("400x445")
gerges.title('Tic-Tac-Toe')
text = tkinter.StringVar()
font = Font(size=32)


def changeText1():
    buttons[0][0].config(text="X")
    board[0][0]="X"
    opponentplace(board)
    iswinstate(board)

def changeText2():
    buttons[0][1].config(text="X")
    board[0][1]="X"
    opponentplace(board)
    iswinstate(board)

def changeText3():
    buttons[0][2].config(text="X")
    board[0][2]="X"
    opponentplace(board)
    iswinstate(board)

def changeText4():
    buttons[1][0].config(text="X")
    board[1][0]="X"
    opponentplace(board)
    iswinstate(board)

def changeText5():
    buttons[1][1].config(text="X")
    board[1][1]="X"
    opponentplace(board)
    iswinstate(board)

def changeText6():
    buttons[1][2].config(text="X")
    board[1][2]="X"
    opponentplace(board)
    iswinstate(board)

def changeText7():
    buttons[2][0].config(text="X")
    board[2][0]="X"
    opponentplace(board)
    iswinstate(board)

def changeText8():
    buttons[2][1].config(text="X")
    board[2][1]="X"
    opponentplace(board)
    iswinstate(board)

def changeText9():
    buttons[2][2].config(text="X")
    board[2][2]="X"
    opponentplace(board)
    iswinstate(board)

def reset():
    for i in range(0,3,1):
        for j in range(0,3,1):
            buttons[i][j].config(text="")
            board[i][j]='_'

player = 'X'
opponent = 'O'


def ismoveleft(board):
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if board[i][j] == '_':
                return True
    return False
                

def evaluate(b):
    for row in range(0, 3, 1):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return (-10)

    for col in range(0, 3, 1):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return (-10)
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return (-10)
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return (-10)
    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10:
        return score
    if score == -10:
        return score
    if ismoveleft(board) == False:
        return 0
    if isMax:
        best = -1000
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1,not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1,not isMax))
                    board[i][j] = '_'
        return best


def findBestMove(board):
    bestVal = 1000
    bestMove = move(-1, -1)
    bestMove.row = -1
    bestMove.col = -1
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if board[i][j] == '_':
                board[i][j] = opponent
                moveVal = minimax(board, 0, True)
                board[i][j] = '_'
                if moveVal < bestVal:
                    bestMove.row = i
                    bestMove.col = j
                    bestVal = moveVal

    return bestMove


def indexfree(board, row, col):
    if board[row][col] == '_':
        return True
    else:
        return False


def opponentplace(board):
    bestMove = findBestMove(board)
    if indexfree(board, bestMove.row, bestMove.col):
        board[bestMove.row][bestMove.col] = opponent
        buttons[bestMove.row][bestMove.col].config(text="O")

def iswinstate(board):
    G=evaluate(board)
    R=ismoveleft(board)
    if G==10:
        messagebox.showinfo("Tic Tac Toe","You Win")
    elif G==-10:
        messagebox.showinfo("Tic Tac Toe","You Lost")
    elif G==0 and R==False:
        messagebox.showinfo("Tic Tac Toe","It's a Draw")

b1 = tkinter.Button(gerges, text="", width=5,
                    height=2, font=font, command=changeText1)
b1.grid(row=1, column=0)
b2 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText2)
b2.grid(row=1, column=1)

b3 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText3)
b3.grid(row=1, column=2)

b4 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText4)
b4.grid(row=2, column=0)

b5 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText5)
b5.grid(row=2, column=1)
b6 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText6)
b6.grid(row=2, column=2)
b7 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText7)
b7.grid(row=3, column=0)
b8 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText8)
b8.grid(row=3, column=1)
b9 = tkinter.Button(
    gerges, text="", width=5, height=2, font=font, command=changeText9)
b9.grid(row=3, column=2)
b10=tkinter.Button(gerges,text="Play Again",width=36,height=1,font=Font,command=reset)
b10.grid(row=4, column=0,columnspan=3)
buttons = [[b1, b2, b3], [
    b4, b5, b6], [b7, b8, b9]]
gerges.mainloop()


