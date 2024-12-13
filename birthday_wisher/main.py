import smtplib, pandas
from config import my_email, my_password, my_recipient, my_smtp

# TODO
# check for today birthday
# pick random email template
# mail merge
# send email

def send_email():
    with smtplib.SMTP(my_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_recipient, 
            msg="Subject:And yet another test!\n\nWill this work?")

# load csv

birthdays = pandas.read_csv("./birthdays.csv")
print(birthdays)