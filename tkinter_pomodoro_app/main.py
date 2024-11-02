from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer_text = "00:00"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

timer_window = Tk()
timer_window.title("Pomodoro")
timer_window.config(padx=100, pady=50, bg=YELLOW)

timer_canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomtato_img = PhotoImage(file="./tomato.png")
timer_canvas.create_image(100, 112, image=tomtato_img)
timer_canvas.create_text(100, 130, text=timer_text, fill="white", font=(FONT_NAME, 35, "bold"))
timer_canvas.pack()


# equivalent of a while loop
timer_window.mainloop()