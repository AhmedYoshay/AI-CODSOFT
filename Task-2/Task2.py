import math

# Constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if the game is over
def game_over(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY:
            return True

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True

    # Check if the board is full
    if all([cell != EMPTY for row in board for cell in row]):
        return True

    return False

# Function to get the empty positions on the board
def empty_positions(board):
    positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                positions.append((i, j))
    return positions

# Function to evaluate the board
def evaluate(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY:
            return row[0]

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # If no winner, return None
    return None

# Function to execute Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if game_over(board):
        return 1 if evaluate(board) == PLAYER_X else -1 if evaluate(board) == PLAYER_O else 0

    if maximizing_player:
        max_eval = -math.inf
        for i, j in empty_positions(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i, j in empty_positions(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move for the AI player
def best_move(board):
    best_score = -math.inf
    move = None
    for i, j in empty_positions(board):
        board[i][j] = PLAYER_X
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]

    print("Let's play Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        # Player's move
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if board[row][col] != EMPTY:
            print("Invalid move. Try again.")
            continue
        board[row][col] = PLAYER_O
        print_board(board)

        # Check if player wins
        if game_over(board):
            winner = evaluate(board)
            if winner:
                print(f"{winner} wins!")
                break

        # Check for a tie
        if all([cell != EMPTY for row in board for cell in row]):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        row, col = best_move(board)
        board[row][col] = PLAYER_X
        print_board(board)

        # Check if AI wins
        if game_over(board):
            winner = evaluate(board)
            if winner:
                print(f"{winner} wins!")
                break

        # Check for a tie
        if all([cell != EMPTY for row in board for cell in row]):
            print("It's a tie!")
            break

    # If the game ends without a winner, it's a tie
    if not winner:
        print("It's a tie!")

play_game()
