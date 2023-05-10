from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
screen = Screen()
screen.colormode(255)

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



# Draw random walk

# timmy.pensize(15)
# timmy.speed("fastest")

# direction = [0,90,180,270]

# for i in range(0,200):
#     timmy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#     timmy.setheading(random.choice(direction))
#     timmy.forward(30)

# Draw a Spirograph

timmy.speed("fastest")
def draw_spirograph(gap):
    for i in range(int(360/gap)):
        timmy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        timmy.circle(100)
        timmy.left(gap)

draw_spirograph(5)

screen.exitonclick()

