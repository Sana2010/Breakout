from turtle import Turtle

STRETCH_LEN = 10
STRETCH_WID = 1


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_width = None
        self.stretch_wid = None
        self.stretch_len = None

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.stretch_len = STRETCH_LEN
        self.stretch_wid = STRETCH_WID
        self.penup()
        self.shapesize(stretch_wid=self.stretch_wid, stretch_len=self.stretch_len)
        self.paddle_width = 20 * STRETCH_LEN
        self.goto(position)

    def go_left(self):
        if self.xcor() - self.paddle_width / 2 - 20 >= -300:
            new_x = self.xcor() - 20
            self.goto(x=new_x, y=self.ycor())

    def go_right(self):
        if self.xcor() + self.paddle_width / 2 + 20 <= 300:
            new_x = self.xcor() + 20
            self.goto(x=new_x, y=self.ycor())

    def shorten_paddle(self):
        if self.stretch_len == STRETCH_LEN:
            self.stretch_len /= 2
            self.shapesize(stretch_wid=self.stretch_wid, stretch_len=self.stretch_len)