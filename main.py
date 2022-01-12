from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

# -------------------UI SETUP---------------------------#
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

ball = Ball()
paddle = Paddle(0, -250)
brick = Brick()
brick.lay_bricks()
score = Scoreboard()

# -----------------PADDLE FUNCTIONALITY-----------------#

screen.listen()
screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)

# --------------------SET VARIABLES---------------------#
game_is_on = True
top_bounce = 0
bricks_hit = 0
red_hit = 0
orange_hit = 0
lives = 3
game_round = 1

# ---------------------GAME PLAY----------------------#

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect collision with top wall, increasing speed, decreasing paddle size
    if ball.ycor() > 280:
        ball.bounce_y()
        top_bounce += 1
        paddle.shrink()
        if top_bounce == 1:
            ball.double_speed()
            top_bounce += 1

    # detect collision with side walls
    if ball.xcor() < -480 or ball.xcor() > 475:
        ball.bounce_x()

    # detect collision with paddle
    if top_bounce > 0:
        if ball.distance(paddle) < 40 and ball.ycor() < -225: #adjusted distance from paddle to reflect smaller paddle size
            ball.bounce_y()
    elif ball.distance(paddle) < 60 and ball.ycor() < -225: #distance from paddle for initial size
        ball.bounce_y()

    # detect collision with bottom
    if ball.ycor() < -275:
        lives -= 1
        if lives == 0:
            score.game_over()
            game_is_on = False
        ball.reset_position()

    # detect brick collision
    for coord in brick.coordinates:
        if coord[0] - 35 < ball.xcor() < coord[0] + 35 and coord[1] + 20 > ball.ycor() > coord[1] - 20:
            brick.hide(brick.coordinates.index(coord))
            ball.bounce_y()
            bricks_hit += 1
            # calculate points to add to score
            if coord[1] > 200:
                score.add_points(7)
                red_hit += 1
            elif coord[1] > 150:
                score.add_points(5)
                orange_hit += 1
            elif coord[1] > 100:
                score.add_points(3)
            elif coord[1] > 0:
                score.add_points(1)

        # increase speed for red or orange hit
        if orange_hit == 1:
            ball.double_speed()
            orange_hit += 1
        if red_hit == 1:
            ball.double_speed()
            red_hit += 1

        # increase ball speed for total bricks hit
        if bricks_hit == 4 or bricks_hit == 11:
            ball.double_speed()
            bricks_hit += 1

        # create second screen of bricks
        if not brick.id and lives > 0:
            game_round += 1
            ball.reset_position()
            if game_round > 2:
                score.winner()
                ball.hideturtle()
                game_is_on = False
            else:
                orange_hit = 0
                red_hit = 0
                top_bounce = 0
                bricks_hit = 0
                game_round += 1
                time.sleep(1.5)
                brick.lay_bricks()

screen.exitonclick()
