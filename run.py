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


def add_ships_manually():
    """
    The function take an input from the player for 
    the rows and columns for the koordinate where 
    the ships will be populated
    """
    ships = 0 
    koord = []
    while ships < 5:
        print("Please enter the koordinate where the ships will be populated")
        print("The numbers shall be between 0-4 for the row and column")
        data_row = input("Enter row number:\n")
        data_col = input("Enter column number:\n")
        if validate_data(data_row, data_col, koord):
            data = [int(data_row), int(data_col)]
            koord.append(data)
            ships += 1
            print(f"Ship placed in row {data_row} and column {data_col}")
            if ships == 4:
                print("Well done! You placed out all your ships.")
                break
    return koord


def validate_data(row, col, koord):
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
    
    for i in range(len(koord)):
        try:
            if int(row) == koord[i][0] and int(col) == koord[i][1]:
                raise ValueError(
                    f"You have already placed a ship in row {row} and column {col}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False            
    return True    


def populate_ships(user_board, ships):
    """
    This function will place out the ships in the player board
    to display it to the terminal
    """
    for i in range(len(ships)):
        user_board[ships[i][0]][ships[i][1]] = "¤"
    return user_board
    

def computer_choice():
    """
    Function to produce a choice for the computer player
    """
    while True:
        choices = []
        x = randint(0,4)
        y = randint(0,4)
        for i in range(len(choices)):
            if x == choices[i][0] and y == choices[i][1]:
                continue
        choice = [x, y]    
        choices.append(choice)
        break    
    
    return choices


def new_game():
    """
    Start a new game
    """
    player_board = board()
    computer_board = board()

    print("Do you want to place out your ships manually?")
    choose_to_select = input("Enter any key for yes or n for no:\n")
    if choose_to_select == "n":
        player_ships = add_ships_auto()
    else:
        player_ships = add_ships_manually()
    populated_board = populate_ships(player_board, player_ships)
    print("")
    print("*" * 28)
    print("Player board")
    pprint(populated_board)

    print("")
    print("Computer board")
    pprint(computer_board)
    print("*" * 28)
    print("")
    print("Computers Ships populated in following places")
    computer_ships = add_ships_auto()
    print(computer_ships)
    


    

    # print("")
    # print("The choice of the computer is:")
    # comp_choice = computer_choice()
    # print(comp_choice)


new_game()