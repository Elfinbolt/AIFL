import random

board = [str(i) for i in range(1, 10)]

def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def board_full():
    return all(cell in ['X', 'O'] for cell in board)

def user_move():
    while True:
        choice = input("Enter position (1-9): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 9 and board[choice - 1] not in ['X', 'O']:
                board[choice - 1] = 'X'
                break
        print("Invalid move. Try again.")

def find_winning_move(player):
    for i in range(9):
        if board[i] not in ['X', 'O']:
            temp = board[i]
            board[i] = player
            if check_winner(player):
                board[i] = temp
                return i
            board[i] = temp
    return None

def computer_move():
    # 1. Try to win
    move = find_winning_move('O')
    if move is not None:
        board[move] = 'O'
        print("Computer chose position", move + 1)
        return

    # 2. Block user
    move = find_winning_move('X')
    if move is not None:
        board[move] = 'O'
        print("Computer blocked at position", move + 1)
        return

    # 3. Take center
    if board[4] not in ['X', 'O']:
        board[4] = 'O'
        print("Computer took center (5)")
        return

    # 4. Take a corner
    corners = [0, 2, 6, 8]
    for i in corners:
        if board[i] not in ['X', 'O']:
            board[i] = 'O'
            print("Computer chose corner", i + 1)
            return

    # 5. Take any remaining spot
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = 'O'
            print("Computer chose position", i + 1)
            return

current_player = random.choice(["user", "computer"])
print("First move:", current_player.upper())

while True:
    print_board()

    if current_player == "user":
        user_move()
        if check_winner('X'):
            print_board()
            print("You win! 🎉")
            break
        current_player = "computer"

    else:
        computer_move()
        if check_winner('O'):
            print_board()
            print("Computer wins 🤖")
            break
        current_player = "user"

    if board_full():
        print_board()
        print("It's a draw!")
        break