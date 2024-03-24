import random

import pyxel


class Bomb:
    def __init__(self):
        self.x = random.randint(50, 225)
        self.y = random.randint(50, 225)

        self.w = 8
        self.h = 8

        self.take = False

    def update(self, hero):
        self.player_x = hero.x
        self.player_y = hero.y

        # Death
        if (self.x <= hero.x + hero.w) and (self.x + self.w >= hero.x) and \
                (self.y <= hero.y + hero.h) and (self.y + self.h >= hero.y) and not self.take:
            hero.health = 0

            self.x, self.y = 250, 250
            self.take = True

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 88, 8, self.w, self.h)
