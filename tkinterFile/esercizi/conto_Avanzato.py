import pickle

movimenti = []
from tkinter import *
import tkinter as tk


class Contocorrente:
    def __init__(self, username, id, saldo):
        self.username = username
        self.id = id
        self.saldo = saldo
        self.listamovimenti = []

    def __str__(self):
        return f"Username: {self.username}, ID conto: {self.id}, Saldo: € {self.saldo}\n"


class Bancomat:
    def __init__(self, conti):
        self.conti = conti

    def __str__(self):
        return self.conti

    def prelievo(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo > cifra:
                    i.saldo -= cifra
                    stampa = (f"\nIl saldo aggiornato è di € {i.saldo}")
                    print(stampa)
                    i.listamovimenti.append(stampa)
                else:
                    print("saldo non disponibile")

    def versamento(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                i.saldo += cifra
                stampa = ("Il saldo aggiornato è di € ", i.saldo)
                print(stampa)
                i.listamovimenti.append(stampa)

    def bonifico(self, cifra, id):
        for i in self.conti:
            if i.id == id:
                if i.saldo > cifra:
                    i.saldo -= cifra + 1.50
                    stampa = (f"\nIl saldo aggiornato è di € {i.saldo}")
                    print(stampa)
                    i.listamovimenti.append(stampa)
                else:
                    print("saldo non disponibile")

    def stampa_saldo(self, id):
        for i in self.conti:
            if i.id == id:
                print(i.saldo)

    def stampa_movimenti(self, id):
        for i in self.conti:
            if i.id == id:
                print(i.listamovimenti)


'''
utente1 = Contocorrente("User 1", "01", int(10000))
utente2 = Contocorrente("User 2", "02", int(30000))
lista_utenti = []
lista_utenti.append(utente1)
lista_utenti.append(utente2)
b1 = Bancomat(lista_utenti)
b1.versamento(400, "02")
b1.prelievo(200, "02")
b1.stampa_movimenti("02")
f = open("testBancomat1.pkl", "wb")
pickle.dump(lista_utenti, f)
f.close()'''

"""print("Benvenuto nella tua home banking.")
f = open("testBancomat1.pkl", "rb")
unpickler = pickle.Unpickler(f)
lista_utenti = unpickler.load()
b1 = Bancomat(lista_utenti)
f.close()
validation = False"""
'''
while validation == False:
    user = input("digita il tuo username: ")
    idcode = input("digita il tuo ID utente: ")
    for el in lista_utenti:
        if user == el.username and idcode == el.id:
            print("Utente convalidato.")
            utente_attivo = el
            validation = True
            scelta = 0
            while scelta != "6":
                scelta = input("Digitare\n"
                               "1 per prelevare\n"
                               "2 per versare\n"
                               "3 per effettuare un bonifico\n"
                               "4 per visualizzare il saldo\n"
                               "5 per visualizzare l'elenco movimenti\n"
                               "6 per terminare: ")
                if scelta == "1":
                    importo = int(input("\nInserisci la cifra da prelevare: "))
                    b1.prelievo(importo, utente_attivo.id)
                elif scelta == "2":
                    importo = int(input("\nInserisci la cifra da versare: "))
                    b1.versamento(importo, utente_attivo.id)
                elif scelta == "3":
                    importo = int(input("\nInserisci l'importo del bonifico: "))
                    b1.bonifico(importo, utente_attivo.id)
                elif scelta == "4":
                    b1.stampa_saldo(utente_attivo.id)
                elif scelta == "5":
                    b1.stampa_saldo(utente_attivo.id)
                elif scelta == "":
                    f = open("testBancomat1.pkl", "wb")
                    pickle.dump(lista_utenti, f)
                    f.close()
                    exit()
                else:
                    print("Scelta non valida.")

    if validation == False:
        print("Utente non trovato. Riprova.")
'''


def open():
    user = password_entry.get()
    password = password_entry1.get()
    for el in lista_utenti:
        if user == el.username and password == el.id:
            login_button2.pack()
            login_button3.pack()
            login_button4.pack()
            password_entry2.pack()
            password_label2.pack()


# create root window
root = tk.Tk()
root.geometry('300x300')
# root window title and dimension
root.title("Bancomat Talentform")
# Set geometry(widthxheight)
# Creazione del pulsante di login
login_button = tk.Button(root, text="Login", command=open)
login_button.pack()
password_label = tk.Label(root, text="Username:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()
password_label1 = tk.Label(root, text="Password:")
password_label1.pack()
password_entry1 = tk.Entry(root, show="*")
password_entry1.pack()
password_label2 = tk.Label(root, text="Display:")
password_label2.pack_forget()
password_entry2 = tk.Entry(root, show="display")
password_entry2.pack_forget()