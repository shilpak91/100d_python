from turtle import Screen
from paddle import Paddle
from ball import Ball

STARTING_POSITIONS = [(350,0),(-350,0)]

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")



game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()