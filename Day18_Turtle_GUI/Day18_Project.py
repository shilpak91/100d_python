from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
screen = Screen()
screen.colormode(255)

# colors = colorgram.extract('Day18_Turtle_GUI\Image1.jpg',30)
# rgb_colors = []
# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(241, 237, 229), (236, 238, 244), (244, 237, 242), (235, 243, 238), (183, 162, 134), (125, 92, 73), (81, 93, 115), (148, 161, 179), (177, 153, 162), (208, 206, 140), (29, 35, 48), (117, 83, 95), (52, 24, 32), (148, 168, 
154), (47, 26, 20), (85, 105, 90), (157, 152, 69), (105, 37, 49), (24, 33, 30), (50, 58, 91), (163, 110, 102), (210, 180, 190), (112, 40, 33), (156, 110, 120), (111, 123, 152), (215, 181, 175), (182, 188, 207), (108, 142, 114), (176, 201, 187), (70, 71, 38)]


timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100


for dot_count in range(1,number_of_dots +1):
    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen.exitonclick()