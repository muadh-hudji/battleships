# Battleships
Battleships is a guessing strategy terminal game developed by python, the game runs in the Code Institute mock terminal on Heroku.

The Users will challenge the computer to hit all of the oponents ships first to win the game. The boards have a size of five rows and columns. In the boards there is four ships distributed and are invisible for the opponents. 

[Live link](https://battleships-mh.herokuapp.com/)

## How to play
The game begins with a menu of the three options, start new game, read the rules or exit the game. Once the users enter "1" to start a new game, the users will be asked if they wish to pick where the ships will be placed on the board automatically or manually. The game will start after generating two boards with 4 ships distributed on the board manually by the user or randomly by the computer. 

When the game starts, two boards displays out, the user is able to se the ships on their own board but the ships on the computer board will be hidden. The ships on the board has a character of a hashtag "#". When the user types in the row and column they wants to attack the board will be displayed out with the changes, "X" on the attacked position if it is a miss, asterisk mark "*" if it is a hit.  

The computer will even make a guess generated randomly to attack the users board. 

Whoever hits all the opponent's ships first will win the game. 


## Features

### Existing Features

- __The Menu__
    - The program begins with displaying out game name
    - The Menu of the game contains three options, start a new game, game rules and exit. The user can make a choice between these options by entering 1, 2 or 3.
    - By Entering 2 the user is able to read about how to play the game.

![Responsice Mockup](https://github.com/muadh-hudji/battleships/blob/f8dbb3700fdffc037b3844fec53491ce08aaf637/assets/images/game_rules.PNG)     

- __Board generation__
    - When the users starts a new game, the users will be asked if they wants to chosse the position of own ships by entering any key for yes or n for no.
    - If the users chose to place out the ships manually, they will be asked to enter row and column number in range 0 - 4 for position of four ships. 
    - If the users chose to not place out the ships manually, the computer will make a randomly choice of the positions of the ships.

![Responsice Mockup](https://github.com/muadh-hudji/battleships/blob/f8dbb3700fdffc037b3844fec53491ce08aaf637/assets/images/place_ships.PNG)         

- __Game boards__
    - When the boards are generated, it will be displayed out on the terminal, the users are able to se their own ships on the board, but not the ships of the computer.
    - The boards consists of five rows and columns and has the index in range 0 - 4.
    - Next step, the users will be asked to enter the position they wants to attack by typing numbers in range 0 - 4 for row and column

![Responsice Mockup](https://github.com/muadh-hudji/battleships/blob/f8dbb3700fdffc037b3844fec53491ce08aaf637/assets/images/populated_board.PNG) 

- __Input validation__
    - All users inputs are validated, this when users makes inputs to pick an option of the menu, answering if they wants to place out the ships manually, when they makes input for position where the ships will be placed and when they entering the position they wants to attack.
    - The play game input has to be in number between 0 - 4, numbers outside this range is not approved. The user cannot either enter same position twice.

![Responsice Mockup](https://github.com/muadh-hudji/battleships/blob/fe96184115fbb2736173b8bc70cf506a2c49ecae/assets/images/invalid_input.PNG)   

![Responsice Mockup](https://github.com/muadh-hudji/battleships/blob/fe96184115fbb2736173b8bc70cf506a2c49ecae/assets/images/same_postion.PNG) 

- __End of the game__
    - After every round the result will be displayed with the boards, if one player makes a hit the score will be incremented with one.
    - The first player who hits all of the four ships wins the game.
    - When the game is finished, the users will get back to the game menu to make a choice again.

![Responsice Mockup](https://github.com/muadh-hudji/battleships/blob/fe96184115fbb2736173b8bc70cf506a2c49ecae/assets/images/end_result.PNG)     

### Future Features
- Let the user to choose the size of the board and number of ships

## Data Model


## Testing

### Bugs

### Remaining Bugs

### Validator


## Deployment


## Credits
