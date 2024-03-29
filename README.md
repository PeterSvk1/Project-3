# Project 3: My battleship game

This is simple game where you can play against the computer. Player needs to hit all ships in order to defeat computer.
I hope users will enjoy this functionality and and find it relaxing to play, users have nothing to lose other than their mind if they lose too many times.

![Responsice Mockup](https://github.com/PeterSvk1/Project-3/blob/main/views/ui.jpg)

## How to play
When player enters his name game will ask him how big board he wants to make.
Battlefield will be genrated according to the player's input and ships will be randomly generated.
Player is able to see his ships and computer ships are hidden.
player ship = @
miss/guess = X
hit = *

The player and computer takes turn untill one of them loses all ships.
Winner is the one who has atleast 1 ship left on the battlefield.

## Features 
### Existing Features

- Player is asked to enter his name
- Player can choose size of the board
- Game will generate board according to players wishes
- Ships are randomly generated on the board

![Responsice Mockup](https://github.com/PeterSvk1/Project-3/blob/main/views/start.jpg)

- Play against computer
- accepts user imputs
- Maintains scores
- tells player if he missed or not

![Responsice Mockup](https://github.com/PeterSvk1/Project-3/blob/main/views/score.jpg)

- Input validation and error checking
- you cannot enter wrong coordinations or use letters
- you cannot enter same coordinations twice
- you can restart the game

![Responsice Mockup](https://github.com/PeterSvk1/Project-3/blob/main/views/inputs.jpg)

### Future features
- Add bigger ships than 1x1
- Player can possition ships on the board
- player can change number of ships

## Data model
I decided to to use BattleshipGame class as my model. The game creates one instance of BattleshipGame class which can hold the players board
and computer board.

The BattleshipGame class stores the board size, the number of ships, the possition of the ships, the guesses on the board, and small details
like players name, players board, computer board, scores.

The class also has methods to help play game, such as print out current board after each turn.

## Testing
I have manually tested this project by doing following:
- passed code though a PEP8 linter and confirmed there are no problems
- Given invalid inputs: same input twice, numbers are expected and such
- Tested in local terminal and the Code intitute heroku terminal

## Bugs
Solved bugs:
- my validate function wasnt printed out and I managed to fix it by adding
        if (x, y) in p:
            print("Already used coordinates. Try again.")
            return False
        return 0 <= x < r and 0 <= y < c

## Bugs to fix
- Hopefully none

## Validator tesing
- PEP8 
     - no errors were returned from PEP8online.com
![Responsice Mockup](https://github.com/PeterSvk1/Project-3/blob/main/views/pep8.jpg)