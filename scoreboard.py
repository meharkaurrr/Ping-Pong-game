from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.scoreboard_score()

    def scoreboard_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_point, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_point, align="center", font=("courier", 80, "normal"))

    def l_score(self):
        self.l_point += 1
        self.scoreboard_score()

    def r_score(self):
        self.r_point += 1
        self.scoreboard_score()
