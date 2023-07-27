import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)
p2 = Person("Carlo", 38)
lista = []
lista.append(p1)
lista.append(p2)
f = open("esercizi/testOggetto.pkl", "wb")
pickle.dump(lista, f)
f.close()