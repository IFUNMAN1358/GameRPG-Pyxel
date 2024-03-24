import pyxel

from game.config import Config
from game.menu.choose_hero import ChooseHero


class MainMenu:
    def __init__(self):
        self.selected_button = 0

        self.x = 110

    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.selected_button = (self.selected_button - 1) % 2
        elif pyxel.btnp(pyxel.KEY_S):
            self.selected_button = (self.selected_button + 1) % 2

        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.selected_button == 0:
                Config.game_state = ChooseHero()
            elif self.selected_button == 1:
                pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(self.x, 70, 'Menu', 12)
        pyxel.text(self.x, 100, "Start", pyxel.COLOR_YELLOW if self.selected_button == 0 else pyxel.COLOR_WHITE)
        pyxel.text(self.x, 120, "Exit", pyxel.COLOR_YELLOW if self.selected_button == 1 else pyxel.COLOR_WHITE)
