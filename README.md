## Battleship Game

Battleship game is a Pythonterminal game, which runs in the Code Institute mock terminal on Heroku

In the beginning of the game user is to set three ships on the grid, after that the goal of the game is to 
try and beat the computer by finding and destroying all computers ships before computer finds users.

here is the live version of my project

![image-of-the-project](assets/images/Home%20screen.png)

## How to play

This is a classic battleship game in which user is playing agains computer. First user is asked
to place three ships on the grid that are shown with a simbol "S". After that the game realy begins
and user is asked to try and figure out where are computers ships by imputing coordinates on 
the grid. If the user misses it will get a message and miss will be shown as "X" on the grid, and 
if the user hits it will get the corespodning message. Game is played untill user or computer 
find all the enemies ships.

## Features

Random board generation for the computers ships

- User cannot see the computers ships
- Ships are placed randomly on the grid

User board

- User is able to see the board and place ships on the board
  before the game begins

![image-of-the-board](assets/images/Home%20screen.png)

- Play agains the computer
- Keep score
- Accepts user imput 

Imput validation and error checking 

- If user imputs a value that toes not corespond with the game
  the game will warn him and let him try again
- User must enter the right value provided by example
- User cannot enter the same value twice 

## Data Model 

I decided to use a board calss as a model. The game creates a board that user can see and 
place the ships on, also it creates a random board with ships for the computer. 

Board class stores the board size, the number of ships, the position of the ships and the 
guesses against the board.

## Testing

I have manualy tested the project by doing the following:

- Passed the code trough the PEP8 and confirmed there are errors but only in 
  lenght of some code, no functionality errors.
  I understand that lenght of the code can be adjusted but I didnt want to 
  try and break the code in order not to make serious problems with it.
- Given Invalid inputs: string when numbers are expected, out of bounds inputs, same imput twice
- Tested in my local terminal and the Code Institute Heroku terminal

## Remaining bugs

- Passed the code trough the PEP8 and confirmed there are errors but only in 
  lenght of some code, no functionality errors.
  I understand that lenght of the code can be adjusted but I didnt want to 
  try and break the code in order not to make serious problems with it.

## Validator testing

- Passed the code trough the PEP8 and confirmed there are errors but only in 
  lenght of some code, no functionality errors.
  I understand that lenght of the code can be adjusted but I didnt want to 
  try and break the code in order not to make serious problems with it.

## Deploiment

This project is deployed using the Code Institute mock terminal for Heroku.
Steps of deployment:
- Cloned the depository
- Created the ne Heroku app
- Set the buildbacks to Pythone and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy

## Credits

- Code Institute for the deployment terminal
- https://bigmonty12.github.io/battleship 
- https://www.youtube.com/watch?v=MgJBgnsDcF0
