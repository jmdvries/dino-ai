import arcade
from dinogame import X_MIN, X_MAX, GROUND_HEIGHT, JUMP_VELOCITY, GRAVITY


class Player(arcade.Sprite):
    """Player object (probably a dinosaur)"""

    def __init__(self):
        super().__init__('./resources/player/dino.png')

        # Set physics
        self.dt = 1.0
        self.sx = 50
        self.sy = 100
        self.vx = 4
        self.vy = 0
        self.ax = 0
        self.ay = GRAVITY

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

        # Handle edge of screen
        if self.sx < X_MIN:
            self.sx = X_MAX
        if self.sx > X_MAX:
            self.sx = X_MIN

        # Handle ground
        if self.sy < GROUND_HEIGHT:
            self.sy = GROUND_HEIGHT

        self.center_x = self.sx
        self.center_y = self.sy

    def jump(self):
        # Or if we allow to double jump on the apex
        # TODO: Only allow a single double jump?
        # if self.sy == GROUND_HEIGHT or abs(self.vy) <= abs(DOUBLE_JUMP_MARGIN):

        # Can only jump if on the ground
        if self.sy == GROUND_HEIGHT:
            # Jump simply adds vy
            self.vy = JUMP_VELOCITY