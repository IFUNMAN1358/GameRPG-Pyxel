import pyxel

from game.assets.tiles.tile import Tile


class Transfer(Tile):
    def __init__(self, x=0, y=0, level_class=None):
        super().__init__(x=x, y=y, w=8, h=8)
        self.level_class = level_class

        pyxel.load('assets/assets.pyxres')

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 32, 0, self.w, self.h)
