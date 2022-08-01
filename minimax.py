class move:
    def __init__(self, row, col):
        self.row = row
        self.col = col


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


def minimax(board,isMax):
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
                    best = max(best, minimax(board,not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board,not isMax))
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
                moveVal = minimax(board, True)
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


def printBoard(board):
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print("\n")


def initalizeboard(board):
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    return board


def map():
    map = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [
        1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    return map


def playerplace(board):
    run = True
    while run:
        place = input('Please select a position to place an \'X\' (1-9): \n')
        try:
            place = int(place)
            if place > 0 and place < 10:
                pmove = move(-1, -1)
                pmove.row = map()[place][0]
                pmove.col = map()[place][1]
                if indexfree(board, pmove.row, pmove.col):
                    run = False
                    board[pmove.row][pmove.col] = player
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def opponentplace(board):
    print("Opponent Turn \n")
    bestMove = findBestMove(board)
    if indexfree(board, bestMove.row, bestMove.col):
        board[bestMove.row][bestMove.col] = opponent


def main():
    board = [[]]
    board = initalizeboard(board)
    printBoard(board)
    score=evaluate(board)
    while ismoveleft(board):
        playerplace(board)
        printBoard(board)
        opponentplace(board)
        printBoard(board)
        score = evaluate(board)
        if score != 0:
            break
    if score == 10:
        print("You Won This Game, Congratulations")
    elif score == -10:
        print("The Opponent Won This Game, You Lost")
    elif score==0:
        print("It's a Tie, Good Game")


if __name__ == "__main__":
    main()
