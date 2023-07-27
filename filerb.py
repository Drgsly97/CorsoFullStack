import pickle
import fileswb

f = open("esercizi/testOggetto.pkl", "rb")
unpickler = pickle.Unpickler(f)
listaDaLettura = unpickler.load()
f.close()
for i in listaDaLettura:
    print(i)