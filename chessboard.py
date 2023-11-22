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
    def __init__(self, screen_width, screen_height): # Class constructor
        self.board = chess.Board()
        self.button = pygame.Rect(screen_width -100, 10, 80, 30)

    def draw(self, screen, game_state):
        self.board.clear()

        # Draw the board
        for row in range(8):
            for col in range(8):
                square_x = col * 100 + 50  # Calculate the x-coordinate of the square's center
                square_y = row * 100 + 50  # Calculate the y-coordinate of the square's center
                pygame.draw.rect(screen, WHITE if (row + col) % 2 == 0 else BLACK, pygame.Rect(col*100, row*100, 100, 100))
                if game_state[row][col] == 'Q':
                    piece_x = square_x - pieces['Q'].get_width() // 2  # Calculate the x-coordinate of the piece's top-left corner
                    piece_y = square_y - pieces['Q'].get_height() // 2  # Calculate the y-coordinate of the piece's top-left corner
                    screen.blit(pieces['Q'], (piece_x, piece_y))

    def draw_button(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.button)
