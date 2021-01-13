import pygame


# Scoring Class
class Scoring:
    def __init__(self, display, point, corX, corY):
        from pong import color_white
        self.display = display
        self.point = point
        self.corX = corX
        self.corY = corY
        self.font = pygame.font.SysFont("monospace", 80, bold=True)  # monospace font chosen for the score text
        self.tag = self.font.render(self.point, 0, color_white)
        self.draw_score()

    # Shows the score
    def draw_score(self):
        self.display.blit(self.tag, (self.corX - self.tag.get_rect().width // 2, self.corY))

    # Adds the score by 1 to the player who scored a goal (no limit)
    def add_score(self):
        from pong import color_white
        point = int(self.point) + 1
        self.point = str(point)
        self.tag = self.font.render(self.point, 0, color_white)

    # Restart to 0 points from any points
    def game_restart(self):
        from pong import color_white
        self.point = '0'
        self.tag = self.font.render(self.point, 0, color_white)
