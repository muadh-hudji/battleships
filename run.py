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


def add_computer_ships():

    """
    Add 4 ships in the computer board randomly
    """

    ships = 0
    koord = []
    while ships < 5:
        x = randint(0,4)
        y = randint(0,4)
        for i in range(len(koord)):
            if x == koord[i][0] and y == koord[i][1]:
                continue
        ship_koord = [x, y]    
        koord.append(ship_koord)
        ships += 1
            
    return koord


def add_player_ships():
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
            if ships == 4:
                print("Well done! You placed out your ships.")
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
    print("Player board")
    pprint(player_board)
    print("*"*28)
    print("Computer board")
    a = computer_board[0].count(".")
    print(a)
    pprint(computer_board)

    print("")
    print("Computers Ships populated in following places")
    computer_ships = add_computer_ships()
    print(computer_ships)

    print("")
    player_ships = add_player_ships()
    print(player_ships)


    # print("")
    # print("The choice of the computer is:")
    # comp_choice = computer_choice()
    # print(comp_choice)


new_game()