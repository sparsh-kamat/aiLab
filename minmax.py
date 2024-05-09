import math

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    elif total_moves == 0:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = '_'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '_'
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '_'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game(total_moves):
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print_board(board)
    while total_moves > 0:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] != '_':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'O'
        total_moves -= 1
        print_board(board)
        if evaluate(board) == -10:
            print("You win!")
            return
        if total_moves == 0:
            print("It's a tie!")
            return
        row, col = find_best_move(board)
        board[row][col] = 'X'
        total_moves -= 1
        print_board(board)
        if evaluate(board) == 10:
            print("You lose!")
            return
        if total_moves == 0:
            print("It's a tie!")
            return

total_moves = 9
play_game(total_moves)
