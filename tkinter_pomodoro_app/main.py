from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer_reps = 0
TOTAL_REPS = 8
WORK_REPS = [1, 3, 5, 7]
SHORT_BREAK_REPS = [2, 4, 6]
LONG_BREAK_REPS = 8

timer_text = "00:00"
timer_label_text = "Timer"
TIMER_LABEL_WORK = "Work"
TIMER_LABEL_BREAK = "Break"
start_button_label = "Start"
reset_button_label = "Reset"
checkmark_symbol = "✓"
checkmarks = []

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global timer_reps
    global checkmarks
    timer_reps += 1
    current_rep = (timer_reps % TOTAL_REPS)
    if current_rep in WORK_REPS:
        rep_minutes = WORK_MIN
        timer_label_new_text = TIMER_LABEL_WORK
        timer_label_new_color = GREEN
    elif current_rep in SHORT_BREAK_REPS:
        rep_minutes = SHORT_BREAK_MIN
        timer_label_new_text = TIMER_LABEL_BREAK
        timer_label_new_color = PINK
        checkmarks.append(checkmark_symbol)
        checkmark_text = "".join(checkmarks)
        checkmarks_label.config(text= checkmark_text)
    else:
        checkmarks = []
        checkmark_text = ""
        checkmarks_label.config(text= checkmark_text)
        rep_minutes = LONG_BREAK_MIN
        timer_label_new_text = TIMER_LABEL_BREAK
        timer_label_new_color = RED
    count_down(rep_minutes * 60)
    timer_label.config(text=timer_label_new_text)
    timer_label.config(fg=timer_label_new_color)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def format_count(count):
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    return f"{count_min}:{count_sec}"

def count_down(count):
    formatted_count = format_count(count)
    timer_canvas.itemconfig(timer_canvas_text, text=formatted_count)
    if count > 0:
        timer_window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

timer_window = Tk()
timer_window.title("Pomodoro")
timer_window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text=timer_label_text, font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

timer_canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomtato_img = PhotoImage(file="./tomato.png")
timer_canvas.create_image(100, 112, image=tomtato_img)
timer_canvas_text = timer_canvas.create_text(100, 130, text=timer_text, fill="white", font=(FONT_NAME, 35, "bold"))
timer_canvas.grid(column=1, row=1)

start_button = Button(text=start_button_label, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text=reset_button_label, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)


# equivalent of a while loop
timer_window.mainloop()