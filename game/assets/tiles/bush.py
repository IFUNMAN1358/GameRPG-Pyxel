import random

import pyxel

from game.assets.tiles.tile import Tile


class Bush(Tile):
    def __init__(self, x=0, y=0, type_bush=None):
        super().__init__(x=x, y=y, w=8, h=8)

        self.type_bush = type_bush if type_bush is not None else self.random_type()

        pyxel.load('assets/assets.pyxres')

    def draw(self):
        if self.type_bush == 0:
            pyxel.blt(self.x, self.y, 1, 0, 0, self.w, self.h)
        elif self.type_bush == 1:
            pyxel.blt(self.x, self.y, 1, 8, 0, self.w, self.h)
        elif self.type_bush == 2:
            pyxel.blt(self.x, self.y, 1, 16, 0, self.w, self.h)
        elif self.type_bush == 3:
            pyxel.blt(self.x, self.y, 1, 24, 0, self.w, self.h)

    def random_type(self):
        return random.choices(range(4), weights=[0.7, 0.1, 0.1, 0.1])[0]
