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
timer_label_text = "Timer"
start_button_label = "Start"
reset_button_label = "Reset"
checkmark_symbol = "✓"
checkmark_text = checkmark_symbol

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

timer_window = Tk()
timer_window.title("Pomodoro")
timer_window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text=timer_label_text, font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

timer_canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomtato_img = PhotoImage(file="./tomato.png")
timer_canvas.create_image(100, 112, image=tomtato_img)
timer_canvas.create_text(100, 130, text=timer_text, fill="white", font=(FONT_NAME, 35, "bold"))
timer_canvas.grid(column=1, row=1)

start_button = Button(text=start_button_label, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

reset_button = Button(text=reset_button_label, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(text=checkmark_text, font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

# equivalent of a while loop
timer_window.mainloop()