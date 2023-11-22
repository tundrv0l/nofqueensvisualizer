'''----------------- 
# Author: Parker Clark
# Date: 11/21/2023
# Description: A driver for chess board.  
-----------------'''

import chess
import pygame


WHITE = (251, 235, 193)
BLACK = (157, 108, 62)

pieces = {}
pieces["Q"] = pygame.image.load("images/bQ.png")

class ChessBoard:
    def __init__(self): # Class constructor
        self.board = chess.Board()

    def draw(self, screen, game_state):

        self.board.clear()

        # Draw the board
        for row in range(8):
            for col in range(8):
                pygame.draw.rect(screen, WHITE if (row + col) % 2 == 0 else BLACK, pygame.Rect(col*100, row*100, 100, 100))
                if game_state[row][col] == 'Q':
                    screen.blit(pieces['Q'], (col * 100, row * 100))

"""         # Draw the queen piece
        screen.blit(pieces["Q"], (3 * 100, 3 * 100)) """
