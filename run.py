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
    ships = 0
    while ships < 5:
        x = randint(0,4)
        y = randint(0,4)
        if list[x][y] == "*":
            continue
        for i in range(5):
            ships_row = list[i].count("*")
            ships += ships_row
        list[x][y] = "*"
            
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
    a = computer_board[0].count(".")
    print(a)
    pprint(computer_board)


new_game()