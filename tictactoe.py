def print_board(board):
    print("\n")
    print("  1   2   3")
    for i, row in enumerate(board):
        print(i + 1, " | ".join(row))
        if i < 2:
            print("  ---------")
    print("\n")

def check_win(board, player):
    # rows
    for row in board:
        if row.count(player) == 3:
            return True
    # columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("=== Tic Tac Toe ===")
    print("Players take turns entering row and column numbers (1-3).")
    
    while True:
        print_board(board)
        print(f"Player {player}'s turn.")

        try:
            row = int(input("Row (1-3): ")) - 1
            col = int(input("Col (1-3): ")) - 1
        except:
            print("Enter numbers only!")
            continue

        # Check valid
        if row not in range(3) or col not in range(3):
            print("Invalid position!")
            continue

        if board[row][col] != " ":
            print("Spot taken!")
            continue

        board[row][col] = player

        # Check win
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} WINS!")
            break

        # Check draw
        if board_full(board):
            print_board(board)
            print("It's a DRAW!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Run game
tic_tac_toe()