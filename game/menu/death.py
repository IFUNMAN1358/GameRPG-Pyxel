import pyxel

from game.menu.choose_hero import ChooseHero


class Death:
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
            Config.game_state = ChooseHero()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(self.x + 5, 70, 'DEATH', pyxel.COLOR_RED)
        pyxel.text(self.x, 100, "Restart?", pyxel.COLOR_WHITE)
