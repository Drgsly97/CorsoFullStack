from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="primodatabase"
)

mycursor = mydb.cursor()

app = Flask(__name__)

listautenti = ["mario", "aldo", "silvio"]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def lista():
    utente = request.form['username']
    for i in listautenti:
        if i == utente:
            return render_template('lista.html', user=listautenti)


    sql = "INSERT INTO lista (persona) VALUES (%s)"
    val = (utente,)
    mycursor.execute(sql, val)
    mydb.commit()

    return render_template('lista.html', user=listautenti)

if __name__ == '__main__':
    app.run(debug=True)