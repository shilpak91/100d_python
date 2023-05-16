from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write("Score :",move=False, align='left', font=('Arial', 8, 'normal'))
