##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import os
import smtplib
import random as rand
import pandas as pd

my_email = "shilpakraichpython@gmail.com"
my_password = "cvraeiwsbakyhbdk"
now = dt.datetime.now()
today = now.day
month = now.month

letter_templates = os.listdir("/Users/shilpak/Documents/Code100/100d_python/Day32/birthday-wisher-extrahard-start/letter_templates")
selected_letter = rand.choice(letter_templates)

def pick_message():
        with open(f"/Users/shilpak/Documents/Code100/100d_python/Day32/birthday-wisher-extrahard-start/letter_templates/{selected_letter}") as letter:
            message = letter.read()
            message = message.replace("Angela","Shilpak-Python")
            return(message)

def send_email(to_email,from_email,message):

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email,
                            msg=f"Subject: Happy Birthday\n\n{message}")


df_birthday = pd.read_csv("/Users/shilpak/Documents/Code100/100d_python/Day32/birthday-wisher-extrahard-start/birthdays.csv")

# dataframe with month and day matching today
result_df = df_birthday[(df_birthday["day"]==today) & (df_birthday["month"]==month)]

birthday_dict = result_df.to_dict(orient="records") # Gives list of dict

for dict in birthday_dict:
    birthday_name = dict["name"]
    birthday_email = dict["email"]
    birthday_message = pick_message()
    birthday_message = birthday_message.replace("[NAME]",f"{birthday_name}")
    send_email(birthday_email,my_email,birthday_message)

    
    






    