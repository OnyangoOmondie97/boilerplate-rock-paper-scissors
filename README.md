# Rock, Paper, Scissors Challenge

Welcome to the Rock, Paper, Scissors challenge! In this project, you will be creating a program to play Rock, Paper, Scissors against four different bots. The goal is to have your program win at least 60% of the games in each match.

## Getting Started

1. **Import the Project on Replit:**
   - Start by importing the project on Replit.

2. **Configure .replit:**
   - Open the .replit window.
   - Select "Use run command" and click the "Done" button.

3. **Coding in RPS.py:**
   - In the file `RPS.py`, you are provided with a function called `player`. It takes a string argument describing the last move of the opponent ("R", "P", or "S").
   - Your task is to return a string representing the next move for your program to play ("R", "P", or "S").
   - Note: The player function receives an empty string for the first game in a match.

4. **Strategies and Multiple Bots:**
   - To defeat all four opponents, your program may need multiple strategies that change depending on the plays of the opponent.

## Development Guidelines

- **Do Not Modify `RPS_game.py`:**
  - Write all your code in `RPS.py`.

- **Testing with `main.py`:**
  - Use `main.py` to test your code.
  - The `play` function takes four arguments: two players, the number of games to play, and an optional argument for verbose output.

    ```python
    play(player1, player2, num_games[, verbose])
    ```

  - Example: `play(player, quincy, 1000, verbose=True)`

## Development Setup

- The file `main.py` imports the game function and bots from `RPS_game.py`.
- To test your code, play a game with the `play` function.

## Testing

- Unit tests are in `test_module.py`.
- Uncomment the last line in `main.py` to run tests automatically when hitting the "run" button.

---

**README.md:**

## Instructions

1. Import the project on Replit.
2. Configure .replit to use the run command.
3. Develop your Rock, Paper, Scissors strategy in `RPS.py`.
4. Use `main.py` for testing your code with the `play` function.
5. Aim to win at least 60% of games against four different bots.
6. Do not modify `RPS_game.py`.
7. Explore multiple strategies depending on opponent plays.

Feel free to check unit tests in `test_module.py` and run them using `main.py`.

Best of luck with your Rock, Paper, Scissors program!
