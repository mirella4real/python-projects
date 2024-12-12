import datetime as dt
import random

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

#wednesday is 2
if day_of_the_week == 2:
    quote_of_the_day = get_random_quote()
    print(quote_of_the_day)