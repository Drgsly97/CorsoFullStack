import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Configurazione della finestra di gioco
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Disattiva gli aggiornamenti automatici dello schermo

# Testa del serpente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Cibo del serpente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Punteggio
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Punteggio: 0  Punteggio massimo: 0", align="center", font=("Courier", 24, "normal"))

# Funzioni
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Ciclo principale del gioco
while True:
    wn.update()

    # Verifica delle collisioni con il bordo dello schermo
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Nasconde i segmenti del serpente
        for segment in segments:
            segment.goto(1000, 1000)

        # Resetta la lista dei segmenti
        segments.clear()

        # Resetta il punteggio
        score = 0

        # Resetta il ritardo
        delay = 0.1

        pen.clear()
        pen.write("Punteggio: {}  Punteggio massimo: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # Verifica la collisione con il cibo
    if head.distance(food) < 20:
        # Sposta il cibo in una posizione casuale
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Aggiungi un segmento al serpente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Abbassa il ritardo
        delay -= 0.001

        # Aumenta il punteggio
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Punteggio: {}  Punteggio massimo: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # Muove i segmenti in ordine inverso
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Muove il segmento 0 alla posizione della testa
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Verifica delle collisioni con il corpo del serpente
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Nasconde i segmenti del serpente
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Punteggio: {}  Punteggio massimo: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()