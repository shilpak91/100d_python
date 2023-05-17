from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(x=-220,y=260)
        self.write(f"level : {self.level}",move=False, align=ALIGMENT, font=FONT)

    def update_level(self):
        self.level +=1
        self.write_level()

    def game_over(self):
        self.write("GAME OVER",move=False, align=ALIGMENT, font=FONT)
    
