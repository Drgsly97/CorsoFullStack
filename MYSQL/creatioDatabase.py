import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Persona  (persona VARCHAR(255),password VARCHAR(255))")