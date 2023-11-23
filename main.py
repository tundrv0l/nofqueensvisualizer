'''----------------- 
# Author: Parker Clark
# Date: 11/21/2023
# Description: A driver for the N of Queens Problem.  
-----------------'''

import pygame
from gui import ChessBoard, MessageBox
from solution import *


#---Global Variables---#
screen_width: int = 800
screen_height: int = 800

#---Instantiate the GUI classes---#
greeting_box: MessageBox = MessageBox()
chessboard: ChessBoard = ChessBoard(screen_width, screen_height)  # Create an instance of the ChessBoard class

def main():
    #--- Initialize pygame and create a window---#
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("N of Queens")
    done = False # Controls the game loop

    #---Create a solution generator---#
    solutions = n_queens_solution(8)
    if solutions:
        solution_generator = make_solution_generator(solutions)

    #---Main game loop---#
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True # Exit the game loop
            elif event.type == pygame.KEYDOWN:  # A key has been pressed
                if event.key == pygame.K_SPACE: #Reset the board upon spacebar press
                    solution_generator = make_solution_generator(solutions) # Create a new solution generator for a new solution
                    chessboard.make_empty_game_state() # Reset the game state
        try:
            col, row = next(solution_generator) # Get the next queen position
            chessboard.game_state[row][col] = 'Q' # Update the game state
            pygame.time.wait(500) # Wait 500 ms for the next queen position to be displayed
        except StopIteration:
            pass # No more solutions

        #---Draw the chessboard---#
        chessboard.draw(screen, chessboard.game_state)  # Draw the chessboard with updated game state
        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__=='__main__':
    #---Display a greeting message---#
    greeting_box.show_info("N of Queens", "Welcome to N of Queens! Press the space bar to generate a new solution.")
    main()
