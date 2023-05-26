from tkinter import *
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Read Data ------------------------------- #

try:
    data = pd.read_csv("Day31\\data\\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("Day31\\data\\french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


current_card = {}


def next_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = rand.choice(data_dict)
    learn_word = current_card['French']
    
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=f"{learn_word}")
    canvas.itemconfig(canvas_background,image=canvas_img)

    flip_timer = window.after(3000,func=flip_card)



def flip_card():
    global current_card
    translate_word = current_card['English']
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=f"{translate_word}")
    canvas.itemconfig(canvas_background,image=canvas_back_image)


def is_known():

    data_dict.remove(current_card)
    next_word()
    df_word_to_learn = pd.DataFrame(data_dict)
    df_word_to_learn.to_csv("Day31\\data\\words_to_learn.csv",index=False)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# window.after(1000)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526,highlightthickness=0)
canvas_img = PhotoImage(file="Day31\images\card_front.png")
canvas_background = canvas.create_image(400,263,image = canvas_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

card_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)

canvas_back_image = PhotoImage(file="Day31\images\card_back.png")


# Buttons

wrong_image = PhotoImage(file="Day31\\images\\wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_word)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="Day31\\images\\right.png")
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)


next_word()



window.mainloop()