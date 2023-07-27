"""crivere una classe contocorrente che rappresenta un conto corrente bancario.
Il conto è rappresentato da uno username, un id e un saldo.
Successivamente scrivere la classe bancomat e che inizializza una lista di contocorrente e permette di prelevare dal conto,
versare sul conto, fare un bonifico, visualizzare il saldo (plus se nel saldo riusciamo a visualizzare la lista movimenti).
Inoltre scrivere un programma che permette all'utente di usufruire del bancomat dopo aver digitato lo username
e l'id corretto associato al conto"""
import pickle
class Contocorrente:
    def __init__(self,username, id, saldo):
        self.username=username
        self.id=id
        self.saldo=saldo
        self.listamovimenti=[]

    def __str__(self):
        return (f"username è {self.username}, l id è : {self.id} e il saldo è {self.saldo}")


class Bancomat :
    def __init__(self, conti):
        self.conti=conti

    def __str__(self):
        return self.cont1


    def prelievo(self, cifra, id):
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
                    print(mov)











listaconti = []

c1 = Contocorrente("gino","A", 2000)
listaconti.append(c1)
c2 = Contocorrente("pino", "B",1900)
listaconti.append(c2)
c3 = Contocorrente("tino","C", 2555)
listaconti.append(c3)
bancomat = Bancomat(listaconti)
f = open("bancomat.pkl", "wb")
pickle.dump(bancomat, f)
f.close()




id = 0
scelta=input("Benvenuto, prema invio per continuare")
accesso = False
while accesso == False:
    utente= input("inserisci il tuo username")
    id = input("Inserisci il tuo id")
    for i in listaconti:
        if utente == i.username and id == i.id:
            print("accesso Valido")
            utente_attivo = i
            accesso = True

    if accesso == False:
            print("DATI SBAGLIATI, ACCESSO RESPINTO")

while scelta != "6":
    scelta = input("scegli cosa fare: \n"
                   "1) Prelevare dal conto\n"
                   "2) Versare sul conto\n"
                   "3) Fare un bonifico ad un altro utente\n"
                   "4) Visualizzare il proprio saldo\n"
                   "5) Logout")
    if scelta == "1":
        importo=int(input("inserisci l importo da prelevare"))

        utente_attivo.prelievo( importo,id)

    if scelta == "2":
        cifra = int(input("immetti la cifra da versare"))
        utente_attivo.versamento(importo,id)

    if scelta =="3":
        cifra = int(input("immetti la cifra del bonifico"))
        utente_attivo.bonifico(cifra)

    if scelta == "4":
        saldo = utente_attivo.saldo
        print(f"il tuo saldo è {saldo} €")

    if scelta =="5":
        print("Grazie per il servizio")
        break
f = open("bancomat.pkl", "rb")
unpickler = pickle.Unpickler(f)
bancomat = unpickler.load()
f.close()
for i in bancomat:
    print (i)





