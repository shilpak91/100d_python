from turtle import Turtle,Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
screen = Screen()
screen.colormode(255) # See  documentation

# Moving Turtle in a square
# for i in range(4): 
#     timmy.forward(100)
#     timmy.left(90)

# Creating a dotted line
# for i in range(100):
#     timmy.forward(2)
#     timmy.penup()
#     timmy.forward(2)
#     timmy.pendown()

# Draw a triangle, square,pentagon,hexagon,heptagon,octagon,nonagon and decagon

# for i in (range(3,11)):
#     timmy.pencolor((random.randint(0,255)
#                     ,random.randint(0,255)
#                     ,random.randint(0,255)))
#     for j in (range(0,i)):
#         timmy.forward(100)
#         timmy.left(360/i)



# Draw random line and random color and ransom direction

timmy.pensize(15)

for i in range(0,100):
    timmy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    coin = random.randrange(0,2)
    if coin ==0:
        timmy.right(90)
    else:
        timmy.left(90)
    timmy.forward(10)


screen.exitonclick()

