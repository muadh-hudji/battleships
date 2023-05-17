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
    game_board = add_ships(empty_game_board)    
    return game_board

def add_ships(list):
    """
    Add 4 ships in the board by choosing a random index
    """
    ships = 4
    while ships != 0:
        x = randint(0,4)
        y = randint(0,4)
        if list.count("*") != 0:
            list[x][y] = "*"
            ships -= 1
    return list

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
    pprint(computer_board)


new_game()