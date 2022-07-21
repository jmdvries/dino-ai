import arcade
from dinogame import BACKGROUND_COLOR, PLAYER_X, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, MAX_ENEMY_COUNT
from dinogame.player import Player
from dinogame.enemy import Enemy


class GameScreen(arcade.Window):
    """Main game window
    """

    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Setup empty sprite lists
        self.backgrounds_list = arcade.SpriteList()  # List of background objects
        self.enemies_list = arcade.SpriteList()  # List of enemy objects
        self.player = None  # Create player in setup()
        self.score = 0

        # Set the background window
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """Create the game objects
        """
        # TODO: Check existing lengths
        # Add players
        self.player = Player()
        # Add enemies
        for i in range(MAX_ENEMY_COUNT):
            enemy = Enemy()
            self.enemies_list.append(enemy)

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw all the sprite objects
        self.backgrounds_list.draw()
        self.enemies_list.draw()
        # self.players_list.draw()
        self.player.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            # self.players_list[0].jump()
            self.player.jump()

    def update(self, dt):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.backgrounds_list.update()
        self.enemies_list.update()
        # self.players_list.update()
        self.player.update()

        # Do collision detection
        hitlist = self.player.collides_with_list(self.enemies_list)
        if len(hitlist) > 0:
            print('Game over.')
            print(self.score, 'points')
            self.close()

        # Update score
        # TODO: Show score during game
        self.score += 1

        # Save player location
        dx = self.player.sx
        # Translate all enemies (with an inline list-compreshension loop)
        [e.translate((- dx + PLAYER_X, 0)) for e in self.enemies_list]
        # Translate player
        self.player.translate((- dx + PLAYER_X, 0))

        # Add in new enemies if the enemies_list is no longer full
        # range() loop will be empty if no more enemies (or for negative ranges)
        for i in range(MAX_ENEMY_COUNT-len(self.enemies_list)):
            enemy = Enemy()
            self.enemies_list.append(enemy)
