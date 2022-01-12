from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 32, "normal"))

    def add_points(self, points):
        self.score += points
        self.update_scoreboard()

    def winner(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"WINNER! You've reached the maximum score of {self.score}!",
                   align="center",
                   font=("Courier", 32, "normal"))

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER. Your score is {self.score}.", align="center", font=("Courier", 32, "normal"))

