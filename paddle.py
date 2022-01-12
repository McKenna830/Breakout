from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):  # creates and displays the paddle
        super().__init__()  # Paddle inherits from Turtle
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.turtlesize(stretch_wid=1, stretch_len=6)
        self.st()

    def move_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def shrink(self):
        self.turtlesize(stretch_wid=1, stretch_len=3)

