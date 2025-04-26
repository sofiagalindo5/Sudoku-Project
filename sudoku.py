import pygame
import sys
from board import Board
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 700
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER = (170, 170, 170)
FONT = pygame.font.SysFont("Arial", 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


# Button class for menus
class Button:
   def __init__(self, text, x, y, width, height):
       self.text = text
       self.rect = pygame.Rect(x, y, width, height)
       self.color = BUTTON_COLOR
       self.hover_color = BUTTON_HOVER


   def draw(self, screen):
       mouse_pos = pygame.mouse.get_pos()
       if self.rect.collidepoint(mouse_pos):
           pygame.draw.rect(screen, self.hover_color, self.rect)
       else:
           pygame.draw.rect(screen, self.color, self.rect)
       text_surf = FONT.render(self.text, True, (0, 0, 0))
       text_rect = text_surf.get_rect(center=self.rect.center)
       screen.blit(text_surf, text_rect)


   def is_clicked(self, event):
       return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
