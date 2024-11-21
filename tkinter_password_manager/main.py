from tkinter import *
from tkinter import messagebox
import pyperclip
from passwordgenerator import generate_pwd

COMMONLY_USED_EMAIL = "myemail@email.com"
STR_TITLE = "Password Manager"
STR_WEBSITE = "Website"
STR_EMAIL_UNAME = "Email/Username"
STR_PWD = "Password"
STR_GEN_PWD = "Generate Password"
STR_ADD = "Add"
STR_CONFIRM = "Please confirm the details entered."
STR_ASK_SAVE = "Is it ok to save?"
STR_WARN_EMPTY_FIELDS = "Please don't leave any fields empty!"
COLOR_WHITE = "#ffffff"
COLOR_BLACK = "#000000"
FONT_NAME = "Courier"

def save():
    website = input_website.get()
    email = input_email_username.get()
    pwd = input_pwd.get()

    if len(email) == 0 or len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Missing inf", message=STR_WARN_EMPTY_FIELDS)
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"{STR_CONFIRM} \nWebsite: {website}\nEmail: {email} \nPassword: {pwd} \n{STR_ASK_SAVE}")
        
        if is_ok:
            data_string = f"{website} | {email} | {pwd}\n"
            with open("data.txt", mode="a") as file:
                file.write(f"{data_string}")
            delete_input_values()

def gen_pwd():
    pwd = string=generate_pwd()
    input_pwd.delete(0, END)
    input_pwd.insert(0, pwd)
    pyperclip.copy(pwd)

def delete_input_values():
    input_website.delete(0, END)
    input_pwd.delete(0, END)

app_window = Tk()
app_window.title(STR_TITLE)
app_window.config(padx=20, pady=20, bg=COLOR_WHITE)

app_canvas = Canvas(width=200, height=200, bg=COLOR_WHITE, highlightthickness=0)
app_logo_image = PhotoImage(file="./logo.png")
app_canvas.create_image(100, 102, image=app_logo_image)
app_canvas.grid(column=1, row=0)

# website
label_website = Label(text=STR_WEBSITE, font=(FONT_NAME, 20, "normal"), fg=COLOR_BLACK, bg=COLOR_WHITE)
label_website.grid(column=0, row=1, sticky="NW")
input_website = Entry(width=35)
input_website.focus()
input_website.grid(column=1, row=1, columnspan=2, sticky="NW")

# email/username
label_email_username = Label(text=STR_EMAIL_UNAME, font=(FONT_NAME, 20, "normal"), fg=COLOR_BLACK, bg=COLOR_WHITE)
label_email_username.grid(column=0, row=2, sticky="NW")
input_email_username = Entry(width=35)
input_email_username.insert(0, string=COMMONLY_USED_EMAIL)
input_email_username.grid(column=1, row=2, columnspan=2, sticky="NW")

# password
label_pwd = Label(text=STR_PWD, font=(FONT_NAME, 20, "normal"), fg=COLOR_BLACK, bg=COLOR_WHITE)
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