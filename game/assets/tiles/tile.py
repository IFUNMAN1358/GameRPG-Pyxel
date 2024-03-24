class Tile:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def collide(self, player_x, player_y, player_w, player_h):
        if (player_x < self.x + self.w and player_x + player_w > self.x and
                player_y < self.y + self.h and player_y + player_h > self.y):
            return True
        return False

    def get_tile_size(self):
        return self.w, self.h
