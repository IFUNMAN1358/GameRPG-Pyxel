import pyxel

from game.levels.first_level import FirstLevel


class ChooseHero:
    def __init__(self):
        self.selected_hero = 0

        self.x = 100

    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.selected_hero = (self.selected_hero - 1) % 3
        elif pyxel.btnp(pyxel.KEY_S):
            self.selected_hero = (self.selected_hero + 1) % 3

        if pyxel.btnp(pyxel.KEY_SPACE):
            from game.config import Config
            from game.creatures.heroes.archer import Archer
            from game.creatures.heroes.swordsman import Swordsman
            from game.creatures.heroes.wizard import Wizard

            if self.selected_hero == 0:
                Config.hero = Swordsman()
            elif self.selected_hero == 1:
                Config.hero = Archer()
            elif self.selected_hero == 2:
                Config.hero = Wizard()
            Config.game_state = FirstLevel()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(self.x, 70, 'Choose Your Hero', 12)
        pyxel.text(self.x + 5, 90, "Swordsman", pyxel.COLOR_YELLOW if self.selected_hero == 0 else pyxel.COLOR_WHITE)
        pyxel.text(self.x + 5, 110, "Archer", pyxel.COLOR_YELLOW if self.selected_hero == 1 else pyxel.COLOR_WHITE)
        pyxel.text(self.x + 5, 130, "Wizard", pyxel.COLOR_YELLOW if self.selected_hero == 2 else pyxel.COLOR_WHITE)
