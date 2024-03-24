class Config:
    game_state = None
    hero = None

    ########################################################
    # Game state methods
    ########################################################

    def update(self):
        self.game_state.update()

    def draw(self):
        self.game_state.draw()
