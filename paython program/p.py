# Imports
from gettext import install
from tkinter import *
from tkinter import messagebox
from random import randint

# Screen
import pip

root = Tk()
root.geometry("500x500")
root.title("Number Guessing Game")


# Generate Number Function
def GenerateNumberFunc():
    global Number
    # Generate Number
    Number = randint(1, 10)

    # MessageBox to show that a number was generated
    messagebox.showinfo("A Number was Generated!", "Please Guess the Number")


# Guess Number Function
def GuessNumberFunc():
    global Number
    # Get Value from Answer Entry Box
    UserResponse = AnswerEntry.get()

    # Convert Value from Answer Entry Box to a Number
    UserResponse = int(UserResponse)

    # Check if the User Response was higher, lower, or equal to the correct number
    if UserResponse > Number:
        ResultLabel.config(text="Incorrect! Please Guess Lower", fg="Red")
    elif UserResponse < Number:
        ResultLabel.config(text="Incorrect! Please Guess Higher", fg="Red")
    else:
        ResultLabel.config(text="You Guess Correctly! The Number was {}".format(Number), fg="Green")
        AnswerEntry.delete(0, "end")


# Title
Title = Label(root, text="Number Guessing Game", font=("Arial", 30))
Title.pack()

# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=60)

# Guess the Number Label
GuessNumLabel = Label(MainFrame, text="Guess a number from 1 to 10:", font=("Arial", 20))
GuessNumLabel.pack()

# Answer Entry
AnswerEntry = Entry(MainFrame, font=("Arial", 16))
AnswerEntry.pack(pady=10)

# Generate Number Button
GenerateNumberBtn = Button(MainFrame, text="Generate Number", width=16, font=("Arial", 16), background="Dodgerblue",
                           command=GenerateNumberFunc)
GenerateNumberBtn.pack()

# Guess Button
GuessBtn = Button(MainFrame, text="Guess", width=16, font=("Arial", 16), background="#15e650", command=GuessNumberFunc)
GuessBtn.pack(pady=5)

# Result Label
ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
ResultLabel.pack()

# Mainloop
root.mainloop()

from playsound import playsound
import threading
def gameover():
    playsound('audio.mp3')
    print("Game Over/n")
    timer = threading.timer(10.0, gameover())
    timer.start()











    /////////////////////////////////////////////////////


import tkinter
window = tkinter.Tk()
window.title("Reema_Almohsen_443007548")
lebal1 = tkinter.Label(window,text="Final lab",bg='yellow',fg='red')
lebal1.grid(column=1,row=1)
lebal2 = tkinter.Label(window,text="")
lebal2.grid(column=1,row=2)

def mul():
    result= int(entry1.get())*int(entry2.get())
    lebal2.configure(text=result)


def bindFunction(avr):
    tkinter.Label(window,text="Hello")


entry1=tkinter.Entry(window,width=10)
entry1.grid(column=1 ,row=2)
entry2=tkinter.Entry(window,width=10)
entry2.grid(column=1 ,row=3)
button = tkinter.Button(window, text=" multiply",command= mul)
button.bind("<Button-1>",bindd )
button.grid(column=1,row=4)
window.geometry('230x250')
window.mainloop()
