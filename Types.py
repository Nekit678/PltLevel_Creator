from typing import Dict, List, Tuple
import pygame


class Map_Item(pygame.Surface):
    def __init__(self, image: pygame.Surface, x: int, y: int, item_id: int,
                 other_args: Dict[str, int] | None = None):
        super().__init__((32, 32))
        self.image = pygame.transform.scale(image, (32, 32))
        self.blit(self.image, (0, 0))

        self.rect = self.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item_id = item_id
        self.other_args = other_args

    def check_collide(self, pos: Tuple[int, int]):
        if self.rect.collidepoint(pos):
            TypeList.set_item(self.item_id)

    def get_args(self) -> str:
        result = f"{self.item_id} {self.rect.x} {self.rect.y}"
        if self.other_args is not None:
            for values in self.other_args.values():
                result += f" {values}"
        return result


# x: int, y: int, HP: int
class Player(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(player_img,
                         x, y, 0, other_args={"HP": 1})

# враги x: int, y: int, HP: int


class TestEnemy(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(test_enemy, x, y, 9)

# x: int, y: int
# все блоки


class GravityBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(gravity_block_img, x, y, 1)


class SpeedBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(speed_block_img, x, y, 2)


class SlowBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(slow_block_img, x, y, 3)


class KillBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(kill_block_img, x, y, 4)


class DamageBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(damage_block_img, x, y, 5)


class CommonBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(common_block_img, x, y, 6)


class JumpBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(jump_block_img, x, y, 7)


class CompleteBlock(Map_Item):
    def __init__(self, x: int, y: int):
        super().__init__(complete_block_img, x, y, 8)


class TypeList:
    CURRENT_ITEM_ID = 0

    items_id = {
        0: Player,
        1: GravityBlock,
        2: SpeedBlock,
        3: SlowBlock,
        4: KillBlock,
        5: DamageBlock,
        6: CommonBlock,
        7: JumpBlock,
        8: CompleteBlock,
        9: TestEnemy
    }

    type_list: List[type[Map_Item]] = [
        Player, TestEnemy, GravityBlock, SlowBlock, SpeedBlock, KillBlock,
        DamageBlock, CompleteBlock, JumpBlock, CommonBlock]

    @staticmethod
    def set_item(item_type: int):
        TypeList.CURRENT_ITEM_ID = item_type


jump_block_img = pygame.image.load("images/jump_block.png")
gravity_block_img = pygame.image.load("images/gravity_block.png")
speed_block_img = pygame.image.load("images/speed_block.png")
slow_block_img = pygame.image.load("images/slow_block.png")
damage_block_img = pygame.image.load("images/damage_block.png")
kill_block_img = pygame.image.load("images/kill_block.png")
complete_block_img = pygame.image.load("images/complete_block.png")
common_block_img = pygame.image.load("images/common_block.png")
player_img = pygame.image.load("images/player.png")
test_enemy = pygame.image.load("images/test_enemy.png")
