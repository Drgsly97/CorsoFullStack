from tkinter import *
from tkinter import messagebox
master= Tk()

width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))


lbl1= Label(master, text="inserisci username")
lbl2= Label(master, text="inserisci password")

lbl1.grid()
lbl2.grid()

e1=Entry(master)
e1.grid(row=0,column=1)
e2=Entry(master)
e2.grid(row=1,column=1)

def clicked():
    user = e1.get()
    password = e2.get()
    if user == "francesco" and password == "ciao":
        messagebox.showinfo("Alert","benvenuto")
    else:
        messagebox.showinfo("Alert", "user or password errati")



btn = Button(master, fg="black", text="Login",command=clicked)


btn.grid(row=3,column=3)

mainloop()

