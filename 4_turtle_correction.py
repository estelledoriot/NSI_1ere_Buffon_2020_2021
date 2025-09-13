# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Turtle
# **********************************

from turtle import *

# Exercice 1 - 2)
# ****************


def carre(c):
    for i in range(4):
        forward(c)
        right(90)


# carre(100)


def triangle(c):
    for i in range(3):
        forward(c)
        right(120)


# triangle(100)


def maison(c):
    carre(c)
    forward(c)
    right(30)
    triangle(c)
    left(30)
    backward(c)


# maison(100)

# Exercice 1 - 3)
# ****************


def figure(c):
    for i in range(6):
        maison(c)
        forward(c)
        right(30)
        forward(c)
        right(30)


# figure(50)

# Exercice 2
# ***********


def branche():
    taille = 100
    for i in range(5):
        carre(taille)
        forward(taille)
        taille = taille - 20
    backward(300)


# branche()


def figure2():
    for i in range(4):
        branche()
        right(90)


# figure2()

# Exercice 3
# ***********


def etoile(c):
    for i in range(7):
        forward(c)
        right(180 - 180 / 7)


# etoile(200)

# Exercice 4 - 1)
# ****************


def heptagone(c):
    for i in range(7):
        forward(c)
        right(360 / 7)


# heptagone(50)

# Exercice 4 - 2)
# ****************


def polygone(n, c):
    for i in range(n):
        forward(c)
        right(360 / n)


# polygone(12, 50)


# Exercice 4 - 3)
# ****************

from math import *


def cercle(r):
    c = 2 * r * cos(pi * (1 / 2 - 1 / 360))
    polygone(360, c)
    right(90)
    forward(2 * r)


# cercle(100)

# Exercice 5
# ***********


def rosace(n, c):
    for i in range(n):
        polygone(n, c)
        right(360 / n)


# rosace(10, 100)

# Exercice 6 - 1)
# ****************


def losange(c, a):
    for i in range(2):
        forward(c)
        right(a)
        forward(c)
        right(180 - a)


# losange(50, 15)

# Exercice 6 - 2)
# ****************


def tore(c):
    for i in range(12):
        # le plus petit angle mesure 15°
        a = 15
        # on crée une "branche" de losanges dont l'angle augmente de 15
        for i in range(11):
            losange(c, a)
            forward(c)
            left(15)
            a = a + 15
        # on retourne au début de la branche
        for i in range(10):
            right(15)
            backward(c)
        left(15)


tore(25)

# pour que la fenêtre reste ouverte après l'exécution
exitonclick()
