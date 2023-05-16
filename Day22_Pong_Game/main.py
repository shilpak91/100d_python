from turtle import Screen,Turtle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Turtle()
r_paddle.shape("square")
r_paddle.shapesize(stretch_wid=5,stretch_len=1)
r_paddle.color("white")
r_paddle.goto(x=350,y=0)


screen.exitonclick()