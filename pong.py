# Name   : Ida Bagus Ryogassa Avatara
# ID     : 2440100323
# Project: Pong Game with PyGame (2 players)

# Tutorial: Paddle 1 (left) will be controlled with w and s key.
#           Paddle 2 (right) will be controlled with up and down key.
#           To start a game, press p.
#           To reset the game, press r.
#           To exit, press the exit button.

# #### MAIN ######

import pygame
import sys
import winsound
from ball import Ball
from paddles import Paddles
from collision import Collision
from scoring import Scoring

# Initialize PyGame
pygame.init()

# Display the Width and Height of Screen
display_width = 900
display_height = 500

# RGB = Red, Green, Blue
color_black = (0, 0, 0)
color_white = (255, 255, 255)

# Sets the Display size
display = pygame.display.set_mode((display_width, display_height))
# Sets the game of the game on the top left hand corner
pygame.display.set_caption('Pong (with PyGame)')


# Fills the background color with the chosen color (black) and creates a line in the middle of the screen depending on the width and height of display/screen
# Calculations was needed for this part
def background_color():
    display.fill(color_black)
    pygame.draw.line(display, color_white, (display_width // 2, 0), (display_width // 2, display_height), 5)


# Every position of ball and paddles, and player score will restart to default settings
def restart():
    background_color()
    player1_score.game_restart()
    player2_score.game_restart()
    display_ball.restart_ball_pos()
    display_paddle1.restart_pad_pos()
    display_paddle2.restart_pad_pos()


background_color()

# MAIN
if __name__ == "__main__":
    # GAME OBJECTS
    display_ball = Ball(display, color_white, display_width // 2, display_height // 2, 10)  # <display_ball> will create the ball itself into the game (calculations was needed for this part)
    display_paddle1 = Paddles(display, color_white, 15, display_height // 2 - 60, 20, 120)  # <display_paddle#> will create the paddles into the game (calculations was needed for this part)
    display_paddle2 = Paddles(display, color_white, display_width - 20 - 15, display_height // 2 - 60, 20, 120)
    # Calls the collision class as collisionMechanics
    collisionMechanics = Collision()
    # Calls the scoring class as player1_score and player2_score
    # It also sets where the points for each player will be displayed
    player1_score = Scoring(display, '0', display_width // 4, 15)
    player2_score = Scoring(display, '0', display_width - display_width // 4, 15)
    running = False

    # MAIN LOOP FOR GAME (Calling all Function/methods in all classes)
    while True:
        for choice in pygame.event.get():

            if choice.type == pygame.QUIT:
                sys.exit()

            if choice.type == pygame.KEYDOWN:
                # Game will start with p key
                if choice.key == pygame.K_p:
                    display_ball.start_move_ball()
                    running = True
                # Game will reset the game with r key
                if choice.key == pygame.K_r:
                    restart()
                    running = False

                # PADDLE MOVEMENTS
                # Up Movement with w key for paddle 1
                if choice.key == pygame.K_w:
                    display_paddle1.status = 'up'
                # Down Movement when s key for paddle 1
                if choice.key == pygame.K_s:
                    display_paddle1.status = 'down'
                # Up Movement with up key for paddle 2
                if choice.key == pygame.K_UP:
                    display_paddle2.status = 'up'
                # Down Movement with down key for paddle 2
                if choice.key == pygame.K_DOWN:
                    display_paddle2.status = 'down'
            # Paddle will stop moving when no movement keys are being pressed
            if choice.type == pygame.KEYUP:
                display_paddle1.status = 'stop'
                display_paddle2.status = 'stop'
        # if Running = True then everything in the loop will be called
        if running:
            background_color()
            # Ball movement
            display_ball.ball_movement()
            display_ball.draw_ball()

            # Paddle 1 Movement
            display_paddle1.start_move_paddles()
            display_paddle1.stop_on_wall()
            display_paddle1.draw_paddles()
            # Paddle 2 Movement
            display_paddle2.start_move_paddles()
            display_paddle2.stop_on_wall()
            display_paddle2.draw_paddles()

            # Collision
            if collisionMechanics.ball_against_paddle1(display_ball, display_paddle1):
                display_ball.collision_with_paddle()
                winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

            if collisionMechanics.ball_against_paddle2(display_ball, display_paddle2):
                display_ball.collision_with_paddle()
                winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

            if collisionMechanics.ball_against_wall(display_ball):
                display_ball.collision_with_wall()
                winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

            if collisionMechanics.goal_player1(display_ball):
                background_color()
                player1_score.add_score()
                display_ball.restart_ball_pos()
                display_paddle1.restart_pad_pos()
                display_paddle2.restart_pad_pos()
                running = False

            if collisionMechanics.goal_player2(display_ball):
                background_color()
                player2_score.add_score()
                display_ball.restart_ball_pos()
                display_paddle1.restart_pad_pos()
                display_paddle2.restart_pad_pos()
                running = False

        # Displays the points for each player
        player1_score.draw_score()
        player2_score.draw_score()

        pygame.display.update()
