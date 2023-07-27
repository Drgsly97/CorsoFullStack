from flask import  Flask, render_template
class oggetto:
   x = 5

   def __str__(self):
    return f"Oggetto semplice con valore: {self.x} "
app = Flask(__name__)

prop = oggetto.x


@app.route("/")
def home():
   prop = 7
   somma= int(input("inserisci un numero"))
   somma += prop
   return f"il valore di c1 {somma}"

if __name__ == "__main__":
    app.run()