import pyxel

from game.creatures.enemies.enemy import Enemy


class SkeletonKing(Enemy):
    def __init__(self, x, y, map_of_tiles: list):
        super().__init__(x, y, map_of_tiles,
                         v=96, w=32, h=32,
                         health=400, damage=20,
                         standing_chance=0.70, move_countdown=0)

    def draw(self):
        if self.direction == "down":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
        elif self.direction == "right":
            pyxel.blt(self.x, self.y, 0, 32, self.v + 32, self.w, self.h)
        elif self.direction == "left":
            pyxel.blt(self.x, self.y, 0, 0, self.v + 32, self.w, self.h)
        elif self.direction == "up":
            pyxel.blt(self.x, self.y, 0, 32, self.v, self.w, self.h)
