from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Turtle Race","Which color turtule will win")

turtles_colors = ["red","orange","yellow","green","blue","purple"]
turtles = ["tim","jim","sim","nin","mim","lil"]

y_cord = -100

for i in range(0,6):
    turtles[i] = Turtle(shape="turtle")
    turtles[i].penup()
    turtles[i].goto(x =-230,y=y_cord)
    y_cord += 35
    turtles[i].color(turtles_colors[i])


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won")
            else:
                print(f"You have lost !! Winner is {winning_color}")
        random_dist = random.randint(0,10)
        turtle.forward(random_dist)



screen.exitonclick()