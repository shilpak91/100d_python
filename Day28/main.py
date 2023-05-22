from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    counter_label.config(text="")
    global reps 
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",font=(FONT_NAME,30,"bold"),fg=RED,bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",font=(FONT_NAME,30,"bold"),fg=PINK,bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global reps

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
        # count_min = f"0{count_min}"
    
    if count_min < 10:
        count_min = f"0{count_min}"
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()

        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔"
        counter_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


window.after(1000,)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="Day28\\tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)



timer_label = Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

counter_label = Label(text="",fg=GREEN,bg=YELLOW)
counter_label.grid(column=1,row=3)


window.mainloop()