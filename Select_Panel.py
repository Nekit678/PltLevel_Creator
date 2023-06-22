from typing import List, Literal, Tuple
import pygame


class Select_Panel(pygame.Surface):
    def __init__(self, x: int, y: int):
        super().__init__((1280, 64))
        self.rect = self.get_rect()
        self.rect. x = x
        self.rect.y = y
        self.shift_x = 0
        self.min_shift = 0

        self.buttons: List[pygame.Surface] = []

        for i in range(0, 50):
            surf = pygame.Surface((32, 32))
            surf.fill("red")
            self.buttons.append(surf)

    def scroll(self, direction: Literal["left", "right"]):
        shift = {"left": -20, "right": 20}
        if self.shift_x + shift[direction] >= self.min_shift:
            self.shift_x += shift[direction]

    def check_scroll(self, mouse_pos: Tuple[int, int], direction: Literal["left", "right"]):
        if self.rect.collidepoint(mouse_pos):
            self.scroll(direction)

    def update(self):
        self.fill("blue")
        x = 10
        gap = 10

        for b in self.buttons:
            self.blit(b, (x - self.shift_x, 16))
            x += gap + 32
