import pyxel

from game.creatures.enemies.enemy import Enemy


class Cat(Enemy):
    def __init__(self, x, y, map_of_tiles: list):
        super().__init__(x, y, map_of_tiles,
                         v=160, w=40, h=32,
                         health=700, damage=20,
                         standing_chance=1, move_countdown=0)
        self.const_x = x
        self.const_y = y

    def update(self, hero, chase_radius):
        # Death
        if self.health <= 0 and not self.death:
            hero.health = 0
            self.death = True

        super().update(hero, chase_radius)

        self.x = self.const_x
        self.y = self.const_y

    def draw(self):
        if self.direction == "down":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
        elif self.direction == "right":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
        elif self.direction == "left":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
        elif self.direction == "up":
            pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h)
