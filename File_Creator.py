from typing import List
from Types import Map_Item


class File_Creator:
    def __init__(self):
        self.items: List[Map_Item] = []

    def load_items(self, items: List[Map_Item]):
        self.items = items

    def create_lvl(self):
        with open("test_lvl.pltlvl", "w") as file:
            for item in self.items:
                file.write(item.get_args() + "\n")
