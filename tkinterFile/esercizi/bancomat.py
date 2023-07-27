import pickle
import tkinter
from  tkinter import *
from  tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter as tk

class Contocorrente:
    def __init__(self,username, id, saldo):
        self.username=username
        self.id=id
        self.saldo=saldo
        self.listamovimenti=[]
        self.bonifico=0
        self.versamento=0
        self.prelievo=0

    def __str__(self):
        return (f"username è {self.username}, l id è : {self.id} e il saldo è {self.saldo}")

    def grafico(self,somma_prelievi):
        for i in listaconti:
            if i.id == e2.get():
                somma_prelievi+=self.prelievo


class Bancomat :
    def __init__(self, conti):
        self.conti=conti

    def __str__(self):
        return self.cont1

    def prelevare(self,cifre):
        for i in listaconti:
            if i.id == e2.get():
                if i.saldo >= cifre:
                    i.saldo -= cifre
                messagebox.showinfo("Ricarica Effettuata", (f"il suono nuovo saldo è {i.saldo} "))
            else:
                messagebox.showinfo("Errore", "Saldo non disponibile")
"""def prelevare(self, cifra, id):
        for el in self.conti:
            if el.id == id:
               if el.saldo >= cifra:
                   el.saldo -= cifra

                   el.movimenti.append(f"- {cifra}\n")
               else: print("Cifra non disponibile")
               print(f"\nIl saldo aggiornato è di € {el.saldo}")

def versamento (self, cifra,):
        for el in self.conti:
            if el.id == id:
                el.saldo += cifra
                el.movimenti.append(f"il saldo aggiornato p {el.saldo}")
        return print(f"il tuo nuovo saldo è di {self.saldo} € ")


def bonifico (self, cifra,mittente,destinatario):
        tasse = 2.50
        for el in self.conti:
            if el.id == destinatario:
                el.saldo += cifra
        for el in self.conti:
            if el.id == mittente:
                if el.saldo>= cifra +tasse:
                    el.saldo= el.saldo - cifra - tasse
                    el.movimenti.append(f"-{cifra} - tasse di {tasse}")
                    print(f"Il saldo è di {el.saldo} €")

def stampa_saldo(self, id):
        for el in self.conti:
            if el.id ==id:
                print(f"il saldo aggiornato e {el.saldo} €")

def stampa_movimenti(self,id):
        for el in self.conti:
            if el.id == id:
                print("la lista dei movimenti è:")
                for mov in el.movimenti:
                    print(mov)"""











listaconti = []

c1 = Contocorrente("gino","A", 2000)
listaconti.append(c1)
c2 = Contocorrente("pino", "B",1900)
listaconti.append(c2)
c3 = Contocorrente("tino","C", 2555)
listaconti.append(c3)
bancomat = Bancomat(listaconti)






master=Tk()
master.title("Bancomat")

def hide_button():
    bt1.pack_forget()



def Autenticazione():
    id =e2.get()
    for i in listaconti:
        if i.id == e2.get() and i.username == e1.get():
            messagebox.showinfo("Benvenuto", "scelga cosa fare")
            bt1.pack_forget()
            e1.pack_forget()
            e2.pack_forget()
            lbl1.pack_forget()
            campo=StringVar()
            e3=Entry(master, textvariable=campo)
            e3.pack()
            bt2= Button(master,text="Prelievo", command=lambda :prelevare())
            bt2.pack()
            bt3=Button(master,text="Versamento",command= lambda:versamento())
            bt3.pack()
            bt4=Button(master,text="Bonifico",command= lambda :bonofico())
            bt4.pack()
            bt5=Button(master,text="Saldo",command= lambda :StampaSaldo())
            bt5.pack()
            bt6=Button(master, text="Grafico", command=lambda : grafico())
            bt6.pack()



            def prelevare():
                for i in listaconti:
                    if i.id == e2.get():
                        if i.saldo >= int(e3.get()):
                            i.saldo -= int(e3.get())
                            messagebox.showinfo("Ricarica Effettuata",(f"il suono nuovo saldo è {i.saldo} "))
                        else:
                            messagebox.showinfo("Errore","Saldo non disponibile")
            def versamento():
                for i in listaconti:
                    if i.id == e2.get():
                        i.saldo += int(e3.get())
                        messagebox.showinfo("Versamento Effettuato", (f"il suono nuovo saldo è {i.saldo} "))

            def bonofico():
                tasse= 2.5
                for i in listaconti:
                        if i.id == e2.get():
                            i.saldo -= int(e3.get()) + tasse
                            messagebox.showinfo("Bonifico effettuato",(f"il suo nuovo saldo è {i.saldo}"))

            def StampaSaldo():
                for i in listaconti:
                    if i.id== e2.get():
                        messagebox.showinfo("Saldo",(f"il suo saldo è {i.saldo}"))

            def grafico():
                id = e2.get()
                somma_prelievi = 0
                for i in listaconti:
                    if i.id == id:
                        for prelevare in i.listamovimenti:
                            if prelevare == int(e3.get()):
                                somma_prelievi += prelevare
                for i in listaconti:
                    somma_versamenti =0
                    if i.id== id:
                        for versamento in i.listamovimenti:
                            if versamento== int(e3.get()):
                               somma_versamenti == versamento[1]
                for i in listaconti:
                     somma_bonifici=0
                     if i.id== id:
                         for bonofico in i.listamovimenti:
                             somma_bonifici += bonofico


                # Creating the graph
                labels = ['Prelievi', 'Versamenti']
                sizes = [somma_prelievi, i.versamento]
                explode = (0.1, 0)  # explode the first slice

                fig, ax = plt.subplots()
                ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

                plt.show()














width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))

lbl1 =Label(master, text="Inserisci ID")
lbl1.pack()

e1=Entry(master)
e1.pack()
e2=Entry(master,show="*")
e2.pack()
bt1=Button(master, text="Invio",command = Autenticazione)
bt1.place(relx=0.5, rely=0.5, anchor= CENTER)
bt1.pack()




mainloop()