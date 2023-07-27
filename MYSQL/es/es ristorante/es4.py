import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Test1234",
    database="talentform"
)


def invia_email(destinatario, oggetto, corpo):
    # Configura il server SMTP per inviare l'email (in questo esempio utilizzo Gmail)
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "francesco.sabatino1997@gmail.com"  # Inserisci il tuo indirizzo email
    sender_password = "txccwzeztnuysscn"  # Inserisci la tua password email
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "francesco.sabatino1997@gmail.com"  # Inserisci il tuo indirizzo email
    sender_password = "txccwzeztnuysscn"  # Inserisci la tua password email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = destinatario
    message["Subject"] = oggetto
    message.attach(MIMEText(corpo, "plain"))

    # Connessione e invio dell'email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, destinatario, message.as_string())
        print("Email inviata con successo!")
    except Exception as e:
        print("Errore nell'invio dell'email:", str(e))
    finally:
        server.quit()


lista = []
lista_prezzo = []
scelta = 3
ok = False
while scelta != "0":
    if ok == False:
        scelta = (input("Inserisci la mail 0 per terminare: "))
        ok = True
    else:
        mycursor = mydb.cursor()
        sceltamenu = int(input("Scegli menu: 1 per carne, 2 per pesce, 3 per bambi"))
        if sceltamenu == 1:

            sql = "INSERT INTO menu (email, menu, prezzo) VALUES (%s, %s, %s)"
            val = (scelta, "menu carne", 25)

            mycursor.execute(sql, val)
            lista.append("menu carne")
            lista_prezzo.append(25)
            mydb.commit()
        elif sceltamenu == 2:
            sql = "INSERT INTO menu (email, menu, prezzo) VALUES (%s, %s, %s)"
            val = (scelta, "menu pesce", 40)

            mycursor.execute(sql, val)
            lista.append("menu pesce")
            lista_prezzo.append(40)
            mydb.commit()

        elif sceltamenu == 3:
            sql = "INSERT INTO menu (email, menu, prezzo) VALUES (%s, %s, %s)"
            val = (scelta, "menu bambino", 15)

            mycursor.execute(sql, val)
            lista.append("menu bambino")
            lista_prezzo.append(40)
            mydb.commit()

        elif sceltamenu == 0:
            ok = False
            somma=0
            mycursor.execute("SELECT * FROM MENU")
            myresult = mycursor.fetchall()
            for x in myresult:
                somma+= int(x[2])