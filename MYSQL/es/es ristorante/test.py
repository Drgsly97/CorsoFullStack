import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="ristorante"
)
mycursor = mydb.cursor()

class Menu:
    def __init__(self, tipo, prezzo):
        self.tipo=tipo
        self.prezzo = prezzo

    def __str__(self):
        return f"Hai scelto un {self.menu}. Il totale è {self.prezzo}"

menu_carne= Menu ("carne", 20)
menu_pesce = Menu("pesce",25)
menu_bambino = Menu("bambino",15)

master=tk.Tk()

width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))

def carne():
    sql = "INSERT INTO MENU (email, menu, prezzo) VALUES (%s, %s, %s)"
    val = (e1.get(), "Menu carne", 20)
    mycursor.execute(sql, val)
    mydb.commit()

def pesce():
    sql = "INSERT INTO MENU (email, menu, prezzo) VALUES (%s, %s, %s)"
    val = (e1.get(), "Menu pesce", 25)
    mycursor.execute(sql, val)
    mydb.commit()

def bambini():
    sql = "INSERT INTO MENU (email, menu, prezzo) VALUES (%s, %s, %s)"
    val = (e1.get(), "Menu per bambini", 15)
    mycursor.execute(sql, val)
    mydb.commit()

def uscire ():
    mycursor.execute("SELECT * FROM MENU")
    sum = 0
    myresult = mycursor.fetchall()
    for x in myresult:
        sum += int(x[2])
        messagebox.showinfo("la somma guadagnata è",(f"{sum}"))

def accedi():
    email= e1.get()
    sql="INSERT INTO MENU (email, menu, prezzo) VALUES(%s,%s,%s)"
    val = (email, "", "")
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Benvento","Cosa vuole ordinare")
    lbl1.pack_forget()
    e1.pack_forget()
    btn1.pack_forget()
    btn2=Button(master,text="Menu carne", command=carne)
    btn2.pack()
    btn3=Button(master,text="Menu pesce",command=pesce)
    btn3.pack()
    btn4=Button(master,text="menu bambini", command=bambini)
    btn4.pack()
    btn5=Button(master,text="uscire",command=uscire)
    btn5.pack()




lbl1=Label(master,text="inserisci email")
lbl1.pack()

e1=Entry(master)
e1.pack()

btn1=Button(master, text="Accedi", command=accedi)
btn1.pack()
btn6=Button(master)




mainloop()