import pygame

class Ship:
    """A class to manage the ship

    """

    def __init__(self, ai_game):
        """Initialize the ship and sets its starting
        the self reference and a reference to the current instance of the AlienInvasion class
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        # place midbottom of the ship at the position midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom        # midbottom is shortcut atribute
        #self.rect.midbottom = (100,500)        # random position

        # Store a decimal value for the ship's horizontal position
        # Because we’re adjusting the position of the ship by fractions of a pixel, we
        # need to assign the position to a variable that can store a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the ship at its current location"""
        # https://stackoverflow.com/questions/37800894/what-is-the-surface-blit-function-in-pygame-what-does-it-do-how-does-it-work
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed


        #Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y