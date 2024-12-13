import smtplib, pandas, datetime, random
from config import my_email, my_password, my_recipient, my_smtp
PLACEHOLDER = "[NAME]"

# TODO
# check for today birthday
# pick random email template
# mail merge
# send email

def send_email(letter, recipient_email):
    with smtplib.SMTP(my_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=recipient_email, 
            msg=f"Subject:Happy Birthday!\n\n{letter}")
        
def get_birthdays(current_month, current_date):
    birthdays_list = []
    birthdays = pandas.read_csv("./birthdays.csv")
    for index, rows in birthdays.iterrows():
        if rows["month"] == current_month and rows["day"] == current_date:
            current_bday = [rows["name"], rows["email"], rows["year"], rows["month"], rows["day"]]
            birthdays_list.append(current_bday)
    return birthdays_list

def get_birthday_letter():
    letter = f"letter_{random.randint(1,3)}"
    with open(f"./letter_templates/{letter}.txt") as letter_file:
        letter_template = letter_file.read()
    return letter_template

now = datetime.datetime.now()
birthdays_list = get_birthdays(now.month, now.day)
if len(birthdays_list) > 0:
    for birthday in birthdays_list:
        birthday_letter_template = get_birthday_letter()
        letter = birthday_letter_template.replace(PLACEHOLDER, birthday[0])
        send_email(letter, birthday[1])