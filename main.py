# from turtle import Screen
# from paddle import Paddle
# from ball import Ball
# import time
# from scoreboard import Scoreboard
#
#
#
#
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
#
# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()
# scoreboard = Scoreboard()
#
#
#
# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")
#
#
#
#
# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()
#  # detect colluision with wall
#
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         ball.bounce_y()
#
# #   detect collusion with paddle
#     if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
#         ball.bounce_x()
#
# #  detect ball goes out of bounds r paddle
#     if ball.xcor() >380 :
#         ball.reset_position()
#         scoreboard.l_point()
#
#     if ball.xcor() <-380 :
#         ball.reset_position()
#         scoreboard.r_point()
#
#
#
#
#
#
#
# screen.exitonclick()
from turtle import Screen
from paddle import Paddle  # Ensure Paddle class is defined correctly
from ball import Ball      # Ensure Ball class is defined correctly
import time
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Control paddles with keyboard
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when the ball goes out of bounds (right paddle misses)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Detect when the ball goes out of bounds (left paddle misses)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()

screen.exitonclick()


