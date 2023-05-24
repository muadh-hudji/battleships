"""Battleship game"""
from random import randint


def board():
    """
    Creates game board consisting of 5 rows and columns.
    The board are created of multilist, every index of
    the list shall contain a point "." representing
    that position of the board.
    """
    size = 5
    empty_game_board = []
    for _ in range(size):
        row_list = []
        for _ in range(size):
            row_list.append(".")
        empty_game_board.append(row_list)
    return empty_game_board


def add_ships_auto():

    """
    The function returns a multilist that contains the
    number of rows and colums where the ships will be
    placed on the board. The number of rows and columns
    are produced randomly in range 0 - 4. The function
    provide position for 4 ships.
    """

    ships = 0
    koord = []
    while ships < 4:
        x_label = randint(0, 4)
        y_label = randint(0, 4)
        busy = "no"
        for _, value in enumerate(koord):
            if x_label == value[0] and y_label == value[1]:
                busy = "yes"
        if busy == "yes":
            continue
        ship_koord = [x_label, y_label]
        koord.append(ship_koord)
        ships += 1
    return koord


def add_data_manually(koord, num, type_action):
    """
    The function returns a multilist that contains the
    number of rows and colums where the ships will be
    placed on the board. The number of rows and columns
    are taken as an input from the user in range 0 - 4.
    The function requires input for position of 4 ships.
    """
    if type_action == "populate":
        msg = "where the ships will be populated"
    else:
        msg = "you want attack"
    while num > 0:
        print("")
        print(f"Please enter the koordinate {msg}")
        print("The numbers shall be between 0-4 for the row and column")
        print("")
        data_row = input("Enter row number:\n")
        data_col = input("Enter column number:\n")
        if validate_data(data_row, data_col, koord, type_action):
            data = [int(data_row), int(data_col)]
            koord.append(data)
            num -= 1
            if type_action == "populate":
                print(f"Ship placed in row {data_row} and column {data_col}")
    return koord


