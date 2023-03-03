from tkinter import *
import pandas as pd
import random


data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_answer, text=current_card['French'], fill='black')
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

# def show_answer():
#     window.after(3000)
#     canvas.itemconfig(img_card_front, image=card_back)


# def random_num(num):
#     random_num = random.randint(0, len(num)-1)
#     return random_num


# def random_word():
#     with open('data/french_words.csv') as file:
#         df = pd.read_csv(file)
#         new_word_french = df['French'][random_num(df['French'])]
#         canvas.itemconfig(card_answer, text=new_word_french)
#         canvas.itemconfig(card_title_new, text='Frenchhh')


def flip_card():
    # print('hello')
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_answer, text=current_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=card_back)

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
button_right = Button(image=img_right, highlightthickness=0, bg='white', command=next_card)
button_right.grid(column=1, row=1)

next_card()

# show_answer()

# window.after(3000)
# window.after_cancel(id(show_answer()))
# print(id(next_card()))
# print(id(show_answer()))

window.mainloop()