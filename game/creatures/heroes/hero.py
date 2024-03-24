import pyxel

from game.assets.tiles.transfer import Transfer
from game.menu.death import Death


class Hero:
    def __init__(self, map_of_tiles=list(), map_of_enemies=list(), x=0, y=0):
        pyxel.load('assets/assets.pyxres')

        self.map_of_tiles = map_of_tiles
        self.map_of_enemies = map_of_enemies

        self.x = x
        self.y = y
        self.w = 9
        self.h = 14

        self.v = 0
        self.direction = "down"
        self.direction_weapon = ''

        self.health = 0
        self.armor = 0
        self.damage = 0
        self.exp = 0
        self.lvl = 0

        self.levels = {'l1': False, 'l2': False, 'l3': False,
                       'l4': False}

    def update(self):
        prev_x, prev_y = self.x, self.y

        # Death
        if self.health <= 0:
            from game.config import Config
            Config.game_state = Death()

        # Controlling
        if pyxel.btn(pyxel.KEY_D):
            self.direction = "right"
            self.x += 1
        elif pyxel.btn(pyxel.KEY_A):
            self.direction = "left"
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_W):
            self.direction = "up"
            self.y -= 1
        elif pyxel.btn(pyxel.KEY_S):
            self.direction = "down"
            self.y += 1

        # Collision
        for tile in self.map_of_tiles:
            if isinstance(tile, Transfer) and tile.collide(self.x, self.y, self.w, self.h):
                self.switch_level(tile.level_class)
                return
            elif tile.collide(self.x, self.y, self.w, self.h):
                self.x, self.y = prev_x, prev_y
                return

    def switch_level(self, level_class):
        from game.config import Config
        Config.game_state = level_class()

    def level_update(self, plus_health: int, plus_damage: int):
        # First level = 30 exp
        if self.exp == 30 and not self.levels['l1']:
            self.levels['l1'] = True
            self.lvl = 1

            self.health = self.max_health + plus_health
            self.max_health = self.health

            self.damage = self.max_damage + plus_damage
            self.max_damage = self.damage

            self.armor += 3

        # Second level = 70 exp
        elif self.exp == 70 and not self.levels['l2']:
            self.levels['l2'] = True
            self.lvl = 2

            self.health = self.max_health + plus_health
            self.max_health = self.health

            self.damage = self.max_damage + plus_damage
            self.max_damage = self.damage

            self.armor += 1

        # Third level = 170 exp
        elif self.exp == 170 and not self.levels['l3']:
            self.levels['l3'] = True
            self.lvl = 3

            self.health = self.max_health + plus_health
            self.max_health = self.health

            self.damage = self.max_damage + plus_damage
            self.max_damage = self.damage

            self.armor += 1

        # Fourth level = 200 exp
        elif self.exp == 200 and not self.levels['l4']:
            self.levels['l4'] = True
            self.lvl = 4

            self.health = self.max_health + plus_health
            self.max_health = self.health

            self.damage = self.max_damage + plus_damage
            self.max_damage = self.damage

            self.armor += 3
