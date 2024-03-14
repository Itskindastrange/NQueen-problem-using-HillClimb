# NQueen-problem-using-HillClimb
This repository contains Python code that implements the Hill Climbing algorithm to solve the N-Queens problem. The N-Queens problem asks how to place N chess queens on an N x N chessboard such that no two queens can attack each other (diagonally, horizontally, or vertically).

This repository contains Python code that implements the Hill Climbing algorithm to solve the N-Queens problem. The N-Queens problem asks how to place N chess queens on an N x N chessboard such that no two queens can attack each other (diagonally, horizontally, or vertically).

Key Features:

Implements the Hill Climbing algorithm for an efficient search to find solutions.
Includes functions to:
Generate random initial board configurations.
Calculate the number of attacking queen pairs in a given state.
Find all valid neighboring states by moving one queen within her column.
Visually represent the solution board using Matplotlib.
Allows user input for the number of queens (board size).
How to Use:

Clone this repository.
Install required libraries (random, matplotlib).
Run the script (python NQueen.py).
Enter the desired number of queens (e.g., 4 or 8) when prompted.
The script will:
Find a solution using the Hill Climbing algorithm.
Print the textual representation of the board configuration.
Display a visual representation of the solution board.
Potential Improvements (Optional):

Explore allowing sideways moves for queens during neighbor generation.
Implement a probability-based mechanism to escape plateaus in the Hill Climbing search.
Feel free to contribute or modify this code!

Note: This Hill Climbing approach may not guarantee the globally optimal solution (no attacking pairs) for larger boards, but it offers a good solution with a high success rate.
