from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.refresh_score(lives=3)

    def create_line(self):
        self.goto(x=-300, y=-400)
        self.pendown()
        self.width(4)
        self.goto(x=-300, y=360)
        self.goto(x=300, y=360)
        self.goto(x=300, y=-400)
        self.penup()

    def refresh_score(self, lives):
        self.clear()
        self.create_line()
        self.goto(x=250, y=370)
        self.write(self.score, font=('Arial', 18, 'normal'))
        self.goto(x=-250, y=370)
        self.write(f"lives:{lives}", font=('Arial', 18, 'normal'))

    def add_score(self, color, lives):
        if color == "yellow":
            self.score += 1
        elif color == "green":
            self.score += 3
        elif color == "orange":
            self.score += 5
        elif color == "red":
            self.score += 7
        self.refresh_score(lives)

    def game_over_lose(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=('Arial', 32, 'normal'))

    def game_over_win(self):
        self.goto(x=0, y=0)
        self.write(f"You win!!!\nYour score was: {self.score}", align="center", font=('Arial', 32, 'normal'))