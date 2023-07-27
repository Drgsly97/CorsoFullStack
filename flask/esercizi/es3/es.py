from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt
import io
import base64

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="carsaba",
    database="primodatabase"
)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

def salva(username, ultimo_accesso):
    try:
        mycursor = mydb.cursor()

        query = "INSERT INTO new_table (username, ultimo_accesso) VALUES (%s, %s)"
        values = (username, ultimo_accesso)

        mycursor.execute(query, values)
        mydb.commit()
        print("Dati salvati correttamente nel database.")

    except mysql.connector.Error as error:
        print("Errore durante il salvataggio dei dati:", error)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

@app.route('/', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        last_access = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        salva(username, last_access,)

        return f'Dati salvati con successo per lo username: {username}'
    else:
        return render_template('index.html')

@app.route('/visualizza_dati')
def visualizza_dati():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="carsaba",
            database="primodatabase"
        )
        mycursor = mydb.cursor()

        categories_query = "SELECT username from new_table"
        values_query = "SELECT ultimo_accesso from new_table"

        mycursor.execute(categories_query)
        categories_data = [row[0] for row in mycursor.fetchall()]

        mycursor.execute(values_query)
        values_data = [row[0] for row in mycursor.fetchall()]

        # Creiamo il grafico a torta
        plt.figure(figsize=(8, 6))
        plt.pie(values_data, labels=categories_data, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Per avere un aspetto circolare

        # Salva il grafico a torta come immagine
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Codifica l'immagine in base64 per poterla visualizzare nella pagina HTML
        image_base64 = base64.b64encode(image_png).decode('utf-8')

        # Chiude la connessione al database
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

        return render_template('index.html')
if __name__ == "__main__":
    app.run()
