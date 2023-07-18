from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage

TARGET_PRICE = 350.00

sender_email = "shilpakraichpython@gmail.com"
sender_password = "cvraeiwsbakyhbdk"
receiver_email = "shilpakraich91@gmail.com"


amazon_url = "https://www.amazon.nl/-/en/WH-1000XM5-Cancelling-Wireless-Headphones-Built/dp/B09Y2MYL5C/ref=sr_1_5?keywords=sony%2Bwh-1000xm5&qid=1689705124&sprefix=sony%2Caps%2C87&sr=8-5&th=1"

response = requests.get(url=amazon_url)
amazon_html = response.text

# print(amazon_html)

soup = BeautifulSoup(amazon_html,"html.parser")
current_price = float(soup.find("span",class_="a-offscreen").text[1:])
# print(current_price)

# Send email
msg = EmailMessage()
msg['Subject'] = "Amazon Price Drop Alert"
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content(f"Price dropped for {amazon_url} to {current_price}")

if current_price < TARGET_PRICE:

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email,password=sender_password)
        connection.send_message(msg)