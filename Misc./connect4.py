def win(board, turn, move):
    if turn == 43:
        return "draw"
    
    for row in range(6):
        for col in range(3):
            match = True
            for i in range(4):
                if move != board[row][col+i]: match = False
            if match: return move
    
    for row in range(2):
        for col in range(7):
            match = True
            for i in range(4):
                if move != board[row+i][col]: match = False
            if match: return move
            
    for row in range(2):
        for col in range(3):
            match = True
            for i in range(4):
                if move != board[row+i][col+i]: match = False
            if match: return move
    
    for row in range(2):
        for col in range(3):
            match = True
            for i in range(4):
                if move != board[row-i][col+i]: match = False
            if match: return move

    return False

def recurs(board, turn):
    if turn % 2 == 1:
        move = "R"
    else:
        move = "B"
    for i in range(7):
        for j in range(1,6):
            if board[j][i] != 0:
                board[j-1][i] = move
        if board[5][i] == 0:
            board[5][i] = move
        condition = win(board, turn, move)
        if condition == False:
            recurs(board, turn+1)
        else:
            for i in range(6):
                for j in range(7):
                    print(board[i][j], end = " ")
                print()
            if condition == "draw":
                print("draw")
            elif condition == "R":
                print("red win")
            elif condition == "B":
                print("black win")
            print(1)
            return 1

board = [[0 for _ in range(7)] for i in range(6)]
print(board)
turn = 1
recurs(board, turn)