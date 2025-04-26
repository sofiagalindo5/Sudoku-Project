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

   def get_removed_cells(self, difficulty):
      if difficulty == "easy":
         return 30
      elif difficulty == "medium":
         return 40
      elif difficulty == "hard":
         return 50
      else:
         return 30

   def draw(self):
       for row in self.cells:
           for cell in row:
               cell.draw()

       for i in range(BOARD_ROWS + 1):
           thickness = 6 if i % 3 == 0 else 1
           pygame.draw.line(self.screen, (0, 0, 0), (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), thickness)
           pygame.draw.line(self.screen, (0, 0, 0), (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), thickness)

   def select(self, row, col):
       for r in self.cells:
           for cell in r:
               cell.deselect()
       self.cells[row][col].select()
       self.selected_cell = (row, col)

   def click(self, x, y):
       if x < WIDTH and y < HEIGHT:
           row = int(y // SQUARE_SIZE)
           col = int(x // SQUARE_SIZE)
           return (row, col)
       return None
