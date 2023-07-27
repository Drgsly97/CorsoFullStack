"""scrivere un programma che chiede all'utente di inserire username e password e li va a registrare in una tabella creata ad hoc. ' \
'Il programma se l'utente è già presente nella tabella stampa bentornato  lo username altrimenti stampa registrazione avvenuta con successo.
Attenzione: se l'utente è già presente nella tabella non deve essere registrato due volte."""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)
x=input("invio per iniziare")
while x != "0":
    x= input("inserisci:\n"
             "1) per entrare\n"
             "0) per terminare")
    if x == "1":
        username= input("inserisci username")
        password= input("inserisci password")
        mycursor = mydb.cursor()
        sqlu = (f"SELECT * FROM es1 WHERE utente ='{username} '")
        mycursor.execute(sqlu)
        myresult = mycursor.fetchall()
        for i in sqlu:
            if sqlu == username:
                print("Utente gia registrato")
        else:
                mycursor = mydb.cursor()

                sql = "INSERT INTO es1(utente, password) VALUES (%s, %s)"
                val = (username, password)
                mycursor.execute(sql, val)
                mydb.commit()

                print(mycursor.rowcount, "record inserted.")