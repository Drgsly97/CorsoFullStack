import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE python")