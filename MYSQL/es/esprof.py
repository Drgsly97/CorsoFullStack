import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Test1234",
    database="talentform"
)

scelta = 2

while scelta != 0:

    user = input("Inserisci lo username: ")
    passw = input("Inserisci la password: ")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM user")

    myresult = mycursor.fetchall()
    ok = False
    for x in myresult:

        nome = x[0]
        passf = x[1]
        if nome == user and passf == passw:
            ok = True

    if ok == False:

        mycursor = mydb.cursor()

        sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
        val = (user, passw)
        mycursor.execute(sql, val)

        mydb.commit()
        print("Ciao ", user, "registrazione effettuata")
        print(mycursor.rowcount, "record inserted.")
    else:
        print("bentornato :", user)

    scelta = int(input("Premi 1 per iterare 0 per terminare: "))