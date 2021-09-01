import pygame
from sets import Settings
import function as fun

def main():
    #init
    pygame.init()
    setting = Settings()

    #init screen
    screen = pygame.display.set_mode(setting.screen_size)
    pygame.display.set_caption('Product assembly')

    #init clock
    clock = pygame.time.Clock()

    while(True):
        clock.tick(120)
        fun.check_event(setting, screen)
        fun.upd_screen(setting, screen)


if __name__ == "__main__":
    main()