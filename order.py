import pygame
import pygame_gui
import sys

def check_events(setting, manager, push_button, pop_button, text_in, finish):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pop_button:
                    if len(setting.part) > 0:
                        del setting.part[-1]

                if event.ui_element == push_button:
                    if len(setting.part) < 9 and len(setting.temp_text) > 0:
                        setting.part.append(setting.temp_text)
                        print(setting.temp_text)

                if event.ui_element == finish:
                    if len(setting.part) > 0:
                        setting.status = 2

            if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == text_in:
                    setting.temp_text = event.text


        manager.process_events(event)




def draw_part(setting, screen):
    x = 540
    y = 350
    w = 100
    h = 50
    col = (220, 220, 220)
    ft = pygame.font.Font("font/consola.ttf", 24)
    
    n = len(setting.part)
    x -= w * 0.5 * n
    for i in setting.part:
        pos = (x, y, w, h)
        pygame.draw.rect(screen, col, pos, 2)

        text = ft.render(i, True, col)
        text_rect = text.get_rect()
        text_rect.centerx = x + w * 0.5
        text_rect.centery = y + h * 0.5
        screen.blit(text, text_rect)

        x += w


def Order(setting, screen, img):
     #init clock
    clock = pygame.time.Clock()
    machine = pygame.image.load("img/machine.bmp")

    manager = pygame_gui.UIManager(setting.screen_size)

    push_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((640, 500), (100, 50)),
                                                 text='push_part',
                                                 manager=manager)

    pop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((640, 600), (100, 50)),
                                                 text='pop_part',
                                                 manager=manager)

    finish = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((375, 600), (150, 50)),
                                                 text='finish_define',
                                                 manager=manager)

    text_in = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 510), (200, 50)),
                                                 manager=manager)

    while setting.status == 1:
        time_delta = clock.tick(60) / 1000.0
        screen.blit(img, (0, 0))
        screen.blit(machine, (412, 50))
        
        draw_part(setting, screen)
        
        check_events(setting, manager, push_button, pop_button, text_in, finish)

        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()