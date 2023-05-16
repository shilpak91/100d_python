from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=0,y=280)
        self.write("Score : ",move=False, align='left', font=('Arial', 8, 'normal'))
        self.goto(x=50,y=280)
        self.write(self.score,move=False, align='left', font=('Arial', 8, 'normal'))

    def update_score(self):
        self.score +=1
        self.write_score()
