from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        print(self.xcor())
        new_y = self.ycor() + 20
        x = self.xcor()
        self.goto(x, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        x = self.xcor()
        self.goto(x, new_y)
