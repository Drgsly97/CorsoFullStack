import tkinter

import mysql.connector
from tkinter import *
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as  tk


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="automobili")

mycursor = mydb.cursor()


class Auto:
    def __init__(self,marca,colore,optional):
        self.marca=marca
        self.colore=colore
        self.optional=optional

    def __str__(self):
        return (f"la marca della sua macchina è {self.marca}, il colore è {self.colore} e lo stato optional è{self.optional}")

class Gestore:
    def __init__(self, ID,password):
        self.ID=ID
        self.password=password

listaGetsori=[]
g1=Gestore("pippo","A")
listaGetsori.append(g1)



def Invio():
    marca = marca_combobox.get()
    optional = optional_combobox.get()

    if marca == "Fiat" and optional == "Basic":
        id = "1"
        prezzo = "1000"

    elif marca == "Fiat" and optional == "Full":
        id = "2"
        prezzo = "6000"

    elif marca == "AlfaRomeo" and optional == "Basic":
        id = "3"
        prezzo = "5000"

    elif marca == "AlfaRomeo" and optional == "Full":
        id = "4"
        prezzo = "11000"

    elif marca == "Audi" and optional == "Basic":
        id = "5"
        prezzo = "8000"

    else:
        id = "6"
        prezzo = "14000"

    sql = "INSERT INTO maautoopzional (id,marca,colore,optional) VALUES (%s, %s, %s, %s)"
    val = (id,marca_combobox.get(),colore_combobox.get(),optional_combobox.get())
    mycursor.execute(sql, val)
    mydb.commit()


    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "saba.official.game@gmail.com"  # Inserisci il tuo indirizzo email
    sender_password = "gdyoyorwzsoeaqps"  # Inserisci la tua password email

    # Messaggio email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = e1.get()
    message["Subject"] = "Preventivo"
    message.attach(MIMEText((f"la marca scelta è{marca_combobox.get()},il colore è {colore_combobox.get()},gli optional sono{optional_combobox.get()} e il prezzo è {prezzo}"), "plain"))

    #l
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, e1.get(), message.as_string())
        print("Email inviata con successo!")
    except Exception as e:
        print("Errore nell'invio dell'email:", str(e))
    finally:
        server.quit()


def accedi():
    if e2.get()== g1.ID and e3.get() == g1.password:
        new_windows=tk.Toplevel(master)
        new_windows.title("Area Personale")
        new_windows.geometry("400x500")



def clienti():
    nuova_finestra=tk.Toplevel(master)
    nuova_finestra.title("Area Cliente")
    nuova_finestra.geometry("400x500")

    marca = StringVar()
    marca_combobox = ttk.Combobox(nuova_finestra, textvariable=marca)
    marca_combobox['values'] = ["Fiat", "AlfaRomeo", "Audi"]
    marca_combobox.pack(pady=10)

    colore = StringVar()
    colore_combobox = ttk.Combobox(nuova_finestra, textvariable=colore)
    colore_combobox['values'] = ["Bianco", "Nero", "Blue"]
    colore_combobox.pack(pady=10)

    optional = StringVar()
    optional_combobox = ttk.Combobox(nuova_finestra, textvariable=optional)
    optional_combobox['values'] = ["Basic", "Full"]
    optional_combobox.pack()

    lbl1 = Label(nuova_finestra, text="inserisci la tua email")
    lbl1.pack(pady=10)

    e1 = Entry(nuova_finestra)
    e1.pack(pady=10)

    btn1 = Button(nuova_finestra, text="Invia", command=Invio)
    btn1.pack()
    mainloop()




master=Tk()

width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))




lbl2=Label(master, text="inserisci id")
lbl2.pack(pady=5)
lbl3=Label(master, text="inserisci password")
lbl3.pack(pady=5)

e2=Entry(master)
e2.pack()
e3=Entry(master)
e3.pack()

btn2=Button(master, text="Login", command=accedi)
btn2.pack()
btn3=Button(master, text="Area Clienti", command=clienti)
btn3.pack()















