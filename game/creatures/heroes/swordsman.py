import random

import pyxel

from game.creatures.heroes.hero import Hero


class Swordsman(Hero):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v = 0

        self.max_health = 100
        self.health = 100
        self.max_damage = 8
        self.damage = 8

        self.damage_zone = 17

    def update(self):
        super().update()

        self.random_for_clear_weapon = random.randint(1, 20)

        # Level update
        self.level_update(plus_health=10, plus_damage=2)

        # Dealing damage
        if pyxel.btnp(pyxel.KEY_SPACE):
            for enemy in self.map_of_enemies:

                if self.direction == "down":
                    self.direction_weapon = 'down'
                    if (enemy.x >= self.x - self.damage_zone and enemy.x <= self.x + self.w + self.damage_zone) \
                            and (enemy.y >= self.y + self.h and enemy.y <= self.y + self.h + self.damage_zone):
                        enemy.health -= self.damage

                elif self.direction == "up":
                    self.direction_weapon = 'up'
                    if (enemy.x >= self.x - self.damage_zone and enemy.x <= self.x + self.w + self.damage_zone) \
                            and (enemy.y >= self.y - self.damage_zone and enemy.y <= self.y):
                        enemy.health -= self.damage

                elif self.direction == "left":
                    self.direction_weapon = 'left'
                    if (enemy.y >= self.y - self.damage_zone and enemy.y <= self.y + self.h + self.damage_zone) \
                            and (enemy.x >= self.x - self.damage_zone and enemy.x <= self.x):
                        enemy.health -= self.damage

                elif self.direction == "right":
                    self.direction_weapon = 'right'
                    if (enemy.y >= self.y - self.damage_zone and enemy.y <= self.y + self.h + self.damage_zone) \
                            and (enemy.x >= self.x + self.w and enemy.x <= self.x + self.w + self.damage_zone):
                        enemy.health -= self.damage

        # Clear weapon
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

        if self.direction_weapon == 'down':
            pyxel.blt(self.x + 2, self.y + 12, 0, 68, self.v, 4, self.h)
        elif self.direction_weapon == 'right':
            pyxel.blt(self.x + 8, self.y, 0, 53, self.v, 11, self.h)
        elif self.direction_weapon == 'left':
            pyxel.blt(self.x - 8, self.y, 0, 44, self.v, self.w, self.h)
        elif self.direction_weapon == 'up':
            pyxel.blt(self.x + 2, self.y - 14, 0, 64, self.v, 4, self.h)
        elif self.direction_weapon == '':
            pass
