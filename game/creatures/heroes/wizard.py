import random

import pyxel

from game.creatures.heroes.hero import Hero


class Wizard(Hero):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v = 30

        self.max_health = 50
        self.health = 50
        self.max_damage = 5
        self.damage = 5

        self.damage_zone = 50

    def update(self):
        super().update()

        self.random_for_clear_weapon = random.randint(1, 20)

        # Level update
        self.level_update(plus_health=10, plus_damage=1)

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
            pyxel.blt(self.x - 10, self.y + 18, 0, 56, 16, 32, 32)
        elif self.direction_weapon == 'right':
            pyxel.blt(self.x + 15, self.y - 7, 0, 56, 16, 32, 32)
        elif self.direction_weapon == 'left':
            pyxel.blt(self.x - 35, self.y - 7, 0, 56, 16, 32, 32)
        elif self.direction_weapon == 'up':
            pyxel.blt(self.x - 10, self.y - 33, 0, 56, 16, 32, 32)
        elif self.direction_weapon == '':
            pass
