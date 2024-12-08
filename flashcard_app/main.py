from tkinter import *
import pandas
import random

STR_TITLE = "Flashy"
COLOR_WHITE = "#ffffff"
COLOR_BLACK = "#000000"
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FRENCH = "French"
LANGUAGE_ENGLISH = "English"
FONT= "Ariel"
active_language = LANGUAGE_FRENCH
active_word_dictionary = {
    "French": "partie",
    "English": "part"
}



# Flip card
def flip_card():
    global active_language
    if active_language == LANGUAGE_ENGLISH:
        active_language = LANGUAGE_FRENCH
        active_image = card_front_image
        active_fill = COLOR_BLACK
    else:
        active_language = LANGUAGE_ENGLISH
        active_image =card_back_image
        active_fill = COLOR_WHITE
    app_canvas.itemconfig(card_image, image=active_image)
    app_canvas.itemconfig(card_language, text=active_language)
    app_canvas.itemconfig(card_language, fill=active_fill)
    app_canvas.itemconfig(card_term, text=active_word_dictionary[active_language])
    app_canvas.itemconfig(card_term, fill=active_fill)

# Display new random word
def get_random_word():
    global active_word_dictionary, flip_timer
    app_window.after_cancel(flip_timer)
    if active_language == LANGUAGE_ENGLISH:
        flip_card()
    active_word_dictionary = random.choice(word_dictionaries_list)
    app_canvas.itemconfig(card_term, text=active_word_dictionary[active_language])
    flip_timer = app_window.after(3000, flip_card)

def remove_word():
    global word_dictionaries_list, flip_timer
    app_window.after_cancel(flip_timer)
    
    for index, dict in enumerate(word_dictionaries_list):
        if dict["French"] == active_word_dictionary["French"]:
            word_dictionaries_list.pop(index) 
            save_words(word_dictionaries_list)  
            break
    get_random_word()
    

def save_words(word_dictionaries_list):
    words = pandas.DataFrame(word_dictionaries_list)
    words.to_csv("./data/words_to_learn.csv", index=False)

# Import data using pandas library
try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("./data/french_words.csv")
    words.to_csv("./data/words_to_learn.csv", index=False)
word_dictionaries_list = words.to_dict(orient="records")

# Create the UI using Tkinter
app_window = Tk()
app_window.title(STR_TITLE)
app_window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = app_window.after(3000, flip_card)

app_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_image = app_canvas.create_image(400, 263, image=card_front_image)
card_language = app_canvas.create_text(400, 150, text=active_language, fill="black", font=(FONT, 40, "italic"))
card_term = app_canvas.create_text(400, 263, text=active_word_dictionary[active_language], fill="black", font=(FONT, 60, "bold"))
app_canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=get_random_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

app_window.mainloop()