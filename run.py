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
    print("Players Ships populated in following places")
    player_ships = add_player_ships()
    print(player_ships)

    print("")
    print("Computers Ships populated in following places")
    computer_ships = add_computer_ships()
    print(computer_ships)

    print("")
    print("The choice of the computer is:")
    comp_choice = computer_choice()
    print(comp_choice)


new_game()