import idlelib.macosx
from  tkinter import *

import tkinter as tk
from tkinter import messagebox


class conto:
    def __init__(self, id, saldo):
        self.saldo = saldo
        self.id = id


class mach:
    def __init__(self, conti):
        self.conti = conti



def ricarica(id,importo):
    for i in lista:
        if i.id == id:
            i.saldo += importo
            messagebox.showinfo(f"Successo",(f"il nuovo saldo è {i.saldo}"))


c1 = conto("01", 20)
c2 = conto("02", 10)
c3 = conto("03", 10)
lista = []
lista.append(c1)
lista.append(c2)
lista.append(c3)
m1 = mach(lista)

master=tk.Tk()

width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))


lbl1=Label(master,text="inserisci Id")


lbl1.grid()


e1=Entry(master)
e1.grid(row=0,column=1)



def valuta():
    password = e1.get()
    for i in lista:
        if i.id == e1.get():
            messagebox.showinfo("Benvenuto","Id inserito correttamente")
            new_window = tk.Toplevel(master)
            new_window.title("Macchinetta")
            new_window.geometry("300x500")
            button1=Button(new_window, text="caffè", command=caffè)
            button1.place(relx=0.5, rely=0.1, anchor=CENTER)
            button2 = Button(new_window, text="thè", command=thè)
            button2.place(relx=0.5, rely=0.3, anchor=CENTER)
            button3 = Button(new_window, text="acqua", command=acqua)
            button3.place(relx=0.5, rely=0.5, anchor=CENTER)
            button4 = Button(new_window, text="cioccolata", command=cioccolata)
            button4.place(relx=0.5, rely=0.7, anchor=CENTER)
            button5 = Button(new_window, text="Ricarica", command=ricaricare)
            button5.place(relx=0.5, rely=0.9, anchor=CENTER)




btn1= Button(master,fg="Black",text="convalida", command=valuta)
btn1.grid(row=0,column=2)

def caffè():
    for i in lista:
        if i.id == e1.get():
            if i.saldo >= 2:
                i.saldo -= 2
                lbl2=Label(master,text=(f"Ecco il suo caffè",f"Il suo nuovo saldo è {i.saldo}"))
                lbl2.grid()
            else:
                messagebox.showinfo("Errore","Fondi insufficenti")

def thè():
    for i in lista:
        if i.id == e1.get():
            if i.saldo >= 2.5:
                i.saldo -= 2.5
                lbl3=Label(master, text=(f"Ecco il suo thè",f"Il suo nuovo saldo è {i.saldo}"))
                lbl3.grid()
            else:
                messagebox.showinfo("Errore","Fondi insufficenti")

def acqua():
    for i in lista:
        if i.id == e1.get():
            if i.saldo >= 1:
                i.saldo -= 1
                lbl4=Label(master,text=(f"Ecco la sua acqua",f"Il suo nuovo saldo è {i.saldo}"))
                lbl4.grid()
            else:
                messagebox.showinfo("Errore","Fondi insufficenti")

def cioccolata():
    for i in lista:
        if i.id == e1.get():
            if i.saldo >= 4:
                i.saldo -= 4
                lbl5=Label(master, text=(f"Ecco la sua cioccolataIl suo nuovo saldo è {i.saldo}"))
                lbl5.grid()
            else:
                messagebox.showinfo("Errore","Fondi insufficenti")

def ricaricare():
    nuovaFinestra=tk.Toplevel(master)
    nuovaFinestra.title("Ricarica")
    nuovaFinestra.geometry("400x400")

    lbl6= Label(nuovaFinestra, text="Inserisci l importo d aggiungere")
    lbl6.grid()

    campo = StringVar()
    e2=Entry(nuovaFinestra, textvariable=campo)


    e2.grid(row=0,column=1)


    btn6=Button(nuovaFinestra,text="ricarica", command=lambda : ricarica(e1.get(), int(campo.get())))
    btn6.place(relx=0.5, rely=0.5, anchor=CENTER)












mainloop()