import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE storico ordini  (username VARCHAR(255), last_access VARCHAR(255), location VARCHAR(255))")