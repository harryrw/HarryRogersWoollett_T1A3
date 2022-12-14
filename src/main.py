# imports
import random
from simple_term_menu import TerminalMenu
import clearing
from ascii import end_screen

# Clear Terminal
clearing.clear()


# Globals

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

clear_board = ["-", "-", "-",
               "-", "-", "-",
               "-", "-", "-"]

current_player = "X"
winner = None
game_running = True


# Display the gameboard
def print_board(board):
    """Prints the gameboard.

    Args:
        board (_type_): _description_
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Receive player input


def player_input(board):
    """Player marks position on grid.

    Args:
        board (_type_): _description_
    """    
    global game_running
    try:
        inp = int(input("Please enter a number between 1 and 9: "))
        if board[inp - 1] == "-":
            board[inp - 1] = current_player
        else:
            print("Sorry, that position is already occupied.")
    except ValueError:
        print("That wasn't a number, please try again.")
    except KeyboardInterrupt:
        print("\nThank you for playing.")
        game_running = False

# Assess Win or Draw


def check_row(board):
    """Checks rows of gameboard for win condition.

    Args:
        board (_type_): _description_

    Returns:
        _type_: _description_
    """    
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_column(board):
    """Checks columns of gameboard for win condition.

    Args:
        board (_type_): _description_

    Returns:
        _type_: _description_
    """    
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_diagonal(board):
    """Checks diagonals of gameboard for win condition.

    Args:
        board (_type_): _description_

    Returns:
        _type_: _description_
    """    
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def check_draw(board):
    """Checks gameboard for draw condition.

    Args:
        board (_type_): _description_
    """    
    global game_running
    if "-" not in board:
        print_board(board)
        print("It's a draw!")
        game_running = False


def check_win():
    """Evaluates if other check functions have returned True for win conditions.
    """    
    global game_running
    if check_row(board) or check_column(board) or check_diagonal(board):
        print_board(board)
        print(f"{current_player}, you win!")
        end_screen()
        # print result to tally.txt file
        with open('tally.txt', 'a') as f:
            f.write(f"{current_player}, you win! \n")
        game_running = False


# Change Player
def switch_player():
    """Switches player making input on game board.
    """    
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Computer Opponent
def cpu(board):
    """Generates random inputs for computer opponent

    Args:
        board (_type_): _description_
    """    
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()


# Game Running Loop

while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_draw(board)
    switch_player()
    cpu(board)
    check_win()
    check_draw(board)

# Print result to txt file

count = sum(1 for line in open('tally.txt'))
print(f'There have been {count} total games played.')

# Terminal Menu

def main():
    """Generates post-game terminal menu
    """    
    global board
    global game_running
    options = ["Play Again", "Quit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    if options[menu_entry_index] == "Play Again":
        board = clear_board
        game_running = True
        while game_running:
            print_board(board)
            player_input(board)
            check_win()
            check_draw(board)
            switch_player()
            cpu(board)
            check_win()
            check_draw(board)
    else:
        quit()


if __name__ == "__main__":
    main()
