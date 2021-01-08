import pygame


class Collision:
    # Collision detection for when the ball hits the 1st paddle
    @staticmethod
    def ball_against_paddle1(ball, paddle1):
        if ball.corY + ball.radius > paddle1.corY and ball.corY - ball.radius < paddle1.corY + paddle1.height:
            if ball.corX - ball.radius <= paddle1.corX + paddle1.width:
                return True
        return False

    # Collision detection for when the ball hits the 2nd paddle
    @staticmethod
    def ball_against_paddle2(ball, paddle2):
        if ball.corY + ball.radius > paddle2.corY and ball.corY - ball.radius < paddle2.corY + paddle2.height:
            if ball.corX - ball.radius >= paddle2.corX:
                return True
        return False

    # Collision detection for when a ball hits the wall (top and bottom wall)
    @staticmethod
    def ball_against_wall(ball):
        # Top wall
        if ball.corY - ball.radius <= 0:
            return True
        # Bottom wall
        from pong import display_height
        if ball.corY + ball.radius >= display_height:
            return True

        return False

    # Collision detection for when the ball goes into the opponent's goal
    @staticmethod
    def goal_player1(ball):
        from pong import display_width
        return ball.corX - ball.radius >= display_width

    @staticmethod
    def goal_player2(ball):
        return ball.corX + ball.radius <= 0
