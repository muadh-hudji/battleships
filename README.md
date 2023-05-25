# Battleships
Battleships is a guessing strategy terminal game developed using python language, the game runs in the Code Institute mock terminal on Heroku.

The Users will challenge the computer to hit all of the oponents ships first to win the game. The boards have a size of five rows and columns. In the boards there is four ships distributed and are invisible for the opponents. 

[Live link](https://battleships-mh.herokuapp.com/)

![Responsice Mockup](https://github.com/muadh-hudji/battleships/blob/0c99c8c4ea84c85ba9110dc487b48acd22612d31/assets/images/battleships_mockup.PNG) 

## How to play
The game begins with a menu of the three options, start new game, read the rules or exit the game. Once the users enter "1" to start a new game, the users will be asked if they wish to pick where the ships will be placed on the board automatically or manually. The game will start after generating two boards with 4 ships distributed on the board manually by the user or randomly by the computer. 

When the game starts, two boards displays out, the user is able to se the ships on their own board but the ships on the computer board will be hidden. The ships on the board has a character of a hashtag "#". When the user types in the row and column they wants to attack, the board will be displayed out with the changes, "X" on the attacked position if it is a miss, asterisk mark "*" if it is a hit.  

The computer will even make a guess generated randomly to attack the users board. 

Whoever hits all the opponent's ships first will win the game. 


## Features

### Existing Features

- __The Menu__
    - The program begins with displaying out game name
    - The Menu of the game contains three options, start a new game, game rules and exit. The user can make a choice between these options by entering 1, 2 or 3.
    - By Entering 2 the user is able to read about how to play the game.

![Game menu](https://github.com/muadh-hudji/battleships/blob/f8dbb3700fdffc037b3844fec53491ce08aaf637/assets/images/game_rules.PNG)     

- __Board generation__
    - When the users starts a new game, the users will be asked if they wants to choose the positions of their own ships by typing any key for yes or n for no.
    - If the users chose to place out the ships manually, they will be asked to enter row and column number in range 0 - 4 for position of four ships. 
    - If the users chose to not place out the ships manually, the computer will make a randomly choice for the positions of the ships.

![Select position](https://github.com/muadh-hudji/battleships/blob/f8dbb3700fdffc037b3844fec53491ce08aaf637/assets/images/place_ships.PNG)         

- __Game boards__
    - When the boards are generated, it will be displayed out on the terminal, the users are able to se their own ships on the board, but not the ships of the computer.
    - The boards consists of five rows and columns and has the index in range 0 - 4.
    - Next step, the users will be asked to enter the position they wants to attack by typing numbers in range 0 - 4 for row and column.

![Game boards](https://github.com/muadh-hudji/battleships/blob/f8dbb3700fdffc037b3844fec53491ce08aaf637/assets/images/populated_board.PNG) 

- __Input validation__
    - All users inputs are validated, this when users makes inputs to pick an option of the menu, answering if they wants to place out the ships manually, when they makes input for position where the ships will be placed and when they entering the position they wants to attack.
    - The inputs for attacking or placing ships has to be in number between 0 - 4, numbers outside this range is not approved. The user cannot either enter same position twice.

![Invalid input](https://github.com/muadh-hudji/battleships/blob/fe96184115fbb2736173b8bc70cf506a2c49ecae/assets/images/invalid_input.PNG)   

![Invalid input](https://github.com/muadh-hudji/battleships/blob/fe96184115fbb2736173b8bc70cf506a2c49ecae/assets/images/same_postion.PNG) 

- __End of the game__
    - After every round the result will be displayed with the boards, if one player makes a hit the score will be incremented with one.
    - The first player who hits all of the four ships wins the game.
    - When the game is finished, the users will get back to the game menu to make a choice again.

![End](https://github.com/muadh-hudji/battleships/blob/fe96184115fbb2736173b8bc70cf506a2c49ecae/assets/images/end_result.PNG)     

### Future Features
- Give the user the option to select the size of the board and number of ships.

## Data Model
I decided to build the game by several functions, the main functions will call other functions to generate the lists of the board, ship positions, attack positions, display the boards, integrate the lists etc...

The functions created for the game:
- board  - Generates mutliple lists that considered as the board
- add ships auto - Generates data for the position of the ships
- add data manually  - Takes input from the user for ships position or attack position
- validate data  - Validates the data input from the user
- populate board   - Adds the ships on the board
- computer choice  - Generate randomly numbers for attack position
- display board  - Displays out the boards
- play game  - Main function when a game is created
- new game  - Main function to generate a new game 
- main function  - Main function contains the menu 

## Testing
The game has been manually tested to ensure that everything is working as it should:
- Invalid inputs:
    - Strings when numbers input expected.
    - Numbers out of required range.
    - Same input twice.
    - Uppercase letters when lowercase expected.
    - Other inputs when specific letters or numbers are expected.
- The game has been tested by playing several times to check that everything is working as it is expected. And even to be secure that when the user starts a new game no older data from previous game are still there.
- Test is made in the local terminal and in Heroku

### Bugs
- The input from the user when they enter "N" in capital letter for the question if they want to place out the ships manually, didn't work well because the if statement is expecting "n" in small letter. The problem is solved by using lower function to convert the input to lowercase.
- When the boards was printed out by using pprint, the boards was displayed out with the comma and the square brackets. In order to have the boards displayed without any more characters than the content, i have created a function to loop through the boards and print out one row at the time.
- Add auto ships function sometimes added 3 or 5 ships because the if statement wasn't directly in the while loop, to solve the problem i added a for loop to check the data and the result of the validation is stored in a variabel, which in next step outside the for loop goes in an if statement to check if the data is approved.

### Remaining Bugs
- There are no known bugs remains.

### Validator
- PEP8
    - No errors were returned from pep8ci.herokuapp.com

## Deployment
This project was deployed using Code institute's mock terminal for Heroku.

- Steps for deployment
    - Commit and push the final code to Github
    - On Heroku site, create a new app
    - Give the app an unique name
    - Under tab settings, add a Config Vars key "PORT" value "8000"
    - Then click on "Add buildpack" and select "heroku/python"
    - Add another buildpack and select "heroku/nodejs"
    - Underneath tab "Deploy" connect to Github account
    - Select the repository
    - Finally click on "Deploy Branch"

### Copy Clone
- The project can be cloned by following steps:
    - Navigate in Github after the repository for the project "battleships"
    - On the top of the page click on the green button "<>Code"
    - Underneath Local tab, click on "HTTPS"
    - Chose to clone the project by either the address, "Open with GitHub desktop" or download as a ZIP-file

### Create a new Fork 
- Create new fork by following steps:
    - Navigate in Github after the repository for the project "battleships"
    - On the top of the page on the right side, click on "Fork"
    - Select "Create new fork"

## Credits
- Ide of the game from "Ultimate Battleships"
- Details about the game from Wikipedia
- Python terminal by Code Institute 
- Validator pep8ci.herokuapp.com
