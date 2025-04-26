import random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):

        self.row_length = row_length  # 9 for a standard Sudoku
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(self.row_length)] for _ in range(self.row_length)]  # initialize the board as a 2D list of zero
        self.box_size = int(self.row_length ** 0.5) # For 9x9 Sudoku, the size of each box is 3

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))

    def valid_in_row(self, row, num):
        # Returns True if num not in the given row.
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Returns True if num not in the given column.
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        # Returns True if num is not in the 3x3 box that starts at (row_start, col_start)
        for i in range(self.box_size):
            for j in range(self.box_size):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        # Checks if placing num at (row, col) is allowed.
        # We must check row, column, and the 3x3 box.
        box_row_start = row - row % self.box_size
        box_col_start = col - col % self.box_size
        return (self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(box_row_start, box_col_start, num))

    def fill_box(self, row_start, col_start):
        # Randomly fills the 3x3 box with numbers 1 to 9 that are not repeated.
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        for i in range(self.box_size):
            for j in range(self.box_size):
                self.board[row_start + i][col_start + j] = nums[self.box_size * i + j]

    def fill_diagonal(self):
        # Fill the three diagonal boxes.
        for i in range(0, self.row_length, self.box_size):
            self.fill_box(i, i)

    def fill_remaining(self, i=0, j=0):
        # If we reach the end of the board, stop
        if i == self.row_length - 1 and j == self.row_length:
            return True
        if j == self.row_length:
            i += 1
            j = 0
        if i >= self.row_length:
            return True

        if self.board[i][j] != 0:
            return self.fill_remaining(i, j + 1)

        for num in range(1, self.row_length + 1):
            if self.is_valid(i, j, num):
                self.board[i][j] = num
                if self.fill_remaining(i, j + 1):
                    return True
                self.board[i][j] = 0  # Undo if it didn't lead to solution

        return False

    def fill_values(self):
        # Constructs a full solution board.
        self.fill_diagonal()  # Step 1: fill the three diagonal boxes.
        self.fill_remaining()  # Step 2: fill the rest of the board

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            # Only remove if the cell is not already empty.
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1




def generate_sudoku(size, removed):

    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    return sudoku.get_board()












