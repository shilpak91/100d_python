from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(0,new_y)
        if self.ycor() == 280:
            self.goto(STARTING_POSITION)