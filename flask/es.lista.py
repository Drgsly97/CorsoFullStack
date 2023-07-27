from flask import Flask, render_template, request

app = Flask(__name__)
listautenti= ["rossi","marroni","bianchi"]
@app.route('/')
def index():
     listautenti =["rossi","marroni","bianchi"]
     return render_template('login3.html', users=listautenti)
@app.route('/login', methods=['POST'])
def login():
    username=request.form['username']
    if username in listautenti:
        return render_template('pag2.html', users=listautenti)
    else:
        listautenti.append(username)
        return render_template('pag2.html', users=listautenti)

if __name__ == '__main__':
    app.run(debug=True)