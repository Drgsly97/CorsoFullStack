class Distributore:
    def __init__(self,saldo, id):
        self.saldo=saldo
        self.id=id

    def __str__(self):
        return (f"sul tuo conto sono prense {self.saldo} e il tuo id è {self.id}")

    def ricarica(self,):
        cifre=int(input("inserisci quanto vuoi ricaricare"))
        i.saldo= i.saldo+cifre
        print(f"il tuono saldo è {i.saldo}")


    def NuovoID(self, saldo , id):
        saldo=int(input("inserisci quanto vuoi caricare"))
        id=input("inserisci il tuo id")
        listasaldi.append(saldo,id)







listasaldi =[]
d1=Distributore(15.00, "A")
listasaldi.append(d1)
d2=Distributore(2.50,"B")
listasaldi.append(d2)
d3=Distributore(1.00,"C")
listasaldi.append(d3)


scelta = input("Benvenuto, COsa desidera ordinare?")
accesso = False
while accesso == False:
    pr=input("Premi 1 se usare il tuo ID \n Premi 2 se vuoi crearne uno nuovo")
    if pr =="1":
        id = input("inserisci il tuo id")
        for i in listasaldi:
            if id == i.id:
                utente_attivo = i
                accesso= True
    if pr =="2":
        saldo = int(input("inserisci quanto vuoi caricare"))
        id = input("inserisci il tuo id")
        listasaldi.append("saldo","id")
        while scelta != "0":
                    scelta = input(
                        "1)Caffe \n 2)the\n 3)acqua \n 4) cioccolata \n 5) versare soldi sul conto\n 6) Creare nuovo utente ")
                    if scelta == "1":
                        if i.saldo < 1.50:
                         print("fondi insufficenti")
                        else:
                         i.saldo= i.saldo - 1.50
                         print(f"ecco il suo caffè, il suo nuovo saldo è {i.saldo} €")
                    if scelta == "2":
                        if i.saldo < 1.60:
                            print("fondi insufficenti")
                        else:
                            i.saldo = i.saldo - 1.60
                            print(f"ecco il suo the, il suo nuovo saldo è {i.saldo} €")
                    if scelta =="3":
                        if i.saldo < 1:
                            print("fondi insufficenti")
                        else:
                            i.saldo = i.saldo - 1
                            print(f"ecco la sua acqua il suo nuovo saldo è {i.saldo} €")
                    if scelta == "4":
                        if i.saldo < 2.50:
                            print("fondi insufficenti")
                        else:
                            i.saldo = i.saldo - 2.50
                            print(f"ecco La sua cioccolata, il suo nuovo saldo è {i.saldo} €")
                    if scelta == "5":
                        utente_attivo.ricarica()




