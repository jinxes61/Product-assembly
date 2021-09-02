import pygame
import pygame_gui
import sys

def draw_title(setting, screen):
    #Title of the program
    ft = pygame.font.Font("font/consola.ttf", 54)
    text = ft.render("Product Assembly System", True, (220, 220, 220))

    #Set the position
    text_rect = text.get_rect()
    screen_rect = screen.get_rect()
    text_rect.centerx = screen_rect.centerx
    text_rect.y = screen_rect.centery - 100

    screen.blit(text, text_rect)

def check_events(setting, manager, button):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    setting.status = 1

        manager.process_events(event)

def Welcome(setting, screen, img):
    #init clock
    clock = pygame.time.Clock()

    manager = pygame_gui.UIManager(setting.screen_size)
    button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((440, 500), (200, 50)),
                                                 text='Define assembly order',
                                                 manager=manager)

    while setting.status == 0:
        time_delta = clock.tick(60) / 1000.0
        screen.blit(img, (0, 0))
        draw_title(setting, screen)
        
        check_events(setting, manager, button)

        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()

