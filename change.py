import pygame
import pygame_gui
import sys

def check_events(setting, manager):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def ChangePart(setting, screen, img):
     #init clock
    clock = pygame.time.Clock()

    manager = pygame_gui.UIManager(setting.screen_size)

    while setting.status == 2:
        time_delta = clock.tick(60) / 1000.0
        screen.blit(img, (0, 0))        
        
        check_events(setting, manager)

        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()
    return