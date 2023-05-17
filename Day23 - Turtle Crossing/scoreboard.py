from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=-300,y=270)
        self.write(f"Score : {self.score}",move=False, align=ALIGMENT, font=FONT)

    def update_score(self):
        self.score +=1
        self.write_score()

    def game_over(self):
        self.write("GAME OVER",move=False, align=ALIGMENT, font=FONT)
    
