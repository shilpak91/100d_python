import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")

image = "Day25/us-states-game/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Day25/us-states-game/50_states.csv")
all_states = data.state.to_list()


# print(answer_state)

score = 0
game_is_on = True
state_font = ("Courier", 12, "normal")
aligment = "center"

guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",prompt="Whats another state name ?").title()

    if answer_state =="Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day25/us-states-game/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_df = data[data.state == answer_state]
        t.goto(int(state_df.x),int(state_df.y))
        t.write(state_df.state.item())
    
    turtle.mainloop()
