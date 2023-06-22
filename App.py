import pygame
import sys
from Level_Map import Level_Map

from Select_Panel import Select_Panel

FPS = 60
WIDTH = 1280
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

pygame.display.set_caption("Level Creator")
clock = pygame.time.Clock()

panel = Select_Panel(0, 656)
level_map = Level_Map(0, 0)


def update():
    panel.update()
    level_map.update()
    screen.blit(panel, panel.rect)
    screen.blit(level_map, level_map.rect)


while True:
    screen.fill("black")
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                level_map.check_collide(event.pos)

        if event.type == pygame.MOUSEWHEEL:
            pos = pygame.mouse.get_pos()
            if event.y > 0:
                panel.check_scroll(pos, "left")
            else:
                panel.check_scroll(pos, "right")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        level_map.scroll("left")
    elif keys[pygame.K_RIGHT]:
        level_map.scroll("right")
    elif keys[pygame.K_UP]:
        level_map.scroll("up")
    elif keys[pygame.K_DOWN]:
        level_map.scroll("down")

    update()

    pygame.display.update()
