from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="carsaba",
  database="primodatabase"
)

mycursor = mydb.cursor()


app = Flask(__name__)
listautenti=[]
u1=["gino","A"]
listautenti.append(u1)

menu_prices = {
    "carbonara": 8,
    "matriciana": 7,
    "cacio e pepe": 6,
    "cotoletta": 5,
    "pesce spada": 8,
    "involtini": 7,
    "patatine fritte": 4,
    "insalata": 3,
    "pane": 1,
    "torta al cioccolato": 4,
    "torta alla fragola": 2,
    "mouse al cioccolato": 6
}
@app.route('/')
def login():
    return  render_template('index.html')



@app.route('/stamp', methods=['POST'])

def stampa():
    primo = request.form['opzione1']
    secondo = request.form['opzione2']
    contorno =request.form ['opzione3']
    dolce = request.form['opzione4']
    totale = menu_prices.get(primo, 0) + menu_prices.get(secondo, 0) + \
             menu_prices.get(contorno, 0) + menu_prices.get(dolce, 0)
    sql = "INSERT INTO ristorante    (primo, secondo, contorno, dolce, prezzo) VALUES (%s, %s, %s, %s, %s)"
    val = (primo,secondo,contorno,dolce,totale)
    mycursor.execute(sql, val)

    mydb.commit()
    return  render_template('risultato.html', primo=primo ,secondo=secondo, contorno=contorno,dolce=dolce,prezzo=totale)


@app.route('/personal', methods=['POST'])
def alpha():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def accesso():
        username = request.form['username']
        password = request.form['password']
        for user in listautenti:
            if username == user[0] and password == user[1]:
                mycursor.execute("SELECT * FROM ristorante")
                tabella = mycursor.fetchall()
                return render_template('lista.html', username=username, password=password, tabella=tabella)


        return "Credenziali errate. Riprova."

def lista():
    mycursor.execute("SELECT * FROM ristorante")
    tabella = mycursor.fetchall()
    return render_template('lista.html',tabella=tabella)


@app.route('/rifiuta_ordine', methods=['Get','POST'])
def rifiuta_ordine():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="carsaba",
        database="primodatabase"
    )
    order_id = request.form['order_id']
    mycursor = mydb.cursor()
    sql = "DELETE FROM ristorante WHERE id = %s"
    val = (order_id,)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('lista'))  #
    except Exception as e:
        # In caso di errore, gestisci il rollback della transazione
        mydb.rollback()
        return "Errore durante la cancellazione dell'ordine: {}".format(str(e))

    return "Ordine rifutato!"


@app.route('/accetta_ordine', methods=['Get','POST'])
def accetta_ordine():
        mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="carsaba",
         database="primodatabase"
       )
        order_id = request.form['order_id']
        mycursor = mydb.cursor()
        sql_select = "SELECT * FROM ristorante WHERE id = %s"
        val = (order_id,)
        mycursor.execute(sql_select, val)
        myresult = mycursor.fetchall()

        # Verifica se il risultato non è vuoto
        if myresult:
            # Estrai i dati dal risultato della query
            menu = myresult[0]  # Suppongo che ci sia solo un risultato per l'order_id

            # Inserisci il menu nella tabella 'storicoOrdini'
            sql_insert = "INSERT INTO storicoordini (primo, secondo, contorno, dolce, prezzo) VALUES (%s, %s, %s, %s, %s)"
            val_insert = (
                menu[1], menu[2], menu[3], menu[4], menu[5]
            )  # Assumendo che i dati corrispondano alle colonne specificate



        else:
            print("Nessun risultato trovato per l'order_id:", order_id)

        try:

            mycursor.execute(sql_insert, val_insert)
            mydb.commit()
            sql = "DELETE FROM ristorante WHERE id = %s"
            val = (order_id,)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(url_for('accesso'))  #
        except Exception as e:
            # In caso di errore, gestisci il rollback della transazione
            mydb.rollback()
            return "Errore durante la cancellazione dell'ordine: {}".format(str(e))

        return "Ordine {} accetato!".format(order_id)


@app.route('/visualizza_dati')
def visualizza_dati():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="carsaba",
        database="primodatabase"
    )
    mycursor = mydb.cursor()

    # Ottieni l'incasso totale
    sql_total = "SELECT SUM(prezzo) FROM storicoOrdini"
    mycursor.execute(sql_total)
    total_result = mycursor.fetchone()
    incasso_totale = total_result[0]

    # Ottieni i dati per il grafico a torta dei primi più scelti
    sql_primi = "SELECT primo, COUNT(*) AS conteggio FROM storicoOrdini GROUP BY primo ORDER BY conteggio DESC LIMIT 5"
    mycursor.execute(sql_primi)
    primi_results = mycursor.fetchall()
    primi_categorie = [result[0] for result in primi_results]
    primi_conteggi = [result[1] for result in primi_results]

    # Ottieni i dati per il grafico a torta dei secondi più scelti
    sql_secondi = "SELECT secondo, COUNT(*) AS conteggio FROM storicoOrdini GROUP BY secondo ORDER BY conteggio DESC LIMIT 5"
    mycursor.execute(sql_secondi)
    secondi_results = mycursor.fetchall()
    secondi_categorie = [result[0] for result in secondi_results]
    secondi_conteggi = [result[1] for result in secondi_results]

    # Chiudi il cursore e la connessione al database
    mycursor.close()
    mydb.close()

    # Genera il grafico a torta dei primi più scelti
    plt.figure(figsize=(8, 8))
    plt.pie(primi_conteggi, labels=primi_categorie, autopct='%1.1f%%')
    plt.title('Primi più scelti')
    plt.savefig('static/primi_piu_scelti.png')  # Salva il grafico come immagine nella cartella static
    plt.close()  # Chiudi il grafico per liberare la memoria

    # Genera il grafico a torta dei secondi più scelti
    plt.figure(figsize=(8, 8))
    plt.pie(secondi_conteggi, labels=secondi_categorie, autopct='%1.1f%%')
    plt.title('Secondi più scelti')
    plt.savefig('static/secondi_piu_scelti.png')  # Salva il grafico come immagine nella cartella static
    plt.close()  # Chiudi il grafico per liberare la memoria

    # Chiudi il cursore e la connessione al database
    mycursor.close()
    mydb.close()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="carsaba",
        database="primodatabase"
    )
    # Ritorna l'incasso totale e i nomi dei file delle immagini dei grafici generati
    incasso_totale = ...  # Il codice per calcolare l'incasso totale va inserito qui
    primi_grafico = 'primi_piu_scelti.png'
    secondi_grafico = 'secondi_piu_scelti.png'

    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(prezzo) FROM storicoOrdini")
    total_result = mycursor.fetchone()
    incasso_totale = total_result[0]

    # Chiudi il cursore e la connessione al database
    mycursor.close()
    mydb.close()

    # Ritorna l'incasso totale e i nomi dei file delle immagini dei grafici generati
    primi_grafico = 'primi_piu_scelti.png'
    secondi_grafico = 'secondi_piu_scelti.png'

    return render_template('visualizzaStatistiche.html', incasso_totale=incasso_totale, primi_grafico=primi_grafico,
                           secondi_grafico=secondi_grafico)


if __name__ == '__main__':
        app.run(debug=True)





