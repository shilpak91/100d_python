from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

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
        self.goto(x=0,y=270)
        self.write(f"Score : {self.score}",move=False, align=ALIGMENT, font=FONT)

    def update_score(self):
        self.score +=1
        self.write_score()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER",move=False, align=ALIGMENT, font=FONT)


