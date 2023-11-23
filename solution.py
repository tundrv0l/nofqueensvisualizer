'''----------------- 
# Author: Parker Clark
# Date: 11/22/2023
# Description: Houses the solution to the N of Queens Problem. 
-----------------'''

import random

def n_queens_solution(n: int, board: list = [], row: int = 0)-> list:
    """
    A function that finds a solution to the N of Queens Problem. There are no two queens in the same row, column, or diagonal.
    For 8 Queens, there are a possible 92 solutions. Our base case is when the row is equal to the number of queens, n.
    Our recursive case is when the row is less than the number of queens, n. We check if the column is not equal to the column. 

    Parameters
    ----------
    n: INT
        The number of queens.
    
    board[]: LIST
        A list of the board positions.
    
    row: INT
        The current row.
    
    Returns
    -------
    solutions: LIST
        A list of the solutions generated for the N of Queens Problem.    
    """

    if row == n: # Base case, when the row is equal to the number of queens, n
        return [board] 

    solutions = []
    for col in range(n): # Recursive case, when the row is less than the number of queens, n
        if all(col != c and row-r != abs(col-c) for r, c in enumerate(board)):
            for result in n_queens_solution(n, board + [col], row + 1):
                solutions.append(result) # Add the solution to the list of solutions, for 8 Queens

    return solutions


def make_solution_generator(solutions: list)-> list:
    """
    A function that makes our 'solution_generator'. This is the actual structure that will be displayed on the chess board from a list of many other solutions.
    We initially pick a random solution from the list passed in, and then enumerae over the chosen solution. 
    This allows for the elements to be displayed on the chess board in real time as the solution is being generated.

    Parameters
    ----------
    solutions: LIST
        A list of the board positions.

    Returns
    -------
    solution_generator: LIST
        A list of the solutions generated for the N of Queens Problem.    
    """

    solution = random.choice(solutions) # Pick a random solution from the list of solutions
    solution_generator = (col for col in enumerate(solution)) # Enumerate over the solution
    return solution_generator