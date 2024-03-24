import random

import pyxel

from game.assets.tiles.bush import Bush
from game.assets.tiles.transfer import Transfer
from game.creatures.enemies.skeleton import Skeleton
from game.creatures.enemies.skeleton_king import SkeletonKing
from game.creatures.sweets.bomb import Bomb
from game.creatures.sweets.heart import Heart
from game.creatures.sweets.shield import Shield
from game.creatures.sweets.sword import Sword
from game.levels.fifth_level import FifthLevel
from game.tools.tiles_builder import TilesBuilder


class FourthLevel:
    def __init__(self):
        # Creating tiles builder
        tiles_builder = TilesBuilder()

        # Walls INIT
        tiles_builder.add_row(0, 0, "right", 30, Bush)
        tiles_builder.add_row(0, 0, "down", 30, Bush)
        tiles_builder.add_row(0, 232, "right", 30, Bush)
        tiles_builder.add_row(232, 0, "down", 16, Bush)
        tiles_builder.add_row(232, 232, "up", 11, Bush)
        tiles_builder.add_row(0, 16, "right", 3, Bush)
        tiles_builder.add_row(16, 0, "down", 3, Bush)

        # Transfer INIT
        tiles_builder.add_row(232, 128, "down", 3, Transfer, level_class=FifthLevel)

        # Creating map of tiles
        self.map_of_tiles = tiles_builder.build()

        # Enemies INIT
        self.first_skeleton = Skeleton(80, 60, map_of_tiles=self.map_of_tiles)
        self.skeleton_king = SkeletonKing(130, 60, map_of_tiles=self.map_of_tiles)
        self.second_skeleton = Skeleton(180, 60, map_of_tiles=self.map_of_tiles)
        self.map_of_enemies = [self.first_skeleton, self.skeleton_king, self.second_skeleton]

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
        self.first_skeleton.update(self.hero, chase_radius=80)
        self.skeleton_king.update(self.hero, chase_radius=150)
        self.second_skeleton.update(self.hero, chase_radius=80)

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
        self.first_skeleton.draw()
        self.skeleton_king.draw()
        self.second_skeleton.draw()

        # Sweet DRAW
        self.sweet.draw()
