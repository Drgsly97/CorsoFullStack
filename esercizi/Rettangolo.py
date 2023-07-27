



"""Scrivere una classe Rettangolo i cui oggetti rappresentano rettangoli.
 Lo stato interno di un rettangolo è dato dai valori della base e dell’altezza. Un rettangolo deve mettere a disposizione tre operazioni
 : ridimensiona() che prende come parametri due nuovi valori di base e altezza e aggiorna lo stato, perimetro() che restituisce il perimetro e area()
  che restituisce l’area. Prevedere inoltre un costruttore che inizializza base e altezza del rettangolo.
Successivamente chiede in maniera iterat
Successivamente chiede in maniera iterativa all’utente
1 di inserire base e altezza e aggiungerlo a una lista di rettangoli
2  di stampare la somma dei perimetri
3 di stampare la somma delle aree
4 di salvare la lista su un file
5 di leggere la lista da un file
6 uscire dal programm"""

import pickle

class Rettangolo:
    def __init__(self,base, altezza):
        self.base=base
        self.altezza=altezza

    def __str__(self):
        return (f"la base del rettangolo è {self.base} e l altezza è {self.altezza}")

    def perimetro(self,):
        return (self.base* 2+ self.altezza * 2)

    def area(self, ):
        return (self.base*self.altezza)

    def ridimensionare(self,newbase,newaltezza):
        self.base=newbase
        self.altezza=newaltezza

r1=Rettangolo(10,10)
r2=Rettangolo(8,2)
rettangoli = []

rettangoli.append(r1)
rettangoli.append(r2)

scelta = input("premi invio per continuare")

while scelta != 7:
    scelta= input("Scegli cosa fare:\n "
                  "1 di inserire base e altezza e aggiungerlo a una lista di rettangoli \n "
                  "2  di stampare la somma dei perimetri\n "
                  "3 di stampare la somma delle aree\n
                  "4 di salvare la lista su un file\n "
                  "5 di leggere la lista da un file\n "
                  "6 uscire dal programma")

    if scelta == "1":
        base= int(input("inserisci la base"))
        altezza= int(input("inserisci l altezza"))
        rettangoli.append(Rettangolo(base,altezza))
    if scelta =="2":
        for el in rettangoli:
            perimetri= Rettangolo.perimetro(el)
            print(f"la somma dei perimetri è {perimetri}")
    if scelta=="3":
        for el in rettangoli:
            area= Rettangolo.area(el)
            print(f"la somma delle aree è{area}")
    if scelta =="4":
        f = open("rettangoli.pkl", "wb")
        pickle.dump(rettangoli, f)
        f.close()
        print("file salvato")

    if scelta =="5":
        f =open("rettangoli.pkl", "rb")
        unpickler = pickle.Unpickler(f)
        rettangoli= unpickler.load()
        f.close()
        for i in rettangoli:
            print(i)

    if scelta =="6":
        print("fine programma")
        break









