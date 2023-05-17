from pprint import pprint

def board():
    """
    Creates game board
    """
    size = 5
    game_board = []
    for i in range(size):
        list = []
        for x in range(size):
            list.append(".")
        game_board.append(list)    
    return game_board


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