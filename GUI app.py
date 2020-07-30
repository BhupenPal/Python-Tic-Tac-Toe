from tkinter import *
import os

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
current_player = "X"
winner = None


def handle_turn(player, butnum):
    board[butnum] = player
    BoardButtons[butnum].config(text=player)


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


def play_game(butnum):
    handle_turn(current_player, butnum)
    check_if_game_over()
    flip_player(current_player)

    if winner == 'X' or winner == 'O':
        winner_text = 'Player ' + winner + ' won!'
        WinnerTag.config(text=winner_text)
    elif "-" in board:
        return
    elif winner is None:
        winner_text = 'Game Tie!'
        WinnerTag.config(text=winner_text)


root = Tk()
root.geometry("850x555")
root.config(bg="#006a71")
root.title("Bhupen Pal")

# Board - Frame - Left Panel
Board = Frame(root, bg='#006a71', borderwidth=5)
Board.pack(side=LEFT, fill=Y)

# Board Buttons
BoardButtons = [None for x in range(9)]
BoardButtons[0] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(0))
BoardButtons[0].grid(row=1, column=1)
BoardButtons[1] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(1))
BoardButtons[1].grid(row=1, column=2)
BoardButtons[2] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(2))
BoardButtons[2].grid(row=1, column=3)
BoardButtons[3] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(3))
BoardButtons[3].grid(row=2, column=1)
BoardButtons[4] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(4))
BoardButtons[4].grid(row=2, column=2)
BoardButtons[5] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(5))
BoardButtons[5].grid(row=2, column=3)
BoardButtons[6] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(6))
BoardButtons[6].grid(row=3, column=1)
BoardButtons[7] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(7))
BoardButtons[7].grid(row=3, column=2)
BoardButtons[8] = Button(Board, width=20, height=10, bg='#ffffdd', bd=0, command=lambda: play_game(8))
BoardButtons[8].grid(row=3, column=3)

# Header - Frame
Header = Frame(root, bg='#006a71', borderwidth=5)
Header.pack(side=TOP, fill=X)

HeadTag = Label(Header, text="Tic Tac Toe", font="Helvetica 30", bg='#006a71', fg='white')
HeadTag.pack(fill=X, pady=50)

WinnerTag = Label(text="", bg="#006a71", font="Helvetica 30", fg='white')
WinnerTag.pack(fill=Y, pady=50)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


RestartButton = Button(root, text="Restart Game", command=restart_program)
RestartButton.pack(pady=50)

root.mainloop()