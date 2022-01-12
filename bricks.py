from turtle import Turtle

class Brick(Turtle):

    def __init__(self,):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=3)
        self.ht()
        self.id = []
        self.coordinates = []
        self.colors = ["red", "orange","green","yellow"]

    def lay_bricks(self):
        self.goto(-455, 250)
        for color in self.colors:
            self.color(color)
            for n in range(0, 12):
                self.id.append(self.stamp())
                self.coordinates.append((self.xcor(), self.ycor()))
                self.goto(self.xcor() + 75, self.ycor())
            self.id.append(self.stamp())
            self.coordinates.append((self.xcor(), self.ycor()))
            self.goto(self.xcor(), self.ycor() - 25)
            for n in range(0, 12):
                self.id.append(self.stamp())
                self.coordinates.append((self.xcor(), self.ycor()))
                self.goto(self.xcor() - 75, self.ycor())
            self.id.append(self.stamp())
            self.coordinates.append((self.xcor(), self.ycor()))
            self.goto(self.xcor(), self.ycor() - 25)


    def hide(self, index):
        self.clearstamp(self.id[index])
        del self.id[index]
        del self.coordinates[index]

