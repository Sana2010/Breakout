from turtle import Turtle

LIVES = 3

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.lives = LIVES
        self.x_move = 5
        self.y_move = 5
        self.goto(0, -330)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def collision_with_x(self):
        if self.xcor() >= 280 or self.xcor() <= -280:
            self.x_move *= -1

    def collision_with_upper_y(self):
        if self.ycor() >= 360:
            self.y_move *= -1
            return True
        return False

    def collision_with_lower_y(self, lives):
        if self.ycor() <= -380:
            self.goto(0, -300)
            self.y_move *= -1
            return True
        return False

    def collision_with_paddle(self, paddle):
        if ((self.ycor() <= -330) and (self.ycor() > -350)) and (self.distance(paddle) < (paddle.paddle_width / 2) - 5):
            self.y_move *= -1

    def increase_speed(self):
        self.x_move += 2
        self.y_move += 2