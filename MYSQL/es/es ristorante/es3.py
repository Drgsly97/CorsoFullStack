import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="ristorante"
)
mycursor = mydb.cursor()

class Menu:
    def __init__(self, tipo, prezzo):
        self.tipo=tipo
        self.prezzo = prezzo

    def __str__(self):
        return f"Hai scelto un {self.menu}. Il totale è {self.prezzo}"

    def invia_email(destinatario, oggetto, corpo):
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "saba.official.game@gmail.com"  # Inserisci il tuo indirizzo email
        sender_password = "gdyoyorwzsoeaqps"  # Inserisci la tua password email
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

listamenu=[]
lista_prezzo=[]

menu_carne= Menu ("carne", 20)
menu_pesce = Menu("pesce",25)
menu_bambino = Menu("bambino",15)

scelta =True

while scelta == True:
    inp=input("insersci 1 per accedere o 0 per uscire")

    if inp == "1":
        mail = input("Inserisci l'email: ")

        sceltamenu=5

        while sceltamenu != "0":
            sceltamenu = input("Scegli il tipo di menu:\n"
                                "1) Menu carne\n"
                                "2) Menu pesce\n"
                                "3) Menu  per bambini\n"
                                "0) Disconnettiti")
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="carsaba",
                database="ristorante"
            )
            mycursor = mydb.cursor()

            if sceltamenu == "1":
                listamenu.append(menu_carne)
                lista_prezzo.append(menu_carne.prezzo)
                sql = "INSERT INTO MENU (email, menu, prezzo) VALUES (%s, %s, %s)"
                val = (mail, "Menu carne", 20)
                mycursor.execute(sql, val)
                mydb.commit()
            elif sceltamenu == "2":
                listamenu.append(menu_pesce)
                lista_prezzo.append(menu_pesce.prezzo)
                sql = "INSERT INTO MENU (email, menu, prezzo) VALUES (%s, %s, %s)"
                val = (mail, "Menu pesce", 25)
                mycursor.execute(sql, val)
                mydb.commit()

            elif sceltamenu == "3":
                listamenu.append(menu_bambino)
                lista_prezzo.append(menu_bambino.prezzo)
                sql = "INSERT INTO MENU (email, menu, prezzo) VALUES (%s, %s, %s)"
                val = (mail, "Menu per bambini", 15)
                mycursor.execute(sql, val)
                mydb.commit()



    else:
        scelta= False
        destinatario = mail  # Inserisci l'indirizzo email del destinatario
        oggetto = "Test Email"

        unica_stringa = " ,".join(listamenu)
        tot = 0
        for i in lista_prezzo:
            tot += i
        corpo = "Conferma menu ordine: " + unica_stringa + " Totale da pagare: " + str(tot)
        invia_email(destinatario, oggetto, corpo)






    def invia_email(destinatario, oggetto, corpo):
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "saba.official.game@gmail.com"  # Inserisci il tuo indirizzo email
        sender_password = "gdyoyorwzsoeaqps"  # Inserisci la tua password email
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


