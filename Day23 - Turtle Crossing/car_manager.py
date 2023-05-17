from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_COR = random.randrange(-300,280,20)
X_COR = 300

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(X_COR,Y_COR)
        self.setheading(180)
        self.move_speed = 0.1
    
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
    
    def speed_up(self):
        self.move_speed *= 0.9
