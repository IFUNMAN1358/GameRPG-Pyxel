import pyxel


class Arrow:
    def __init__(self, x, y, direction_weapon):
        self.x = x
        self.y = y
        self.direction_weapon = direction_weapon
        self.speed = 2

    def update(self):
        if self.direction_weapon == 'down':
            self.y += self.speed
        elif self.direction_weapon == 'up':
            self.y -= self.speed
        elif self.direction_weapon == 'left':
            self.x -= self.speed
        elif self.direction_weapon == 'right':
            self.x += self.speed

    def hits(self, enemy):
        if (enemy.x <= self.x <= enemy.x + enemy.w or enemy.x <= self.x + 3 <= enemy.x + enemy.w) and \
           (enemy.y <= self.y <= enemy.y + enemy.h or enemy.y <= self.y + 11 <= enemy.y + enemy.h):
            return True
        return False

    def draw(self):
        if self.direction_weapon == 'down':
            pyxel.blt(self.x + 3, self.y + 14, 0, 46, 22, 3, 11)
        elif self.direction_weapon == 'right':
            pyxel.blt(self.x + 8, self.y + 5, 0, 42, 16, 11, 3)
        elif self.direction_weapon == 'left':
            pyxel.blt(self.x - 8, self.y + 5, 0, 42, 19, 11, 3)
        elif self.direction_weapon == 'up':
            pyxel.blt(self.x + 3, self.y - 11, 0, 43, 22, 3, 11)
