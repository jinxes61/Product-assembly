import pygame_gui
import pygame
import sys
import welcome as wel
import order
import change

def solve(setting, screen, img):

    if setting.status == 0:
        wel.Welcome(setting, screen, img)
    elif setting.status == 1:
        order.Order(setting, screen, img)
    elif setting.status == 2:
        change.ChangePart(setting, screen, img)