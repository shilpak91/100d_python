import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
cars = []

for car in range(1,10):
    car = CarManager()
    cars.append(car)

screen.listen()
screen.onkey(turtle.up,"Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Has turtle reach the finish line
    if turtle.ycor() ==280:
        turtle.reset_position()
        scoreboard.update_level()
        for car in cars:
            car.speed_up()
    
    for car in cars:
        car.move()


screen.exitonclick()