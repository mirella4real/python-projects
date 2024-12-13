import smtplib, pandas, datetime, random
from config import my_email, my_password, my_recipient, my_smtp
PLACEHOLDER = "[NAME]"


def send_email(letter, recipient_email):
    """
    Sends an email with the given letter content to the specified recipient.

    Args:
        letter (str): The content of the email to be sent.
        recipient_email (str): The email address of the recipient.

    Returns:
        None
    """
    with smtplib.SMTP(my_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=recipient_email, 
            msg=f"Subject:Happy Birthday!\n\n{letter}")
        
def get_birthdays(current_month, current_date):
    """
    Retrieves a list of birthdays that match the given month and date.

    Args:
        current_month (int): The current month to match against the birthdays.
        current_date (int): The current date to match against the birthdays.

    Returns:
        list: A list of lists, where each inner list contains the name, email, year, month, and day of a person whose birthday matches the given month and date.
    """
    birthdays_list = []
    birthdays = pandas.read_csv("./birthdays.csv")
    for index, rows in birthdays.iterrows():
        if rows["month"] == current_month and rows["day"] == current_date:
            current_bday = [rows["name"], rows["email"], rows["year"], rows["month"], rows["day"]]
            birthdays_list.append(current_bday)
    return birthdays_list

def get_birthday_letter():
    """
    Selects a random birthday letter template from the 'letter_templates' directory and returns its content.

    The function randomly selects one of three letter templates (letter_1.txt, letter_2.txt, or letter_3.txt)
    and reads its content.

    Returns:
        str: The content of the randomly selected birthday letter template.
    """
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