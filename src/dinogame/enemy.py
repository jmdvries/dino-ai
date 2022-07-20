import arcade
from random import randint

from dinogame import X_MIN, X_MAX, GROUND_HEIGHT, ENEMY_TYPES, SPAWN_MIN_X, SPAWN_MAX_X


class Enemy(arcade.Sprite):
    """Player object (probably a dinosaur)"""

    def __init__(self):
        # Choose enemy type
        self.type = randint(0, len(ENEMY_TYPES)-1)

        super().__init__(ENEMY_TYPES[self.type]['image'])

        # Set physics
        self.dt = 1.0
        self.sx = randint(SPAWN_MIN_X, SPAWN_MAX_X)
        self.sy = ENEMY_TYPES[self.type]['sy']
        self.vx = ENEMY_TYPES[self.type]['vx']
        self.vy = ENEMY_TYPES[self.type]['vy']
        self.ax = ENEMY_TYPES[self.type]['ax']
        self.ay = ENEMY_TYPES[self.type]['ay']

        # Update sprite location
        self.center_x = self.sx
        self.center_y = self.sy

    def update(self):
        """Check for collisions and update player state accordingly
        """
        # Apply physics (euler) manually
        self.vx = self.vx + self.ax * self.dt
        self.vy = self.vy + self.ay * self.dt
        self.sx = self.sx + self.vx * self.dt
        self.sy = self.sy + self.vy * self.dt

        # TODO: Collision detection, probably automatable

        # TODO: Probably not necessary...
        # Handle edge of screen
        if self.sx < X_MIN:
            self.sx = X_MAX
        if self.sx > X_MAX:
            self.sx = X_MIN

        # TODO: Probably not necessary...
        # Handle ground
        if self.sy < GROUND_HEIGHT:
            self.sy = GROUND_HEIGHT

        self.center_x = self.sx
        self.center_y = self.sy