from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
screen = Screen()
screen.colormode(255)

colors = colorgram.extract('images.jpg',30)
print(colors)

screen.exitonclick()