def validate_data(row, col, koord, type_action):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there are numbers not between 0-4. The function will
    also validate if the numbers recently provided has been
    provided before and raises ValueError if it is.
    """
    try:
        int(row)
        int(col)
        if int(row) not in range(0, 5) or int(col) not in range(0, 5):
            raise ValueError(
                ("The numbers should be between 0 - 4, "
                 + "you provided " + str(row) + " for row, and " +
                 str(col) + " for column")
            )
    except ValueError as e_msg:
        print(f"Invalid data: {e_msg}, please try again.\n")
        return False
    if type_action == "populate":
        message = ("You have already placed a ship in row " + str(row) +
                   " column " + str(col))
    else:
        message = ("You have already attacked the position at row " +
                   str(row) + " column " + str(col))
    for _, value in enumerate(koord):
        try:
            if int(row) == value[0] and int(col) == value[1]:
                raise ValueError(
                    message
                )
        except ValueError as e_msg:
            print(f"Invalid data: {e_msg}, please try again.\n")
            return False
    return True


def populate_board(game_board, ships):
    """
    This function takes the multilist which considered
    as the game board and a list of positions where the
    ships will be placed. The position of the ships will
    be given a hashtag character "#".
    """
    for _, value in enumerate(ships):
        game_board[value[0]][value[1]] = "#"
    return game_board


def computer_choice(choices):
    """
    Receives an empty list to add a random integer
    numbers of the position where the computer attack
    will take a place on user board. Returns the list
    with the recently added position. The function will
    loop until its provide a position which are
    not used before.
    """
    while True:
        x_row = randint(0, 4)
        y_col = randint(0, 4)
        chosen = "no"
        for _, value in enumerate(choices):
            if x_row == value[0] and y_col == value[1]:
                chosen = "yes"
        if chosen == "yes":
            continue
        choice = [x_row, y_col]
        choices.append(choice)
        break
    return choices


def attack_board(board0, board1, attack_list, score):
    """
    Receive two boards, list of attack positions and the score,
    one of the boards used to hide the ships of the computer,
    and the other as a reference to check the content on specific
    position. The function adds asterisk mark "*" if it is a hit,
    or "X" if it is a miss. Returns the boards, incremented score
    if it is a hit, and a message.
    """
    if board1[attack_list[-1][0]][attack_list[-1][1]] == "#":
        board1[attack_list[-1][0]][attack_list[-1][1]] = "*"
        board0[attack_list[-1][0]][attack_list[-1][1]] = "*"
        message = "made a hit"
        score += 1
    else:
        board1[attack_list[-1][0]][attack_list[-1][1]] = "X"
        board0[attack_list[-1][0]][attack_list[-1][1]] = "X"
        message = "missed"
    return board0, board1, message, score


def display_board(game_board):
    """
    Displays the board as a string by looping through
    the multilist. It prints out one row at a time.
    """
    for _, aval in enumerate(game_board):
        string = ""
        for j in range(5):
            string += "    "
            string += "".join(aval[j])
        print(string)


def play_game(u_board, c_board):
    """
    This function is the main function of the game
    after creating a new game. The function is used to
    manage game steps to make inputs, attack, display
    the result and boards.
    """
    list_choices = []
    computer_choices = []
    hide_board = board()
    x_board = board()
    c_score = 0
    u_score = 0
    while True:
        list_choices = add_data_manually(list_choices, 1, "attack")
        hide_board, c_board, msg1, u_score = attack_board(hide_board,
                                                          c_board,
                                                          list_choices,
                                                          u_score)
        computer_choices = computer_choice(computer_choices)
        x_board, u_board, msg2, c_score = attack_board(u_board,
                                                       u_board,
                                                       computer_choices,
                                                       c_score)
        print("")
        print("*" * 28)
        print("        Player board")
        print("*" * 28)
        display_board(u_board)

        print("")
        print("*" * 28)
        print("        Computer board")
        print("*" * 28)
        display_board(hide_board)
        print("")
        print("_" * 38)
        print(" "*15, "Result")
        print(f"You {msg1}, your score: {u_score}")
        print("")
        print(f"Computer {msg2}, computer score: {c_score}")
        print("_" * 38)
        if u_score == 4 or c_score == 4:
            if u_score == 4 and c_score == 4:
                print("Draw!")
                print(f"Your score: {u_score}. Computer score: {c_score}")
            elif u_score == 4:
                print("Congratulation you win!")
                print(f"Your score: {u_score}. Computer score: {c_score}")
            else:
                print("You lost!")
                print(f"Your score: {u_score}. Computer score: {c_score}")
            break
        print("")


def new_game():
    """
    Start a new game by calling other functions to create
    game boards, choose the position of the ships. The User
    is able to  distibute the ships automatically or manually.
    """
    player_board = board()
    computer_board = board()
    list_ships_pos = []
    num_ships = 4

    print("Do you want to place out your ships manually?")
    choose_to_select = input("Enter any key for yes or n for no:\n")
    if choose_to_select.lower() == "n":
        player_ships = add_ships_auto()
    else:
        player_ships = add_data_manually(list_ships_pos, num_ships, "populate")
        print("Well done! You placed out all your ships.")
    player_board = populate_board(player_board, player_ships)
    print("")
    print("*" * 28)
    print("        Player board")
    print("*" * 28)
    display_board(player_board)

    print("")
    print("*" * 28)
    print("        Computer board")
    print("*" * 28)
    display_board(computer_board)
    computer_ships = add_ships_auto()
    computer_board = populate_board(computer_board, computer_ships)

    play_game(player_board, computer_board)


def game_menu():
    """
    In the menu of the game, the user is able to start a new game,
    read the rules or exit the game by typing 1, 2 or 3.
    """
    while True:
        print("")
        print("The Menu")
        print("1 - Start a new game")
        print("2 - Game rules")
        print("3 - Exit")
        alternative = input("Enter 1, 2 or 3\n")
        print(" ")
        if alternative == "1":
            new_game()
        elif alternative == "2":
            print("-"*58)
            print(" "*24, "Rules")
            print("Battleship is a guessing strategy game for two players. \
\nIt is played on two grid boards where a number of ships \
\nare distributed. The ships are hidden from each player.\n\
Players take turns attacking the other player by guessing\n\
the position of the ships on the board.")
            print("")
            print("The board consists of 5 rows and columns, and \
the attack\ninput has to be in numbers between 0 - 4.")
            print("")
            print("Your ships can be distributed on the board automatically\
\nor manually, the input has to be in numbers between 0 - 4.")
            print("")
            print("The player who hits 4 ships first wins the game.")
            print("-"*58)
        elif alternative == "3":
            break
        else:
            print(f"Invalid data: You provided following input {alternative}, \
the input has\nto be as described below, please try again.")


print("")
print("*"*33)
print("   Welcome to battleship game!")
print("*"*33)
game_menu()
