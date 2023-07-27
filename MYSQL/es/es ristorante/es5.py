from tkinter import *
import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt



class Gestore:
    def __init__(self,user,id):
      self.user =user
      self.id= id

    def __str__(self):
      return (f"il tuo username è {self.user} e il tuo id è {self.id}")

listaGestori=[]
g1=Gestore("Gino","A")
listaGestori.append(g1)
g2=Gestore("Pino","B")
listaGestori.append(g2)

def login ():
    tot = 0
    for x in listaGestori:
        if e1.get() == x.user and e2.get() == x.id:
            informazioni= tk.Toplevel(master)
            informazioni.title("Ordini")
            informazioni.geometry("400x600")
            mycursor.execute("SELECT * FROM MENU")
            myresult = mycursor.fetchall()
            for x in myresult:
                tot+=1
                lbl3 = Label(informazioni, text=x)
                lbl3.pack()
        A = [x[2]]
        B = [tot]
        plt.plot(A, B)
        plt.title("ordini")
        plt.xlabel("somma")
        plt.ylabel("ordini")





    plt.plot
    plt.axis('equal')
    plt.title("Ordini")
    plt.show()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="ristorante"
)
mycursor = mydb.cursor()
master = tk.Tk()


width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))

lbl1=Label(master ,text="inserisci utente")
lbl1.grid()
lbl2=Label(master,text="inserisci password")
lbl2.grid()
e1=Entry(master)
e1.grid(row=0 ,column=3)
e2=Entry(master)
e2.grid(row=1, column=3)

btn1=Button(master,text="login", command=login)
btn1.grid(row=2,column=3)
mainloop()