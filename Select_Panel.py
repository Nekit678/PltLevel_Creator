from typing import List, Literal, Tuple
import pygame
from Types import Map_Item, TypeList


class Select_Panel(pygame.Surface):
    def __init__(self, x: int, y: int):
        super().__init__((1280, 64))
        self.rect = self.get_rect()
        self.rect. x = x
        self.rect.y = y
        self.shift_x = 0
        self.min_shift = 0
        self.buttons: List[Map_Item] = []

    def scroll(self, direction: Literal["left", "right"]):
        shift = {"left": -20, "right": 20}
        if self.shift_x + shift[direction] >= self.min_shift:
            self.shift_x += shift[direction]

    def check_scroll(self, mouse_pos: Tuple[int, int], direction: Literal["left", "right"]):
        if self.rect.collidepoint(mouse_pos):
            self.scroll(direction)

    def check_collide(self, pos: Tuple[int, int]):
        if self.rect.collidepoint(pos):
            for b in self.buttons:
                b.check_collide((pos[0] + self.shift_x, pos[1] - self.rect.y))

    def update(self):
        self.fill("blue")
        self.buttons = []
        x = 10
        gap = 10
        for type_block in TypeList.type_list:
            item = type_block(x - self.shift_x, 16)
            self.buttons.append(item)
            x += gap + 32

        for b in self.buttons:
            self.blit(b, b.rect)
