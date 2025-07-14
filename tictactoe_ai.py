import math

board = [' '] * 9
AI = 'O'
YOU = 'X'

def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def print_sample_board():
    print()
    print("This is how positions are numbered:")
    sample = [str(i+1) for i in range(9)]
    for i in range(0, 9, 3):
        print(f" {sample[i]} | {sample[i+1]} | {sample[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def check_winner(board, player):
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def is_board_full(board):
    return ' ' not in board

def minimax_alpha_beta(board, depth, alpha, beta, maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, YOU):
        return -1
    if is_board_full(board):
        return 0

    if maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = YOU
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_move = -1
    best_eval = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            eval = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Game start
print("Welcome to Tic-Tac-Toe!")
print("You are 'X' and the AI is 'O'")
print_sample_board()

while True:
    print_board(board)
    try:
        move = int(input("Choose your move (1-9): "))
        if move < 1 or move > 9:
            print(" Invalid move. Pick a number from 1 to 9.")
            continue
    except ValueError:
        print(" Please enter a valid number.")
        continue

    move_index = move - 1

    if board[move_index] == ' ':
        board[move_index] = YOU
        if check_winner(board, YOU):
            print_board(board)
            print(" You win!")
            input("\nPress Enter to exit...")
            break
        if is_board_full(board):
            print_board(board)
            print(" It's a draw!")
            input("\nPress Enter to exit...")
            break

        ai_move = find_best_move(board)
        board[ai_move] = AI
        print("\nAI has made a move.\n")

        if check_winner(board, AI):
            print_board(board)
            print(" AI wins!")
            input("\nPress Enter to exit...")
            break
        if is_board_full(board):
            print_board(board)
            print(" It's a draw!")
            input("\nPress Enter to exit...")
            break
    else:
        print(" That cell is already taken. Try again.")
