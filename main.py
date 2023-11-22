'''----------------- 
# Author: Parker Clark
# Date: 11/21/2023
# Description: A driver for the N of Queens Problem.  
-----------------'''

import pygame
from chessboard import ChessBoard
import random

""" def is_safe(board: ChessBoard , row: int, col: int)->bool:
    # Check row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True """


def n_queens_solution(n, board=[], row=0):
    if row == n:
        return [board]


    solutions = []
    for col in range(n):
        if all(col != c and row-r != abs(col-c) for r, c in enumerate(board)):
            for result in n_queens_solution(n, board + [col], row + 1):
                solutions.append(result)

    return solutions


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))

    clock = pygame.time.Clock()
    pygame.display.set_caption("N of Queens")

    chessboard = ChessBoard()  # Create an instance of the ChessBoard class

    done = False

    game_state = [['' for _ in range(8)] for _ in range(8)]

    # update the board state with n of queens
    solutions = n_queens_solution(8)
    if solutions:
        solution = random.choice(solutions)
        for row, col in enumerate(solution):
            game_state[row][col] = 'Q'

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
        chessboard.draw(screen, game_state)  # Draw the chessboard with updated game state
        pygame.display.flip()  # Update the display
        
    pygame.quit()

if __name__=='__main__':
    main()
