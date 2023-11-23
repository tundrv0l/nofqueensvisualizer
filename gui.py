'''----------------- 
# Author: Parker Clark
# Date: 11/21/2023
# Description: A driver for the gui.  
-----------------'''

import chess
import pygame
import tkinter as tk
from tkinter import messagebox

#---Colors---#
WHITE = (251, 235, 193)
BLACK = (157, 108, 62)

#---Queen container---#
pieces = {}
pieces["Q"] = pygame.image.load("images/bQ.png")

class ChessBoard:
    """
        A class that represents a chessboard. The chessboard is represented by an 8x8 grid.
    """

    def __init__(self, screen_width: int, screen_height: int):
        """
        Parameterized constructor for the ChessBoard class.
        """
        self.board = chess.Board()
        self.game_state = [['' for _ in range(8)] for _ in range(8)] # Initialize an empty game state

    def draw(self, screen: pygame.Surface, game_state: list) -> None:
        """
        Function that draws the chessboard. Takes the game state and checks it against the board to see if a queen is present. If it is, then it draws the queen on the board.

        Parameters
        ----------
        self: SELF
            An instance of the ChessBoard class.
        
        screen: SURFACE
            The surface to draw on.
        
        game_state: LIST
            The current game state to draw.
        """

        # Clear the screen
        self.board.clear()

        # Draw the board
        for row in range(8):
            for col in range(8):
                square_x = col * 100 + 50  # Calculate the x-coordinate of the square's center
                square_y = row * 100 + 50  # Calculate the y-coordinate of the square's center
                pygame.draw.rect(screen, WHITE if (row + col) % 2 == 0 else BLACK, pygame.Rect(col*100, row*100, 100, 100)) # Draw the squares
                if game_state[row][col] == 'Q':
                    piece_x = square_x - pieces['Q'].get_width() // 2  # Calculate the x-coordinate of the piece's top-left corner
                    piece_y = square_y - pieces['Q'].get_height() // 2  # Calculate the y-coordinate of the piece's top-left corner
                    screen.blit(pieces['Q'], (piece_x, piece_y))

    def make_empty_game_state(self):
        self.game_state = [['' for _ in range(8)] for _ in range(8)]

class MessageBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

