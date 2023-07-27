import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="automobili")

mycursor = mydb.cursor()


def Invio():
    global marca_combobox, colore_combobox, optional_combobox, e1

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

    sql = "INSERT INTO Auto (id,marca,colore,optional,prezzo) VALUES (%s, %s, %s, %s, %s)"
    val = (id, marca_combobox.get(), colore_combobox.get(), optional_combobox.get(),prezzo)
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


class Gestore:
    def __init__(self, ID, password):
        self.ID = ID
        self.password = password


listaGetsori = []
g1 = Gestore("pippo", "A")
listaGetsori.append(g1)

def stampalista():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Auto")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def sommare():
    mycursor.execute("SELECT * FROM Auto")
    myresult = mycursor.fetchall()
    somma = 0
    for x in myresult:
        somma += int(x[4])
    stringa = f"La somma totale dei preventivi è {somma}"
    lbl4 = Label(text=stringa)
    lbl4.pack()

def accedi():
    if e2.get() == g1.ID and e3.get() == g1.password:
        new_window = tk.Toplevel(master)
        new_window.title("Area Personale")
        new_window.geometry("400x500")
        btn4=Button(new_window,text="stampa",command=stampalista)
        btn4.pack(pady=10)
        btn5=Button(new_window,text="somma",command=sommare)
        btn5.pack(pady=10)
    else:
        messagebox.showinfo("ERRORE","Dati non validi")

def clienti():
    nuova_finestra = tk.Toplevel(master)
    nuova_finestra.title("Area Cliente")
    nuova_finestra.geometry("400x500")

    global marca_combobox, colore_combobox, optional_combobox, e1

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


master = Tk()
width = 600
height = 300
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
master.geometry('%dx%d+%d+%d' % (width, height, x, y))

lbl2 = Label(master, text="inserisci id")
lbl2.pack(pady=5)
lbl3 = Label(master, text="inserisci password")
lbl3.pack(pady=5)

e2 = Entry(master)
e2.pack()
e3 = Entry(master)
e3.pack()

btn2 = Button(master, text="Login", command=accedi)
btn2.pack()
btn3 = Button(master, text="Area Clienti", command=clienti)
btn3.pack()

master.mainloop()