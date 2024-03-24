import random

import pyxel

from game.assets.tiles.bush import Bush
from game.assets.tiles.transfer import Transfer
from game.creatures.enemies.rat import Rat
from game.creatures.sweets.bomb import Bomb
from game.creatures.sweets.heart import Heart
from game.creatures.sweets.shield import Shield
from game.creatures.sweets.sword import Sword
from game.levels.fourth_level import FourthLevel
from game.tools.tiles_builder import TilesBuilder


class ThirdLevel:
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
        tiles_builder.add_row(232, 128, "down", 3, Transfer, level_class=FourthLevel)

        # Creating map of tiles
        self.map_of_tiles = tiles_builder.build()

        # Enemies INIT
        self.first_rat = Rat(180, 60, map_of_tiles=self.map_of_tiles)
        self.second_rat = Rat(180, 70, map_of_tiles=self.map_of_tiles)
        self.third_rat = Rat(180, 80, map_of_tiles=self.map_of_tiles)
        self.fourth_rat = Rat(180, 90, map_of_tiles=self.map_of_tiles)
        self.fifth_rat = Rat(180, 100, map_of_tiles=self.map_of_tiles)
        self.sixth_rat = Rat(180, 110, map_of_tiles=self.map_of_tiles)
        self.seventh_rat = Rat(180, 120, map_of_tiles=self.map_of_tiles)
        self.eighth_rat = Rat(180, 130, map_of_tiles=self.map_of_tiles)
        self.ninth_rat = Rat(180, 140, map_of_tiles=self.map_of_tiles)
        self.tenth_rat = Rat(180, 150, map_of_tiles=self.map_of_tiles)
        self.map_of_enemies = [self.first_rat, self.second_rat, self.third_rat, self.fourth_rat, self.fifth_rat,
                               self.sixth_rat, self.seventh_rat, self.eighth_rat, self.ninth_rat, self.tenth_rat]

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
        self.first_rat.update(self.hero, chase_radius=100)
        self.second_rat.update(self.hero, chase_radius=100)
        self.third_rat.update(self.hero, chase_radius=100)
        self.fourth_rat.update(self.hero, chase_radius=100)
        self.fifth_rat.update(self.hero, chase_radius=100)
        self.sixth_rat.update(self.hero, chase_radius=100)
        self.seventh_rat.update(self.hero, chase_radius=100)
        self.eighth_rat.update(self.hero, chase_radius=100)
        self.ninth_rat.update(self.hero, chase_radius=100)
        self.tenth_rat.update(self.hero, chase_radius=100)

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
        self.first_rat.draw()
        self.second_rat.draw()
        self.third_rat.draw()
        self.fourth_rat.draw()
        self.fifth_rat.draw()
        self.sixth_rat.draw()
        self.seventh_rat.draw()
        self.eighth_rat.draw()
        self.ninth_rat.draw()
        self.tenth_rat.draw()

        # Sweet DRAW
        self.sweet.draw()
