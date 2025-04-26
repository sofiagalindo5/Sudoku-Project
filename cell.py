import pygame


class Cell:
   def __init__(self, value, row, col, screen):
       self.value = value
       self.sketched_value = 0
       self.row = row
       self.col = col
       self.screen = screen
       self.selected = False


   def set_cell_value(self, value):
       self.value = value


   def set_sketched_value(self, value):
       self.sketched_value = value

   def draw(self):
       SQUARE_SIZE = 600 // 9
       BG_COLOR = (255, 255, 245)
       LINE_COLOR = (245, 152, 66)
       CROSS_COLOR = (66, 66, 66)
       RED = (255, 0, 0)


       x = self.col * SQUARE_SIZE
       y = self.row * SQUARE_SIZE


       pygame.draw.rect(self.screen, BG_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))
       pygame.draw.rect(self.screen, LINE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE), 1)


       font = pygame.font.SysFont("Arial", 40)
       if self.value != 0:
           text = font.render(str(self.value), True, CROSS_COLOR)
           self.screen.blit(text, (x + SQUARE_SIZE/2 - text.get_width()/2, y + SQUARE_SIZE/2 - text.get_height()/2))
       elif self.sketched_value != 0:
           sketched_font = pygame.font.SysFont("Arial", 20)
           text = sketched_font.render(str(self.sketched_value), True, (0, 0, 0))
           self.screen.blit(text, (x + 5, y + 5))


       if self.selected:
           pygame.draw.rect(self.screen, RED, (x, y, SQUARE_SIZE, SQUARE_SIZE), 3)
