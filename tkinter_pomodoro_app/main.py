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
TOTAL_REPS = 8
WORK_REPS = [1, 3, 5, 7]
SHORT_BREAK_REPS = [2, 4, 6]
LONG_BREAK_REPS = 8
TIMER_TEXT = "00:00"
TIMER_LABEL_TEXT = "Timer"
TIMER_LABEL_WORK = "Work"
TIMER_LABEL_BREAK = "Break"
START_BUTTON_LABEL = "Start"
RESET_BUTTON_LABEL = "Reset"
CHECKMARK_SYMBOL = "✓"

timer_reps = 0
timer = None
checkmarks = []

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_reps
    global timer
    if timer != None:
        timer_window.after_cancel(timer)
        reset_checkmarks()
        timer_canvas.itemconfig(timer_canvas_text, text=TIMER_TEXT)
        timer_label.config(text=TIMER_LABEL_TEXT)
        timer_label.config(fg=GREEN)
        timer_reps = 0
        timer = None

def reset_checkmarks():
    global checkmarks
    checkmarks = []
    checkmark_text = ""
    checkmarks_label.config(text= checkmark_text)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    if timer == None:
        run_timer()

def run_timer():
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
        checkmarks.append(CHECKMARK_SYMBOL)
        checkmark_text = "".join(checkmarks)
        checkmarks_label.config(text= checkmark_text)
    else:
        reset_checkmarks()
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
        global timer
        timer = timer_window.after(1000, count_down, count-1)
    else:
        run_timer()

# ---------------------------- UI SETUP ------------------------------- #

timer_window = Tk()
timer_window.title("Pomodoro")
timer_window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text=TIMER_LABEL_TEXT, font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

timer_canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomtato_img = PhotoImage(file="./tomato.png")
timer_canvas.create_image(100, 112, image=tomtato_img)
timer_canvas_text = timer_canvas.create_text(100, 130, text=TIMER_TEXT, fill="white", font=(FONT_NAME, 35, "bold"))
timer_canvas.grid(column=1, row=1)

start_button = Button(text=START_BUTTON_LABEL, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text=RESET_BUTTON_LABEL, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)


# equivalent of a while loop
timer_window.mainloop()