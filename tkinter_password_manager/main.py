from tkinter import *

TITLE = "Password Manager"
WHITE = "#ffffff"



app_window = Tk()
app_window.title(TITLE)
app_window.config(padx=20, pady=20, bg=WHITE)

app_canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
app_logo_image = PhotoImage(file="./logo.png")
app_canvas.create_image(100, 102, image=app_logo_image)
app_canvas.grid(column=1, row=1)


app_window.mainloop()