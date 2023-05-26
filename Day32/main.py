import smtplib

my_email = "shilpakraichpython@gmail.com"
my_password = "cvraeiwsbakyhbdk"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="shilpakraich91@gmail.com",
                        msg="Subject: Hello\n\n This is body of email")