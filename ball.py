import pygame


# Ball Class
class Ball:
    def __init__(self, display, color, corX, corY, radius):
        self.color = color
        self.display = display
        self.radius = radius
        self.corX = corX
        self.corY = corY
        self.bX = 0  # bX and bY will tell us how the ball is moving through x and y coordinates/positions
        self.bY = 0
        self.draw_ball()

    # draw_ball displays the ball to the game itself
    def draw_ball(self):
        pygame.draw.circle(self.display, self.color, (self.corX, self.corY), self.radius)

    # start_move_ball will be called as soon as we press the starting key which is the ENTER Key
    # this will give the velocity of the ball
    def start_move_ball(self):
        self.bX = 0.20
        self.bY = 0.20

    # ball_movement is responsible from moving the ball
    def ball_movement(self):
        self.corX = self.corX + self.bX
        self.corY = self.corY + self.bY

    # collision_with_paddle is responsible for the ball to move after hitting a paddle
    def collision_with_paddle(self):
        self.bX = -self.bX

    # collision_with_wall is responsible for the ball to move after hitting a wall
    def collision_with_wall(self):
        self.bY = -self.bY

    # restart_ball_pos will reset the position of the ball to the default position when restart
    def restart_ball_pos(self):
        from pong import display_width, display_height
        self.corX = display_width // 2
        self.corY = display_height // 2
        self.bX = 0
        self.bY = 0
        self.draw_ball()
