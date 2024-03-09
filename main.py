import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("Black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
print(scoreboard)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_score()
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_score()
    
screen.exitonclick()
