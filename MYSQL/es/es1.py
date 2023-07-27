"""Scriviamo un programma che in maniera iterativa se l'utente preme 1 chiede all'utente di inserire nome e indirizzo.
Il programma prevede che il nome e l'ndirizzo vengano scritti all'interno della tabella customers.
quando l'utente preme 0 il programma termina"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)

x= input("premi invio per continuare")
while x != "0":
    x = input("scegli cosa fare:\n"
              "1) Insersci nuovo utente e indirizzo\n"
              "0) Finisci il programma")
    if x == "1":

        user=input("insersci nome utente")
        indi=input("inserisci indirizzo")
        mycursor = mydb.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (user, indi)

        mycursor.execute(sql, val)

        mydb.commit()

    print(mycursor.rowcount, "record inserted.")