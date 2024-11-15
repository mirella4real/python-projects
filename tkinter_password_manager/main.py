from tkinter import *

STR_TITLE = "Password Manager"
STR_WEBSITE = "Website"
STR_EMAI_UNAME = "Email/Username"
STR_PWD = "Password"
STR_GEN_PWD = "Generate Password"
STR_ADD = "Add"
COLOR_WHITE = "#ffffff"
COLOR_BLACK = "#000000"
FONT_NAME = "Courier"

app_window = Tk()
app_window.title(STR_TITLE)
app_window.config(padx=20, pady=20, bg=COLOR_WHITE)

app_canvas = Canvas(width=200, height=200, bg=COLOR_WHITE, highlightthickness=0)
app_logo_image = PhotoImage(file="./logo.png")
app_canvas.create_image(100, 102, image=app_logo_image)
app_canvas.grid(column=1, row=1)


app_window.mainloop()