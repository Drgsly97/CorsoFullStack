"""Chiedere all'utente di inserire dei numeri in input.' \
' Ogni numero viene registrato in una lista. quando l'utente preme 0
il programma termina e restituisce un grafico (a scelta) sui dati acquisiti"""
import matplotlib.pyplot as plt


z=[]
c=[]



x=input("benvenuto al programma,premi invio per continuare")

while x != "0":
   x= input("Aggiungi un numero")
   z.append(x)
   values = (x)

   print(z)
categories= list(range(1, len(c) + 1))

plt.plot(categories,values)
plt.title("esercizio")
plt.xlabel("categories")
plt.ylabel("numeri")
plt.show()