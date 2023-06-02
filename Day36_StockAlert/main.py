import requests
import datetime as dt

import smtplib

my_email = "shilpakraichpython@gmail.com"
my_password = "cvraeiwsbakyhbdk"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "9DWX7W9Q64YQNBC4"
NEWS_API = "9a60fcfe6cb5482f90583ec933f631c2"

now = dt.datetime.today()
yesterday = now.date() + dt.timedelta(days=-1)
# day_before_yesterday = now.date() + dt.timedelta(days=-2)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# 9DWX7W9Q64YQNBC4

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={STOCK_API}'
r = requests.get(url)
data = r.json()

data_list = list(data["Time Series (60min)"].keys())
# print(data_list[0])
# print(data_list[16])
yes_closing_price = float(data["Time Series (60min)"][data_list[0]]["4. close"])
dfy_closing_price = float(data["Time Series (60min)"][data_list[16]]["4. close"])

value_change = round((yes_closing_price - dfy_closing_price)/yes_closing_price * 100,2) 
if value_change > 0:
    value_change_str = (f"🔺" + str(value_change) + "%")
else:
    value_change_str = (f"🔻" + str(value_change) + "%")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
# 9a60fcfe6cb5482f90583ec933f631c2

news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={yesterday}&sortBy=publishedAt&apiKey={NEWS_API}"
# print(news_url)
result = requests.get(news_url)
data_news = result.json()
top_news = data_news["articles"][0:3]

final_news = ""

for news in top_news:

    news_title = news["title"]
    news_desc = news["description"]
    news = (f"""
    {COMPANY_NAME} : {value_change_str}
    Headline : {news_title} 
    Brief : {news_desc}
    """)

    final_news += news

print(final_news)


if value_change > 3:
    # print("Get News")
    # get news below and send email
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="shilpakraich91@gmail.com",
                            msg=f"Subject: {COMPANY_NAME} Alert\n\n {final_news}")


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

