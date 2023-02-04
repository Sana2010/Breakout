from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "red", "orange", "yellow", "green", "blue"]
STRETCH_WIDTH_TURTLE = 0.8
STRETCH_HEIGHT_TURTLE = 1.8
NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 15


class BricksManager:
    def __init__(self):
        self.brick = None
        self.bricks = []
        self.number_of_rows = NUMBER_OF_ROWS
        self.number_of_columns = NUMBER_OF_COLUMNS
        self.generate_bricks()

    def generate_bricks(self):
        y_offset = 0
        for row in range(0, self.number_of_rows):
            x_offset = 0
            for column in range(0, self.number_of_columns):
                self.brick = Turtle(shape="square")
                self.brick.penup()
                self.brick.color(COLORS[row])
                self.brick.turtlesize(stretch_wid=STRETCH_WIDTH_TURTLE, stretch_len=STRETCH_HEIGHT_TURTLE)
                self.brick.goto(x=-280 + x_offset, y=330 - y_offset)
                self.bricks.append(self.brick)
                x_offset += 40
            y_offset += 20