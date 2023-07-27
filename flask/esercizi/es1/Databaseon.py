import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE lista  (persona VARCHAR(255))")