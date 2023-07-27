from tkinter import *

master = Tk()

master.title("Calcolatore")

width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))

lbl1=Label(master, text="inserisci il primo numero")
lbl2=Label(master, text="inserisci il seconndo numero")
lbl3=Label(master)

lbl1.grid()
lbl2.grid()
lbl3.grid()

e1=Entry(master)
e1.grid(row=0,column=1)
e2=Entry(master)
e2.grid(row=1,column=1)

def somma():
    x= (f" la somma dei numeri è {int(e1.get())+ int(e2.get())}")
    lbl3.configure(text=x)

def sottrazione():
    y=(f"il risultato della sottrazione è {int(e1.get())-int(e2.get())}")
    lbl3.configure(text=y)

def moltiplicazione ():
    z=(f"il risultato della moltiplicazione è {int(e1.get())*int(e2.get())}")
    lbl3.configure(text=z)

def divisione ():
    if e2 != 0:
        z=(f"il risultato della divisione è {int(e1.get())/int(e2.get())}")
        lbl3.configure(text=z)
    else:
        lbl3.configure(text="errore")


btn1 = Button(master, text="+",background="black", fg="red",height=1,width=1, command=somma)

btn2= Button(master, text="-",background="black", fg="red", height=1,width=1,command=sottrazione )

btn3= Button(master, text="*",background="black", fg="red", height=1,width=1,command=moltiplicazione )

btn4= Button(master, text="/",background="black", fg="red", height=1,width=1,command=divisione )

btn1.grid(row=3,column=3)
btn2.grid(row=3,column=4)
btn3.grid(row=4,column=3)
btn4.grid(row=4,column=4)






mainloop()