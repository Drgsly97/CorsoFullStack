import mysql.connector

# Connettiti al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="primodatabase"
)

mycursor = mydb.cursor()

# Comando SQL per eliminare la tabella
table_name = "clienti"
sql = f"DROP TABLE {table_name}"

try:
    # Esegui il comando SQL per eliminare la tabella
    mycursor.execute(sql)

    # Commit delle modifiche (assicurarsi che le modifiche vengano effettivamente applicate)
    mydb.commit()

    print(f"Tabella {table_name} cancellata con successo!")

except mysql.connector.Error as error:
    print(f"Errore durante la cancellazione della tabella: {error}")

finally:
    # Chiudi il cursore e la connessione al database
    mycursor.close()
    mydb.close()
