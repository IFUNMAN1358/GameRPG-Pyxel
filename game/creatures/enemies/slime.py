import pyxel

from game.creatures.enemies.enemy import Enemy


class Slime(Enemy):
    def __init__(self, x, y, map_of_tiles: list):
        super().__init__(x, y, map_of_tiles,
                         v=48, w=16, h=16,
                         health=20, damage=10,
                         standing_chance=0.98, move_countdown=0)

    def draw(self):
        if self.direction == "down":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
        elif self.direction == "right":
            pyxel.blt(self.x, self.y, 0, 48, self.v, self.w, self.h)
        elif self.direction == "left":
            pyxel.blt(self.x, self.y, 0, 32, self.v, self.w, self.h)
        elif self.direction == "up":
            pyxel.blt(self.x, self.y, 0, 16, self.v, self.w, self.h)
