from tkinter import *
import pandas as pd
import random


current_card = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_answer, text=current_card['French'], fill='black')
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_answer, text=current_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=card_back)


def remove_word():
    # print(current_card)
    to_learn.remove(current_card)
    words_learned = pd.DataFrame.from_dict(to_learn)
    words_learned.to_csv('data/words_to_learn.csv', index=False)
    next_card()
    

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

card_bg = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#Text
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'), fill='black')
card_answer = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'), fill='black')

#Labels
# label_language_title = Label(text='French:', bg='white', fg='black', font=('Ariel', 40, 'italic'))
# label_language_title.grid(column=0, row=0)

# label_answer = Label(text='Answer', bg='white', fg='black', font=('Ariel', 60, 'bold'))
# label_answer.grid(column=0, row=0)

#Buttons
img_wrong = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=img_wrong, highlightthickness=0, bg='white', command=next_card)
button_wrong.grid(column=0, row=1)

img_right = PhotoImage(file='images/right.png')
button_right = Button(image=img_right, highlightthickness=0, bg='white', command=remove_word)
button_right.grid(column=1, row=1)

next_card()

# show_answer()

# window.after(3000)
# window.after_cancel(id(show_answer()))
# print(id(next_card()))
# print(id(show_answer()))

window.mainloop()