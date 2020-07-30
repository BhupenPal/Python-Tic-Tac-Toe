import os
os.system('clear')
# Declaring Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
current_player = "X"
winner = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):
    position = int(input("Choose a position from 1-9: "))
    board[position - 1] = player
    os.system('clear')
    display_board()


def check_win_row():
    global game_still_going
    global current_player
    global winner
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        winner = current_player
        game_still_going = False


def check_win_column():
    global game_still_going
    global current_player
    global winner
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        winner = current_player
        game_still_going = False


def check_win_diagonal():
    global game_still_going
    global current_player
    global winner
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        winner = current_player
        game_still_going = False


def check_if_win():
    check_win_row()
    check_win_column()
    check_win_diagonal()
    return


def check_if_tie():
    global game_still_going
    test = True
    for grid in board:
        if grid == "-":
            test = False
    if test:
        game_still_going = False
    return


def check_if_game_over():
    check_if_win()
    check_if_tie()


def flip_player(player):
    global current_player
    if player == 'X':
        current_player = 'O'
    elif player == 'O':
        current_player = 'X'
    return


def play_game():
    # Display Empty Board
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player(current_player)

    if winner == 'X' or winner == 'O':
        print('Player ' + winner + ' won!')
    elif winner is None:
        print('Game Tie')


play_game()
