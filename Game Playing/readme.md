# Red-Blue Nim Game

This project is a Python-based implementation of a modified version of the classic Nim game called "Red-Blue Nim" played against a human player. In this game, there are two piles of marbles: red and blue. Players take turns removing marbles from one of the piles. If a player takes the last marble from either pile, they win the game, and the winner's score is calculated based on the number of remaining marbles (2 points per remaining red marble and 3 points per remaining blue marble).

## Usage

To play Red-Blue Nim, use the following command line invocation:

```
red_blue_nim.py <num-red> <num-blue> <first-player> <depth>
```

- `<num-red>` and `<num-blue>` are required and represent the initial number of red and blue marbles, respectively.
- `<first-player>` can be one of the following:
  - `computer`: Computer starts the game followed by the human player (default option if not specified).
  - `human`: Human starts the game followed by the computer player.
- `<depth>` is only used if depth-limited MinMax search with alpha-beta pruning is implemented (Extra Credit).

## Gameplay

- On the computer's turn, the program uses MinMax with Alpha-Beta Pruning to determine the best move and performs the move.
- On the human's turn, the program prompts the human player to enter their move (pile selection and number of marbles to remove) and performs the move.
- The game alternates between these turns until one of the players runs out of either red or blue marbles.
- Once the game ends, the program calculates the winner and their final score and displays it to the user.
