from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.move_x = 10
        self.move_y = 10

    def ball_move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.penup()
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
