from pprint import pprint
from random import randint


def board():
    """
    Creates game board
    """
    size = 5
    empty_game_board = []
    for i in range(size):
        list = []
        for x in range(size):
            list.append(".")
        empty_game_board.append(list)
        
    return empty_game_board


def add_ships_auto():

    """
    Add 5 ships in the computer board randomly
    """

    ships = 0
    koord = []
    while ships < 4:
        x = randint(0,4)
        y = randint(0,4)
        busy = "no"
        for i in range(len(koord)):
            if x == koord[i][0] and y == koord[i][1]:
                busy = "yes"
        if busy == "yes":
            continue        
        ship_koord = [x, y]    
        koord.append(ship_koord)
        ships += 1
            
    return koord


def add_data_manually(koord, num, type):
    """
    The function take an input from the player for 
    the rows and columns for the koordinate where 
    the ships will be populated
    """
    if type == "populate":
        msg = "where the ships will be populated"
    else:
        msg = "you want attack"    
    while num > 0:
        print(f"Please enter the koordinate {msg}")
        print("The numbers shall be between 0-4 for the row and column")
        data_row = input("Enter row number:\n")
        data_col = input("Enter column number:\n")
        if validate_data(data_row, data_col, koord, type):
            data = [int(data_row), int(data_col)]
            koord.append(data)
            num -= 1
            if type == "populate":
                print(f"Ship placed in row {data_row} and column {data_col}")
   
    return koord


def validate_data(row, col, koord, type):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there numbers not between 0-4
    """
    try:
        int(row)
        int(col)
        if int(row) not in range(0, 5) or int(col) not in range(0, 5):
            raise ValueError(
                f"The numbers should be between 0 - 4, you provided {row} for row, and {col} for column."
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    if type == "populate":
        message = f"You have already placed a ship in row {row} and column {col}"
    else:
        message = f"You have already attacked the position at row {row} and column {col}"
    for i in range(len(koord)):
        try:
            if int(row) == koord[i][0] and int(col) == koord[i][1]:
                raise ValueError(
                    message
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False            
    return True    


def populate_board(board, ships):
    """
    This function will place out the ships in the player board
    to display it to the terminal
    """
    for i in range(len(ships)):
        board[ships[i][0]][ships[i][1]] = "#"

    return board        


def computer_choice(choices):
    """
    Function to produce a choice for the computer player
    """
    while True:
        x = randint(0,4)
        y = randint(0,4)
        chosen = "no"
        for i in range(len(choices)):
            if x == choices[i][0] and y == choices[i][1]:
                chosen = "yes"
        if chosen == "yes":
            continue        
        choice = [x, y]    
        choices.append(choice)
        break    
    
    return choices


def attack_board(board0, board1, list, score):
    """
    Attack board makes changes on the board by adding attack position
    """
    if board1[list[-1][0]][list[-1][1]] == "#":
        board1[list[-1][0]][list[-1][1]] = "*"
        board0[list[-1][0]][list[-1][1]] = "*"
        message = "made a hit"
        score += 1
    else:
        board1[list[-1][0]][list[-1][1]] = "X"
        board0[list[-1][0]][list[-1][1]] = "X"
        message = "missed"
    return board0, board1, message, score


def play_game(player_board, computer_board):
    """
    The function take the input of postion to attack
    from the computer and player, and give the result
    by displaying out the boards. 
    """
    list_choices = []
    computer_choices = []
    hide_board = board()
    computer_score = 0
    user_score = 0
    while True:
        list_choices = add_data_manually(list_choices, 1, "attack")
        print(list_choices[-1])
        hide_board, computer_board, message1, user_score = attack_board(hide_board, computer_board, list_choices, user_score)
        
        computer_choices = computer_choice(computer_choices)
        player_board, player_board, message2, computer_score = attack_board(player_board, player_board, computer_choices, computer_score)

        print(f"You {message1}, your score: {user_score}")
        print("")
        print(f"Computer {message2}, computer score: {computer_score}")
        print("*" * 28)
        print("        Computer board")
        print("*" * 28)
        pprint(player_board)

        print("")
        print("*" * 28)
        print("        Player board")
        print("*" * 28)
        pprint(hide_board)
        if user_score == 4 or computer_score == 4:
            if user_score == 4 and computer_score == 4:
                print(f"Draw, your score is {user_score}, computer score is {computer_score}")
            elif user_score == 4:
                print(f"Congratulation you win, your score is {user_score}, computer score is {computer_score}")
            else:
                print(f"You lost, your score is {user_score}, computer score is {computer_score}")    
            break
        print("")
        print("Do you want to continue?")
        continue_play = input("Enter any key for yes or n for no:\n")
        if continue_play == "n":
            break


def new_game():
    """
    Start a new game
    """
    player_board = board()
    computer_board = board()
    list_ships_pos = []
    num_ships = 4

    print("Do you want to place out your ships manually?")
    choose_to_select = input("Enter any key for yes or n for no:\n")
    if choose_to_select == "n":
        player_ships = add_ships_auto()
    else:
        player_ships = add_data_manually(list_ships_pos, num_ships, "populate")
        print("Well done! You placed out all your ships.")
    player_board = populate_board(player_board, player_ships)
    print("")
    print("*" * 28)
    print("        Player board")
    print("*" * 28)
    pprint(player_board)

    print("")
    print("*" * 28)
    print("        Computer board")
    print("*" * 28)
    pprint(computer_board)
    print("")
    print("Computers Ships populated in following places")
    computer_ships = add_ships_auto()
    print(computer_ships)
    computer_board = populate_board(computer_board, computer_ships)

    play_game(player_board, computer_board)


new_game()