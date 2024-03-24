class TilesBuilder:
    def __init__(self):
        self.map_of_tiles = []

    def add_row(self, start_x, start_y, direction, length, tile_type, **kwargs):
        tile_width, tile_height = tile_type().get_tile_size()
        if direction == "right":
            for i in range(length):
                x = start_x + i * tile_width
                y = start_y
                self.add_tile(x, y, tile_type, **kwargs)
        elif direction == "left":
            for i in range(length):
                x = start_x - i * tile_width
                y = start_y
                self.add_tile(x, y, tile_type, **kwargs)
        elif direction == "up":
            for i in range(length):
                x = start_x
                y = start_y - i * tile_height
                self.add_tile(x, y, tile_type, **kwargs)
        elif direction == "down":
            for i in range(length):
                x = start_x
                y = start_y + i * tile_height
                self.add_tile(x, y, tile_type, **kwargs)

    def add_area(self, start_x, start_y, width, height, tile_type, **kwargs):
        for y in range(start_y, start_y + (height - 1) * 8):
            for x in range(start_x, start_x + (width - 1) * 8):
                self.add_tile(x, y, tile_type, **kwargs)

    def add_tile(self, x, y, tile_type, **kwargs):
        tile = tile_type(x, y, **kwargs)
        self.map_of_tiles.append(tile)

    def build(self):
        return self.map_of_tiles
