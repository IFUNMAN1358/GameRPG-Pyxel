import pyxel

from game.creatures.enemies.enemy import Enemy


class Rat(Enemy):
    def __init__(self, x, y, map_of_tiles: list):
        super().__init__(x, y, map_of_tiles,
                         v=80, w=8, h=8,
                         health=30, damage=10,
                         standing_chance=0.20, move_countdown=5)

    def draw(self):
        if self.direction == "down":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
        elif self.direction == "right":
            pyxel.blt(self.x, self.y, 0, 8, self.v + 8, self.w, self.h)
        elif self.direction == "left":
            pyxel.blt(self.x, self.y, 0, 0, self.v + 8, self.w, self.h)
        elif self.direction == "up":
            pyxel.blt(self.x, self.y, 0, 8, self.v, self.w, self.h)
