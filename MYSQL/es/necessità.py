import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="primodatabase"
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE menù (menu VARCHAR(255), email VARCHAR(255), prezzo VARCHAR(255)")