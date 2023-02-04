from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
from bricks import BricksManager
import time

LIVES = 3

screen = Screen()
screen.setup(width=640, height=840)
screen.bgcolor("black")
screen.title("Breakout arcade game")
screen.tracer(0)
screen.listen()

game_is_on = True

scoreboard = Scoreboard()

paddle = Paddle()
paddle.create_paddle((0, -350))
screen.onkey(paddle.go_left, "Left")
screen.onkeypress(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkeypress(paddle.go_right, "Right")

ball = Ball()

bricks_manager = BricksManager()

first_orange = True
first_red = True

while game_is_on:
    time.sleep(0.001)
    screen.update()

    ball.move()
    ball.collision_with_x()

    if ball.collision_with_upper_y():
        paddle.shorten_paddle()

    if ball.collision_with_lower_y(LIVES):
        LIVES -= 1
        scoreboard.refresh_score(LIVES)
        paddle.goto(0, -350)
        time.sleep(2)

    ball.collision_with_paddle(paddle)
    hit = False

    for brick in bricks_manager.bricks:
        if ((ball.ycor() >= brick.ycor() - 10) and (ball.ycor() <= brick.ycor() + 10)) and (
                (ball.xcor() >= brick.xcor() - 30) and (ball.xcor() <= brick.xcor() + 30)):
            brick.hideturtle()
            scoreboard.add_score(brick.color()[0], LIVES)
            ball.x_move *= -1
            bricks_manager.bricks.remove(brick)
            hit = True

        elif ((ball.xcor() >= brick.xcor() - 20) and (ball.xcor() <= brick.xcor() + 20)) and (
                (ball.ycor() >= brick.ycor() - 20) and (ball.ycor() <= brick.ycor() + 20)):
            brick.hideturtle()
            scoreboard.add_score(brick.color()[0], LIVES)
            ball.y_move *= -1
            bricks_manager.bricks.remove(brick)
            hit = True

        if brick.color()[0] == "orange" and first_orange and hit:
            first_orange = False
            ball.increase_speed()
        elif brick.color()[0] == "red" and first_red and hit:
            first_red = False
            ball.increase_speed()

    if (len(bricks_manager.bricks) == 116) and hit:
        ball.increase_speed()
        hit = False
    elif (len(bricks_manager.bricks) == 108) and hit:
        ball.increase_speed()
        hit = False

    if not bricks_manager.bricks:
        game_is_on = False
        scoreboard.game_over_win()
    elif LIVES == 0:
        scoreboard.game_over_lose()
        game_is_on = False

screen.exitonclick()