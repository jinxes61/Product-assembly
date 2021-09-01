import pygame
import sys

def check_event(setting, screen):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def upd_screen(setting, screen):
    screen.fill(setting.bg_color)