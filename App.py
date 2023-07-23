import pygame
import sys
from File_Creator import File_Creator
from Level_Map import Level_Map

from Select_Panel import Select_Panel
from Types import TypeList

FPS = 60
WIDTH = 1280
HEIGHT = 720
CURRENT_ITEM: int = 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

pygame.display.set_caption("Level Creator")
clock = pygame.time.Clock()

panel = Select_Panel(0, 656)
level_map = Level_Map(0, 0)
file_creator = File_Creator()


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

        #!!!!!!!
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                level_map.check_collide(
                    event.pos, TypeList.items_id[TypeList.CURRENT_ITEM_ID])
                panel.check_collide(event.pos)
            if event.button == 3:
                level_map.check_collide_delete(event.pos)

        if event.type == pygame.MOUSEWHEEL:
            pos = pygame.mouse.get_pos()
            if event.y > 0:
                panel.check_scroll(pos, "left")
            else:
                panel.check_scroll(pos, "right")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                file_creator.load_items(level_map.get_items())
                file_creator.create_lvl()

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
