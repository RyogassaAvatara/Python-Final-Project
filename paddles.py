import pygame


# Paddle Class
class Paddles:
    def __init__(self, display, color, corX, corY, width, height):
        self.display = display
        self.color = color
        self.width = width
        self.height = height
        self.corX = corX
        self.corY = corY
        self.status = 'stop'  # This variable will tell if the paddles are going up, down or neither
        self.draw_paddles()

    # draw_paddles displays the paddles to the game itself
    def draw_paddles(self):
        pygame.draw.rect(self.display, self.color, (self.corX, self.corY, self.width, self.height))

    # start_move_paddles will give the velocity of which the paddles can move up and down
    def start_move_paddles(self):
        if self.status == 'up':
            self.corY = self.corY - 0.2
        elif self.status == 'down':
            self.corY = self.corY + 0.2

    # stop_on_wall will not allow the paddles to go out of boundaries
    def stop_on_wall(self):
        # Top Wall
        if self.corY <= 0:
            self.corY = 0
        # Bottom Wall
        from pong import display_height
        if self.corY + self.height >= display_height:
            self.corY = display_height - self.height

    # restart_pad_pos will reset the position of both paddles to the default position when restart
    def restart_pad_pos(self):
        from pong import display_height
        self.corY = display_height // 2 - self.height // 2
        self.status = 'stop'
        self.draw_paddles()
