import math
import random


class Enemy:
    def __init__(self, x, y, map_of_tiles: list, v, w, h, health, damage, standing_chance, move_countdown):
        self.map_of_tiles = map_of_tiles
        self.x = x
        self.y = y
        self.direction = "down"
        self.v = v
        self.w = w
        self.h = h
        self.standing_chance = standing_chance
        self.move_countdown = move_countdown
        self.health = health
        self.damage = damage
        self.death = False

    def update(self, hero, chase_radius):
        self.player_x = hero.x
        self.player_y = hero.y

        prev_x, prev_y = self.x, self.y

        distance_to_player = math.sqrt((self.x - self.player_x) ** 2 + (self.y - self.player_y) ** 2)

        # Dealing damage
        if (self.x <= hero.x + hero.w) and (self.x + self.w >= hero.x) and \
                (self.y <= hero.y + hero.h) and (self.y + self.h >= hero.y):
            self.random_damage = random.randint(1, 50)
            if self.random_damage == 1:
                hero.health -= (self.damage - hero.armor)

        # Death
        if self.health <= 0 and not self.death:
            self.x = 350
            self.y = 350
            hero.exp += 10
            self.death = True

        # Hero detection
        if distance_to_player <= chase_radius:
            self.random_speed = random.randint(1, 5)
            if self.random_speed == 1:
                if self.player_x < self.x:
                    self.direction = "left"
                    self.x -= 1
                elif self.player_x > self.x:
                    self.direction = "right"
                    self.x += 1
                if self.player_y < self.y:
                    self.direction = "up"
                    self.y -= 1
                elif self.player_y > self.y:
                    self.direction = "down"
                    self.y += 1

        # Random behavior
        else:
            if self.move_countdown <= 0:
                if random.random() < self.standing_chance:
                    self.direction = "down"
                    self.move_countdown = 0
                else:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.move_countdown = random.randint(5, 15)
            else:
                if self.direction == "up":
                    self.y -= 1
                elif self.direction == "down":
                    self.y += 1
                elif self.direction == "left":
                    self.x -= 1
                elif self.direction == "right":
                    self.x += 1
                self.move_countdown -= 1

        # Collision
        for tile in self.map_of_tiles:
            if tile.collide(self.x, self.y, self.w, self.h):
                self.x, self.y = prev_x, prev_y
