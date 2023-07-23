from typing import List, Literal, Tuple
import pygame

from Types import Map_Item


class Level_Map(pygame.Surface):
    def __init__(self, x: int, y: int):
        super().__init__((1280, 656))
        self.rect = self.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shift_x = 0
        self.shift_y = -32*15

        self.items: List[Map_Item] = []

    def get_items(self) -> List[Map_Item]:
        return self.items

    def scroll(self, direction: Literal["left", "right", "up", "down"]):
        shift = {"left": -32, "right": 32, "up": -32, "down": 32}
        if direction == "left":
            self.shift_x += shift[direction]
        elif direction == "right":
            self.shift_x += shift[direction]
        elif direction == "up":
            self.shift_y += shift[direction]
        elif direction == "down":
            self.shift_y += shift[direction]

    def tailing_coord(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        x = pos[0]
        y = pos[1]
        while x % 32 != 0:
            x -= 1
        while y % 32 != 0:
            y -= 1
        return (x, y)

    def check_collide(self, pos: Tuple[int, int], item: type[Map_Item]):
        if self.rect.collidepoint(pos):
            x, y = self.tailing_coord(
                (pos[0] + self.shift_x, pos[1] + self.shift_y))
            if y < 0:
                self.items.append(item(x, y))

    def check_collide_delete(self, pos: Tuple[int, int]):
        if self.rect.collidepoint(pos):
            x, y = (pos[0] + self.shift_x, pos[1] + self.shift_y)
            for item in self.items:
                if item.rect.collidepoint((x, y)):
                    self.items.remove(item)
                    break

    def update(self):
        self.fill("violet")

        for item in self.items:
            self.blit(item, (item.rect.x - self.shift_x,
                      item.rect.y - self.shift_y))

        if 720+self.shift_y > 0:
            deactive_zone = pygame.Surface((1280, 720+self.shift_y))
            deactive_zone.fill("red")
            self.blit(deactive_zone, (0, 0-self.shift_y))

        for row in range(0, 720, 32):
            pygame.draw.line(self, (102, 150, 255), (0, row), (1280, row))
        for col in range(0, 1280, 32):
            pygame.draw.line(self, (102, 150, 255), (col, 0), (col, 720))
