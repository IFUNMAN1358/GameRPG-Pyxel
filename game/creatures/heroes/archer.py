import random

import pyxel

from game.creatures.weapons.arrow import Arrow
from game.creatures.heroes.hero import Hero


class Archer(Hero):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v = 15

        self.max_health = 20
        self.health = 20
        self.max_damage = 2
        self.damage = 2

        self.damage_zone = 17

        self.arrows = []

    def update(self):
        super().update()

        self.random_for_clear_weapon = random.randint(1, 20)

        # Level update
        self.level_update(plus_health=5, plus_damage=2)

        if pyxel.btnp(pyxel.KEY_SPACE):
            arrow = Arrow(self.x, self.y, self.direction)

            self.arrows.append(arrow)

        for arrow in self.arrows:
            arrow.update()

            for enemy in self.map_of_enemies:
                if arrow.hits(enemy):
                    enemy.health -= self.damage
                    self.arrows.remove(arrow)
                    break

        if self.direction_weapon != '' and self.random_for_clear_weapon == 1:
            self.direction_weapon = ''

    def draw(self):
        if self.direction == "down":
            pyxel.blt(self.x, self.y, 0, 33, self.v, self.w, self.h)
        elif self.direction == "right":
            pyxel.blt(self.x, self.y, 0, 10, self.v, self.w, self.h)
        elif self.direction == "left":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
        elif self.direction == "up":
            pyxel.blt(self.x, self.y, 0, 22, self.v, self.w, self.h)

        for arrow in self.arrows:
            arrow.draw()
