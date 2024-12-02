from tkinter import *
import pandas
import random

STR_TITLE = "Flashy"
BACKGROUND_COLOR = "#B1DDC6"
FONT= "Ariel"

# Import data using pandas library
words = pandas.read_csv("./data/french_words.csv")
words_dictionary = words.to_dict(orient="records")

# Display new random word
def get_random_word():
    random_word = random.choice(words_dictionary)
    app_canvas.itemconfig(card_term, text=random_word["French"])
# Create the UI using Tkinter
app_window = Tk()
app_window.title(STR_TITLE)
app_window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

app_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
app_canvas.create_image(400, 263, image=card_front_image)
card_language = app_canvas.create_text(400, 150, text="French", fill="black", font=(FONT, 40, "italic"))
card_term = app_canvas.create_text(400, 263, text="trouve", fill="black", font=(FONT, 60, "bold"))
app_canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=get_random_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=get_random_word)
right_button.grid(column=1, row=1)
app_window.mainloop()