import pickle
class Libro:
    def __init__(self,titolo,autore,pubblicazione,disponibile=True):
        self.titolo=titolo
        self.autore=autore
        self.pubblicazione=pubblicazione
        self.disponibile=disponibile

    def __str__(self):
         return (f"il titolo del libro è:{self.titolo},l autore è {self.autore}, è stato pubblicato il{self.pubblicazione} e attualmente è {self.disponibile}")


class Biblioteca:
    def __init__(self,lista):
        lista=[]
        self.lista=lista

    def __str__(self):
        return f"{self.lista}"

    def add(self, libro):
        self.lista.append(libro)

    def dispo(self,libro):
        libro.disponibile=False


bibliolista = Biblioteca("lista")


scelta = input("benvenuto nel file,premi invio per continuare")

while scelta != "6":
    scelta = input("Scegli un opzione :\n"
                   "1 aggiungere un nuovo libro \n"
                   "2 prenotare un libro dal titolo \n"
                   "3 ricercare i libri per autore\n"
                   "4 salvare la biblioteca su un file (scrittura wb)\n"
                   "5 leggere la biblioteca salvata (lettura rb)\n"
                   "6 uscire dal programma")
    if scelta == "1":
        titolo= input("Inserisci titolo libro")
        autore= input("Inserisci l autore")
        pubblicazione= input("Inserisci data di pubblicazione")
        bibliolista.add(Libro(titolo,autore,pubblicazione))


    if scelta == "2":
        titolo = input("Inserisci titolo libro")
        for el in bibliolista.lista:
            if el.titolo== titolo and el.disponibile==True:
                print("libro prenotato")
            else:
                print("libro gia prenotato")

    if scelta =="3":
        aut=input("inserisci un autore")
        for el in bibliolista.lista:
            if el.autore == aut:
                print(el)

    if scelta=="4":
        f = open("bibliolista.pkl", "wb")
        pickle.dump(bibliolista, f)
        f.close()
        print("file salvato con successo")

    if scelta=="5":
        f = open("bibliolista.pkl", "rb")
        unpickler = pickle.Unpickler(f)
        bibliolista = unpickler.load()
        f.close()
        for i in bibliolista:
            print(i)






