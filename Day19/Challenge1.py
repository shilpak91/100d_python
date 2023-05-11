from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(5)

def move_backward():
    tim.backward(5)

def move_clockwise():
    tim.right(5)

def move_anticlockwise():
    tim.left(5)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun = move_forward)
screen.onkey(key="s",fun = move_backward)
screen.onkey(key="a",fun = move_anticlockwise)
screen.onkey(key="d",fun = move_clockwise)
screen.onkey(key="c",fun = clear_screen)


screen.exitonclick()