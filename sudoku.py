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

def game_loop(difficulty):
   board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, difficulty)


   reset_button = Button("Reset", 50, 620, 150, 50)
   restart_button = Button("Restart", 225, 620, 150, 50)
   exit_button = Button("Exit", 400, 620, 150, 50)


   running = True
   while running:
       screen.fill((255, 255, 255))
       board.draw()
       reset_button.draw(screen)
       restart_button.draw(screen)
       exit_button.draw(screen)


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()


           if event.type == pygame.MOUSEBUTTONDOWN:
               pos = pygame.mouse.get_pos()
               if pos[1] < 600:
                   clicked = board.click(pos[0], pos[1])
                   if clicked:
                       board.select(clicked[0], clicked[1])
               if reset_button.is_clicked(event):
                   board.reset_to_original()
               if restart_button.is_clicked(event):
                   main_menu()
               if exit_button.is_clicked(event):
                   pygame.quit()
                   sys.exit()


           if event.type == pygame.KEYDOWN:
               if board.selected_cell:
                   row, col = board.selected_cell
                   if event.key == pygame.K_1:
                       board.sketch(1)
                   if event.key == pygame.K_2:
                       board.sketch(2)
                   if event.key == pygame.K_3:
                       board.sketch(3)
                   if event.key == pygame.K_4:
                       board.sketch(4)
                   if event.key == pygame.K_5:
                       board.sketch(5)
                   if event.key == pygame.K_6:
                       board.sketch(6)
                   if event.key == pygame.K_7:
                       board.sketch(7)
                   if event.key == pygame.K_8:
                       board.sketch(8)
                   if event.key == pygame.K_9:
                       board.sketch(9)
                   if event.key == pygame.K_RETURN:
                       board.place_number(board.cells[row][col].sketched_value)
       board.update_board()
       if board.is_full():
           if board.check_board():
               win_screen()
           else:
               lose_screen()


       pygame.display.update()


if __name__ == "__main__":
   main_menu()
