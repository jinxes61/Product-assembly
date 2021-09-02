import pygame
import pygame_gui
from sets import Settings
import function as fun

def main():
    #init
    pygame.init()
    setting = Settings()

    #init screen
    screen = pygame.display.set_mode(setting.screen_size)
    pygame.display.set_caption('Product assembly')
    img = pygame.image.load("img/BG.bmp")

    #init pygame_gui manager
    #manager = pygame_gui.UIManager(setting.screen_size)


    while(True):
        screen.blit(img, (0, 0))
        fun.solve(setting, screen, img)

if __name__ == "__main__":
    main()