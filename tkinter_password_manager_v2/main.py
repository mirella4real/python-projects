from tkinter import *
from tkinter import messagebox
from passwordgenerator import PasswordGenerator
import pyperclip
import json

COMMONLY_USED_EMAIL = "myemail@email.com"
STR_TITLE = "Password Manager"
STR_WEBSITE = "Website"
STR_EMAIL_UNAME = "Email/Username"
STR_PWD = "Password"
STR_GEN_PWD = "Generate Password"
STR_SEARCH = "Search"
STR_SEARCH_NOT_FOUND = "Website not found."
STR_SEARCH_EPTY_FIELD = "Please enter a website to search."
STR_ADD = "Add"
STR_CONFIRM = "Please confirm the details entered."
STR_ASK_SAVE = "Is it ok to save?"
STR_WARN_EMPTY_FIELDS = "Please don't leave any fields empty!"
COLOR_WHITE = "#ffffff"
COLOR_BLACK = "#000000"
FONT_NAME = "Courier"
FONT_SIZE = 14

def find_password():
    website = input_website.get()
    if len(website) == 0:
        messagebox.showinfo(title="", message=STR_SEARCH_EPTY_FIELD)
    else:
        try:
            with open("data.json", mode="r") as file:
                # load saved data
                saved_creds = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="", message=STR_SEARCH_NOT_FOUND)
        else:
            if website in saved_creds:
                password = saved_creds[website]["password"]
                email = saved_creds[website]["email"]
                pyperclip.copy(password)
                messagebox.showinfo(title="", message=f"Login credentials for {website} \n\nEmail: {email}\n Password: {password} \n\nPassword has been coppied to the clipboard.")

            else:
                messagebox.showinfo(title="", message=STR_SEARCH_NOT_FOUND)

def save():
    website = input_website.get()
    email = input_email_username.get()
    pwd = input_pwd.get()

    if len(email) == 0 or len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="", message=STR_WARN_EMPTY_FIELDS)
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"{STR_CONFIRM} \nWebsite: {website}\nEmail: {email} \nPassword: {pwd} \n{STR_ASK_SAVE}")
        if is_ok:
            save_to_json(website, email, pwd)
            delete_input_values()

def save_to_json(website: str, email: str, pwd: str):
    new_entry = {
        website: {
            "email": email,
            "password": pwd
        }
    }
    try:
        with open("data.json", mode="r") as file:
            # load saved data
            saved_creds = json.load(file)
    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(new_entry, file, indent=4)
    else:
        # apped saved data with new data
        saved_creds.update(new_entry)
        with open("data.json", mode="w") as file:
            # save updated data
            json.dump(saved_creds, file, indent=4)
    

def gen_pwd():
    pwd = PasswordGenerator.generate_pwd()
    input_pwd.delete(0, END)
    input_pwd.insert(0, pwd)
    pyperclip.copy(pwd)

def delete_input_values():
    input_website.delete(0, END)
    input_pwd.delete(0, END)

# building the UI using Tkinter
app_window = Tk()
app_window.title(STR_TITLE)
app_window.config(padx=20, pady=20, bg=COLOR_WHITE)

app_canvas = Canvas(width=200, height=200, bg=COLOR_WHITE, highlightthickness=0)
app_logo_image = PhotoImage(file="./logo.png")
app_canvas.create_image(100, 102, image=app_logo_image)
app_canvas.grid(column=1, row=0)

# website
label_website = Label(text=STR_WEBSITE, font=(FONT_NAME, FONT_SIZE, "normal"), fg=COLOR_BLACK, bg=COLOR_WHITE)
label_website.grid(column=0, row=1, sticky="NW")
input_website = Entry(width=21)
input_website.focus()
input_website.grid(column=1, row=1, sticky="NW")

# search
button_search = Button(text=STR_SEARCH, highlightbackground=COLOR_WHITE, command=find_password)
button_search.grid(column=2, row=1, sticky="NW", ipadx=38)

# email/username
label_email_username = Label(text=STR_EMAIL_UNAME, font=(FONT_NAME, FONT_SIZE, "normal"), fg=COLOR_BLACK, bg=COLOR_WHITE)
label_email_username.grid(column=0, row=2, sticky="NW")
input_email_username = Entry(width=38)
input_email_username.insert(0, string=COMMONLY_USED_EMAIL)
input_email_username.grid(column=1, row=2, columnspan=2, sticky="NW")

# password
label_pwd = Label(text=STR_PWD, font=(FONT_NAME, FONT_SIZE, "normal"), fg=COLOR_BLACK, bg=COLOR_WHITE)
label_pwd.grid(column=0, row=3, sticky="NW")
input_pwd = Entry(width=21)
input_pwd.grid(column=1, row=3, sticky="NW")

# generate password
button_gen_pwd = Button(text=STR_GEN_PWD, highlightbackground=COLOR_WHITE, command=gen_pwd)
button_gen_pwd.grid(column=2, row=3, sticky="NW")

# add password
button_add = Button(text=STR_ADD, highlightbackground=COLOR_WHITE, width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="NW")

app_window.mainloop()