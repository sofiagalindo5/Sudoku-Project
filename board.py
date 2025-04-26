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

   def clear(self):
       if self.selected_cell:
           row, col = self.selected_cell
           if self.original_board[row][col] == 0:
               self.cells[row][col].set_cell_value(0)
               self.cells[row][col].set_sketched_value(0)


   def sketch(self, value):
       if self.selected_cell:
           row, col = self.selected_cell
           self.cells[row][col].set_sketched_value(value)


   def place_number(self, value):
       if self.selected_cell:
           row, col = self.selected_cell
           if self.original_board[row][col] == 0:
               self.cells[row][col].set_cell_value(value)
               self.cells[row][col].set_sketched_value(0)


   def reset_to_original(self):
       for row in range(BOARD_ROWS):
           for col in range(BOARD_COLS):
               self.cells[row][col].set_cell_value(self.original_board[row][col])
               self.cells[row][col].set_sketched_value(0)


   def is_full(self):
       for row in self.cells:
           for cell in row:
               if cell.value == 0:
                   return False
       return True


   def update_board(self):
       for row in range(BOARD_ROWS):
           for col in range(BOARD_COLS):
               self.board[row][col] = self.cells[row][col].value


   def find_empty(self):
       for row in range(BOARD_ROWS):
           for col in range(BOARD_COLS):
               if self.cells[row][col].value == 0:
                   return (row, col)
       return None


   def check_board(self):
       for i in range(BOARD_ROWS):
           row_vals = []
           col_vals = []
           for j in range(BOARD_COLS):
               row_val = self.cells[i][j].value
               col_val = self.cells[j][i].value
               if row_val in row_vals or col_val in col_vals:
                   return False
               if row_val != 0:
                   row_vals.append(row_val)
               if col_val != 0:
                   col_vals.append(col_val)


       for box_row in range(0, BOARD_ROWS, 3):
           for box_col in range(0, BOARD_COLS, 3):
               box_vals = []
               for r in range(3):
                   for c in range(3):
                       val = self.cells[box_row + r][box_col + c].value
                       if val in box_vals:
                           return False
                       if val != 0:
                           box_vals.append(val)
       return True





