from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


