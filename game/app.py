import pyxel

from game.config import Config


class Game:
    def __init__(self):
        self.game_state = Config()

        from game.menu.main_menu import MainMenu
        Config.game_state = MainMenu()

        pyxel.init(width=240, height=240, fps=120, title='GameRPG')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.game_state.update()

    def draw(self):
        self.game_state.draw()


if __name__ == '__main__':
    Game()
