class Canzone:
    def __init__(self,titolo,autore,pubblicazione):
        self.titolo=titolo
        self.autore=autore
        self.pubblicazione=pubblicazione

    def __str__(self):
        return (f"titolo:{self.titolo}\n autore{self.autore}\nanno pubblicazione {self.pubblicazione}")

canzoni = []

c1 = Canzone("mercoledi","marco",2022)
canzoni.append(c1)
c2 = Canzone("viaggiare","giulio",2021)
canzoni.append(c2)
c3 = Canzone("sognare","mario",2000)
canzoni.append(c3)

print(canzoni)

scelta = input("scegli cosa fare:\n "
               "1 aggiungere una nuova canzone\n"
               "2 cercare una canzone dalla lista per titolo \n"
               "3 stampare tutte le canzoni di un autore \n"
               "4 rimuovere una canzone dal titolo \n5 uscire dal programma")
while scelta != 5:
    if scelta == "1":
        titolo = input("inserisci titolo")
        autore = input("inserisci autore")
        pubblicazione = input("anno di pubbliazione")
        canzoni.append(Canzone(titolo, autore, pubblicazione))
        print(f" la canzone aggiunta è {titolo}, l autore è {autore},lanon di pubblicazione è {pubblicazione}")
        break

    elif scelta == "2":
        cerca = input("inserisci titolo")
        for el in canzoni:
                if cerca == el.titolo:
                    print(f"la canzone cercata è{el.titolo2}")
                else:
                    print("non presente")
        
    elif scelta == "3":
        stampare= input("autore da stampare")
        for el in canzoni:
            if stampare == el.autore:
                print(f"le canzoni di quest autore sono {el.titolo}")

    elif scelta == "4":
        cancella=input("Titolo canzone cancellare")
        for el in canzoni:
            if el == cancella:
                canzoni.remove(cancella)
                print("canzone rimossa")
else:
    print("Fine del programma")

