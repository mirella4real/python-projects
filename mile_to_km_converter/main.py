import tkinter
WINDOW_TITLE = "Mile to Km Converter"
FONT = ("Arial", 12)
MILES = "Miles"
KM = "Km"
IS_EQUAL = "is equal to"
BUTTON_LABEL = "Calculate"

def convert_miles():
    pass

my_window = tkinter.Tk()
my_window.title(WINDOW_TITLE)
my_window.minsize(width=300, height=150)
my_window.config(padx=40, pady=40)

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)
user_input.insert(0, string=0)

input_label = tkinter.Label(text=MILES, font=FONT)
input_label.grid(column=2, row=0)

leyend_label = input_label = tkinter.Label(text=IS_EQUAL, font=FONT)
input_label.grid(column=0, row=2)

result = tkinter.Label(text=0, font=FONT)
result.grid(column=1, row=2)

result_label = tkinter.Label(text=KM, font=FONT)
result_label.grid(column=2, row=2)

calculate_button = tkinter.Button(text=BUTTON_LABEL, command=convert_miles)
calculate_button.grid(column=1, row=2)
















my_window.mainloop()