import datetime as dt

now = dt.datetime.now()
day_of_the_week = now.weekday()

#wednesday is 2
if day_of_the_week == 2:
    print("today!")