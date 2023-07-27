import tkinter
from tkinter import *


master = Tk()

master.title("Primo esercizio")
master.geometry('400x500')

lbl1= Label(master, text="primo numero")
lbl2= Label(master, text="secondo numero")
lbl3= Label(master)


lbl1.grid(row=0,column=1)
lbl2.grid(row=1,column=1)
lbl3.grid(row=1, column=3)

e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=2)
e2.grid(row=1, column=2)

def clicked():
    ris=(f"la somma è :{(int(e1.get()))+ int(e2.get())}")
    lbl3.configure(text=ris)

button= Button(master, text='somma', width=35, command=clicked)
button.grid(row=0,column=3)

mainloop()





