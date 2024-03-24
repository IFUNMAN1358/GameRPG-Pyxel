import random

import pyxel

from game.assets.tiles.bush import Bush
from game.creatures.enemies.cat import Cat
from game.creatures.enemies.skeleton_king import SkeletonKing
from game.creatures.sweets.bomb import Bomb
from game.creatures.sweets.heart import Heart
from game.creatures.sweets.shield import Shield
from game.creatures.sweets.sword import Sword
from game.tools.tiles_builder import TilesBuilder


class FifthLevel:
    def __init__(self):
        # Creating tiles builder
        tiles_builder = TilesBuilder()

        # Walls INIT
        tiles_builder.add_row(0, 0, "right", 30, Bush)
        tiles_builder.add_row(0, 0, "down", 30, Bush)
        tiles_builder.add_row(0, 232, "right", 30, Bush)
        tiles_builder.add_row(232, 0, "down", 30, Bush)
        tiles_builder.add_row(0, 16, "right", 3, Bush)
        tiles_builder.add_row(16, 0, "down", 3, Bush)

        # Creating map of tiles
        self.map_of_tiles = tiles_builder.build()

        # Enemies INIT
        self.cat = Cat(100, 100, map_of_tiles=self.map_of_tiles)
        self.first_skeleton_king = SkeletonKing(130, 100, map_of_tiles=self.map_of_tiles)
        self.second_skeleton_king = SkeletonKing(70, 100, map_of_tiles=self.map_of_tiles)
        self.third_skeleton_king = SkeletonKing(100, 130, map_of_tiles=self.map_of_tiles)
        self.fourth_skeleton_king = SkeletonKing(100, 70, map_of_tiles=self.map_of_tiles)
        self.map_of_enemies = [self.cat, self.first_skeleton_king, self.second_skeleton_king,
                               self.third_skeleton_king, self.fourth_skeleton_king]

        # Sweet INIT
        self.sweet = random.choice([Heart(), Shield(), Sword(), Bomb()])

        # Hero INIT
        from game.config import Config
        self.hero = Config.hero
        self.hero.x = 40
        self.hero.y = 40
        self.hero.map_of_tiles = self.map_of_tiles
        self.hero.map_of_enemies = self.map_of_enemies

    def update(self):
        # Hero UPDATE
        self.hero.update()

        # Enemies UPDATE
        self.cat.update(self.hero, chase_radius=240)
        self.first_skeleton_king.update(self.hero, chase_radius=100)
        self.second_skeleton_king.update(self.hero, chase_radius=100)
        self.third_skeleton_king.update(self.hero, chase_radius=100)
        self.fourth_skeleton_king.update(self.hero, chase_radius=100)

        # Sweet UPDATE
        self.sweet.update(self.hero)

    def draw(self):
        # Clear
        pyxel.cls(0)

        # Background DRAW
        pyxel.rect(x=0, y=0, w=240, h=240, col=pyxel.COLOR_LIME)

        # Tiles DRAW
        for tile in self.map_of_tiles:
            tile.draw()

        # Interface DRAW
        pyxel.rect(x=0, y=0, w=20, h=21, col=pyxel.COLOR_BLACK)
        pyxel.text(0, 0, f'H:{self.hero.health}', col=pyxel.COLOR_RED)
        pyxel.text(0, 5, f'A:{self.hero.armor}', col=pyxel.COLOR_LIGHT_BLUE)
        pyxel.text(0, 10, f'D:{self.hero.damage}', col=pyxel.COLOR_YELLOW)
        pyxel.text(0, 15, f'L:{self.hero.lvl}', col=pyxel.COLOR_LIME)

        # Hero DRAW
        self.hero.draw()

        # Enemies DRAW
        self.cat.draw()
        self.first_skeleton_king.draw()
        self.second_skeleton_king.draw()
        self.third_skeleton_king.draw()
        self.fourth_skeleton_king.draw()

        # Sweet DRAW
        self.sweet.draw()
