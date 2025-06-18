
import tkinter
window = tkinter.Tk()
window.title("Reema_Almohsen_443007548")
lebal1 = tkinter.Label(window,text="Final lab",bg='yellow',fg='red')
lebal1.grid(column=4,row=1)
lebal2 = tkinter.Label(window,text="")
lebal2.grid(column=4,row=5)

def mul():
    entry_mul= int(entry.get())*int(entry2.get())# multplay function
    lebal2.configure(text =entry_mul)

def bindFunction(arg):
    tkinter.Label(window,text="Hello")


entry=tkinter.Entry(window,width=20)
entry.grid(column=4 ,row=2)
entry2=tkinter.Entry(window,width=20)
entry2.grid(column=4 ,row=3)
button = tkinter.Button(window, text=" multiply ",command= mul)
button.bind("<Button-1>",bindFunction )
button.grid(column=4,row=4)
window.geometry('250x250')
window.mainloop()








