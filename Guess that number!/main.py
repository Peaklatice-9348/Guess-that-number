from tkinter import *
import math
import random

number=random.randint(1,100)
window = Tk()
window.title('game')

def checking_guess():
    if guessbox.get().isdigit:
        guess = int(guessbox.get())
        if guess > 0 and guess < 101:
            if guess>number:
                label3.configure(text='too high')
            elif guess<number:
                label3.configure(text='too low')
            elif guess==number:
                label3.configure(text='you win!')

    else:
        label3.configure(text='invalid')
        


label = Label(window,text='welcome to...',font=('arial',20))
label2 = Label(window,text='GUESS THAT NUMBER!!!!!',font=('impact',100))
label3 = Label(window,text='guess a number from 1 to 100.',font=('arial',20))
label.grid(row=1,column=3)
label2.grid(row=2,column=1,columnspan=7)
label3.grid(row=3,column=3)
guessbox = Entry(window,font=('arial',20))
enterbox = Button(window,font=('arial',20),text='Guess',command=checking_guess)
guessbox.grid(row=4,column=3)
enterbox.grid(row=4,column=4)

window.mainloop()