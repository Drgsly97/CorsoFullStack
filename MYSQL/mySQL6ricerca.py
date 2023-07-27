import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE name ='ettore '"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)