import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="automobili"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Auto (id VARCHAR(255), marca VARCHAR(255), colore VARCHAR(255),optional VARCHAR(255),prezzo VARCHAR(255))")