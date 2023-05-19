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
        with open("Day20-21_Snake_Game/data.txt") as data:
            self.high_score = int(data.read())
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=0,y=270)
        self.write(f"Score : {self.score} High Score : {self.high_score}",move=False, align=ALIGMENT, font=FONT)

    def update_score(self):
        self.score +=1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day20-21_Snake_Game/data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()
  



    # def game_over(self):
    #     self.goto(x=0,y=0)
    #     self.write("GAME OVER",move=False, align=ALIGMENT, font=FONT)


