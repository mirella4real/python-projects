import datetime as dt
import random
import smtplib
from config import my_email, my_password, my_recipient, my_smtp

SUBJECT = "Motivational Quote"
GREETING = "Hello Mirella!\nHere is your weekly motivational quote:"
now = dt.datetime.now()
day_of_the_week = now.weekday()
quotes_list = []

def load_quotes():
    global quotes_list
    try:
        with open("./quotes.txt", "r") as file:
            quotes_list = [line.strip() for line in file]
    except:
      quotes_list.append("All out of motivation today - Mirella Batista")

def get_random_quote():
    quote = ""
    if len(quotes_list) == 0:
        load_quotes()
    quote = random.choice(quotes_list)
    return quote

def send_email(quote):
    with smtplib.SMTP(my_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_recipient, 
            msg=f"Subject:{SUBJECT}\n\n{GREETING}\n{quote}")

#wednesday is 2
if day_of_the_week == 2:
    quote_of_the_day = get_random_quote()
    send_email(quote_of_the_day)
    