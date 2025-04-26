import pygame
from sudoku_generator import generate_sudoku
from cell import Cell


WIDTH = 600
HEIGHT = 600
BOARD_ROWS = 9
BOARD_COLS = 9
SQUARE_SIZE = WIDTH // BOARD_COLS




class Board:
   def __init__(self, width, height, screen, difficulty):
       self.width = width
       self.height = height
       self.screen = screen
       self.difficulty = difficulty
       self.board = generate_sudoku(9, self.get_removed_cells(difficulty))
       self.cells = []
       for row in range(9):
           cell_row = []
           for col in range(9):
               value = self.board[row][col]
               cell_row.append(Cell(value, row, col, screen))
           self.cells.append(cell_row)


       self.selected_cell = None
       self.original_board = [row[:] for row in self.board]
