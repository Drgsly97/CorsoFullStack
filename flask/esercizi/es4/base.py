from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Imposta il backend 'Agg' per matplotlib
import matplotlib.pyplot as plt
from io import BytesIO


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)

mycursor = mydb.cursor()

lista_prezzi= {
        "cereali": 2,
        "pasta": 1.5,
        "olio":4.3,
        "Insalata":3.5,
        "Melone": 5,
        "Angurie": 5.9,
        "latte": 2.5,
        "mozzarella":3.5,
        "ricotta": 4.7,
        "microonde": 99.9,
        "impastatrice": 147.8,
        "frullatore": 30,
    }
listaUtenti =[]
u1=["pippo","A"]
listaUtenti.append(u1)

app = Flask(__name__)
app.secret_key = "la_tua_chiave_segreta"


@app.route("/", methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #print((email,password))
        # Controlla se l'utente esiste
        mycursor.execute("SELECT * FROM clienti WHERE email = %s", (email,))
        clienti = mycursor.fetchone()
        print(clienti[2])
        if clienti:
            #print(email)
            #hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if clienti[2] == password:
                print(email)
                session["email"] = email
                return redirect(url_for("ordine"))
            else:
                return render_template("login.html", error="Credenziali non valide. Riprova.")
        else:
            return render_template("Registrazione.html", error="Utente non esistente. Registrati.")

    return render_template("login.html", error=None)



@app.route("/register", methods=["POST"])
def registration():
     return render_template("registrazione.html")



@app.route("/benvenuto", methods=["POST"])
def benvenuto():
    if request.method == "POST":


        email = request.form.get("email")
        password = request.form.get("password")
        local_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Verifica se l'utente esiste già
        mycursor.execute("SELECT * FROM clienti WHERE email = %s", (email,))
        user = mycursor.fetchone()

        if user:
            return render_template("login.html", error="Email già registrata. Scegline un'altra.")

        # Registra il nuovo utente
        sql = "INSERT INTO clienti (email, password,local_date) VALUES (%s, %s, %s)"
        val = (email, password, local_date)
        print("clown", email, password)
        mycursor.execute(sql, val)
        mydb.commit()

        session["email"] = email
        return render_template("login.html")



@app.route("/ordine", methods=['GET', 'POST'])
def ordine():
    local_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if "email" not in session:
        return redirect(url_for("login"))
    email = session["email"]
    mycursor.execute("SELECT * FROM supermercato WHERE email = %s ORDER BY local_date DESC LIMIT 1", (email,))
    last_order = mycursor.fetchone()
    print("ciao")
    if request.method == 'POST':

        prodotti_banco = request.form.get('prodotti_banco')
        prodotti_freschi = request.form.get('prodotti_freschi')
        prodotti_frigo = request.form.get('prodotti_frigo')
        elettrodomestici = request.form.get('elettrodomestici')
        totale = lista_prezzi.get(prodotti_banco, 0) + lista_prezzi.get(prodotti_freschi, 0) + \
                 lista_prezzi.get(prodotti_frigo, 0) + lista_prezzi.get(elettrodomestici, 0)

        sql = "INSERT INTO supermercato (email, ProdottiDaBanco, ProdottiFreschi, ProdottiFrigo, Elettrodomestici, totale, local_date) VALUES (%s,%s, %s, %s, %s, %s, %s)"
        val = (email,prodotti_banco, prodotti_freschi, prodotti_frigo, elettrodomestici, totale, local_date)
        mycursor.execute(sql, val)

        mydb.commit()
        return render_template('acquisto.html', prodotti_banco=prodotti_banco, prodotti_freschi=prodotti_freschi, prodotti_frigo=prodotti_frigo, elettrodomestici=elettrodomestici, totale=totale, local_date=local_date)

    return render_template("home.html", products=lista_prezzi, last_order=last_order)


@app.route("/amministrazione", methods=['POST'])
def amministrazione():
    return render_template('amministrazione.html')




@app.route("/entrata", methods=['POST'])

def entrata():
    id = request.form.get("id")
    Adminpassword = request.form.get("Adminpassword")

    for el in listaUtenti:
        if id == el[0] and Adminpassword == el[1]:
            return redirect(url_for('visualizza_grafico'))

    # Se il ciclo for termina senza trovare una corrispondenza, l'autenticazione fallisce
    return render_template("login.html", error="Credenziali amministratore non valide.")


@app.route("/visualizza_grafico", methods=['GET'])
def visualizza_grafico():
    try:
        mycursor.execute("SELECT email, SUM(totale) AS totale_acquisti FROM supermercato GROUP BY email")
        data = mycursor.fetchall()
        if data:
            emails = [row[0] for row in data]
            totali_acquisti = [row[1] for row in data]

            plt.figure(figsize=(10, 6))
            plt.bar(emails, totali_acquisti, color='skyblue')
            plt.xlabel("Email Utente")
            plt.ylabel("Totale Acquisti")
            plt.title("Totale Acquisti per Utente")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            # Salva il grafico su file (opzionale)
            plt.savefig('grafico_totale_acquisti.png')

            # Ritorna l'immagine del grafico in formato base64 (per visualizzarlo nella pagina HTML)
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_base64 = buffer.getvalue()

            # Pulisci la figura dopo averla salvata o memorizzata come base64
            plt.clf()

            return render_template('grafico.html', image_base64=image_base64)
        else:
            return "Nessun dato disponibile per creare il grafico."
    except mysql.connector.Error as error:
        return f"Errore durante l'accesso al database: {error}"


if __name__ == '__main__':
    app.run(debug=True)

