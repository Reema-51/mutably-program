
import tkinter
window = tkinter.Tk()
window.title("fatimahturky-443007482")
lebal = tkinter.Label(window,text="Final lab",bg='yellow',fg='blue')
lebal.grid(column=1,row=1)
lebal2 = tkinter.Label(window,text="")
lebal2.grid(column=1,row=5)

def add():
    entry_add= int(entry.get())+int(entry2.get())
    lebal2.configure(text =entry_add)

def bindd(arg):
    tkinter.Label(window,text="welcom")


entry=tkinter.Entry(window,width=10)
entry.grid(column=1 ,row=2)
entry2=tkinter.Entry(window,width=10)
entry2.grid(column=1 ,row=3)
button = tkinter.Button(window, text=" add",command= add)
button.bind("<Button-1>",bindd )
button.grid(column=1,row=4)
window.geometry('30x110')
window.mainloop()



