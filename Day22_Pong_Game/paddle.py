from turtle import Turtle

class Paddle:

    def __init__(self):
        self.create_paddle()

    def create_paddle(self,position):
        paddle = Turtle()
        paddle.shape("square")
        paddle.shapesize(stretch_wid=5,stretch_len=1)
        paddle.color("white")
        paddle.penup()
        paddle.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)