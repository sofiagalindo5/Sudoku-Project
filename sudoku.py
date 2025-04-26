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



def main_menu():
   easy_button = Button("Easy", 200, 250, 200, 50)
   medium_button = Button("Medium", 200, 350, 200, 50)
   hard_button = Button("Hard", 200, 450, 200, 50)


   while True:
       screen.fill((255, 255, 255))
       title = FONT.render("Select Difficulty", True, (0, 0, 0))
       screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))


       easy_button.draw(screen)
       medium_button.draw(screen)
       hard_button.draw(screen)


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if easy_button.is_clicked(event):
               game_loop("easy")
           if medium_button.is_clicked(event):
               game_loop("medium")
           if hard_button.is_clicked(event):
               game_loop("hard")


       pygame.display.update()


def win_screen():
   screen.fill((255, 255, 255))
   font = pygame.font.SysFont("arial", 60)
   text = font.render("You Win!", True, (0, 0, 0))
   screen.blit(text, (WIDTH//2 - text.get_width()//2, 200))


   exit_button = Button("Exit", WIDTH//2 - 75, 400, 150, 50)
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if exit_button.is_clicked(event):
               pygame.quit()
               sys.exit()


       exit_button.draw(screen)
       pygame.display.update()


def lose_screen():
   screen.fill((255, 255, 255))
   font = pygame.font.SysFont("Arial", 60)
   text = font.render("Try Again!", True, (0, 0, 0))
   screen.blit(text, (WIDTH//2 - text.get_width()//2, 200))


   restart_button = Button("Restart", WIDTH//2 - 75, 400, 150, 50)


   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if restart_button.is_clicked(event):
               main_menu()


       restart_button.draw(screen)
       pygame.display.update()
