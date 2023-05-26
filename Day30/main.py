from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = random.randint(8,10) 
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_l = [random.choice(letters) for letter in range(0,nr_letters)]
    password_s = [random.choice(symbols) for symbol in range(0,nr_symbols)]
    password_n = [random.choice(numbers) for number in range(0,nr_numbers)]

    password = password_l + password_s + password_n

    random.shuffle(password)

    password = ''.join(password)

    pass_input.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_button():

    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {website : {email : password}}

    if len(website) > 0 and len(password) > 0:

        # is_ok = messagebox.askokcancel(title={website_input.get()}
        #                     ,message=f"These are the details entered : \n Email: {email_input.get()} \nPassword :{pass_input.get()} \n Is it ok to Save ?")
        # if is_ok :
        try:
            with open("Day30\\data.json",mode="r") as data_file:
                # Reading Old data
                data = json.load(data_file)

        except FileNotFoundError:
                with open("Day30\\data.json",mode="w") as data_file:
                # Saving updated data
                    json.dump(new_data,data_file,indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("Day30\\data.json",mode="w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_input.delete(0,END)
            pass_input.delete(0,END)
    else:
        messagebox.showinfo(title="Oops",message="Please dont leave any fields empty!!")


# ---------------------------- Search Password ------------------------------- #

def find_password():

    website = website_input.get()
    email = email_input.get()

    try:
        with open("Day30\\data.json",mode="r") as data_file:
            data = json.load(data_file)
            password = data[website][email]

            messagebox.showinfo(title="Information",message=f"Website : {website}\n Email: {email}\n Password: {password}")
    
    except FileNotFoundError:
        messagebox.showinfo(title="Warning",message="File not found, please add data to create a file!!")
    
    except KeyError:
        messagebox.showinfo(title="Warning",message=f"{website} not found , please add data  !!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

window.after(1000)

canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file="Day29\\logo.png")
canvas.create_image(140,100,image = logo_img)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3,column=0)


# Entry

website_input = Entry(width=32)
website_input.grid(row=1,column=1)
website_input.focus()


email_input = Entry(width=57)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"shilpakraich91@gmail.com")

pass_input = Entry(width=32)
pass_input.grid(row=3,column=1)

# Buttons

pass_button = Button(text="Generate Password",width=20,command=generate_password)
pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=48,command=add_button)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=20,command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()