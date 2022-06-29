#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Turtle
#**********************************

from turtle import *

forward(100)

# Exercice 1 - 2)
#****************

def carre(c):
    for i in range(4):
        forward(c)
        right(90)

#carre(100)

def triangle(c):
    for i in range(3):
        forward(c)
        right(120)

#triangle(100)

def maison(c):
    carre(c)
    forward(c)
    right(30)
    triangle(c)
    left(30)
    backward(c)

#maison(100)

# Exercice 1 - 3)
#****************

def figure(c):
    for i in range(6):
        maison(c)
        forward(c)
        right(30)
        forward(c)
        right(30)

#figure(50)

# Exercice 2 - 1)
#****************

def branche():
    taille = 100
    for i in range(5):
        carre(taille)
        forward(taille)
        taille = taille - 20
    backward(300)

#branche()

def figure2():
    for i in range(4):
        branche()
        right(90)

#figure2()

# Exercice 3
#***********

def etoile(c):
  for i in range(7):
    forward(c)
    right(180 - 180 / 7)

#etoile(100)

# Exercice 4
#***********

def heptagone(c):
    for i in range(7):
        forward(c)
        right(360 / 7)

#heptagone(50)

def polygone(n, c):
    for i in range(n):
        forward(c)
        right(360 / n)

#polygone(30,10)

from math import *

def cercle(r):
    c = 2 * r * cos(pi * (1 / 2 - 1 / 360))
    polygone(360, c)
    right(90)
    forward(2 * r)

#cercle(100)
#cercle(50)

# Exercice 5
#***********

def rosace(n, c):
    for i in range(n):
        polygone(n, c)
        right(360 / n)

#rosace(8,100)

# Exercice 6
#***********

def losange(c, a):
    for i in range(2):
        forward(c)
        right(a)
        forward(c)
        right(180 - a)
    
def tore(c):
    for i in range(12):
        a = 15
        for i in range(11):
            losange(c, a)
            forward(c)
            left(15)
            a = a + 15
        for i in range(10):
            right(15)
            backward(c)
        left(15)

#tore(25)

# Triangle isocèle
#*****************

def triangle_isocele(a, c):
    d = c / (2 * cos(pi * a / 180))
    forward(d)
    right(180 - a)
    forward(c)
    right(180 - a)
    forward(d)

#triangle_isocele(30,100)

# Spirale carrée
#***************

def spirale_carre(n):
    if n == 0:
        left(90)
    else:
        spirale_carre(n - 1)
        forward(10 + 5 * n)
        right(90)

#spirale_carre(20)

# Arbre fractale
#***************

def arbre(n):
    if (n == 0):
        pass
    else:
        forward(5 * 2 ** n)
        right(45)
        arbre(n - 1)
        left(90)
        arbre(n - 1)
        right(45)
        backward(5 * 2 ** n)

#arbre(5)

# Triangle de Sierpinski
#***********************

def triangle_noir(m):
    color("black")
    begin_fill()
    forward(m)
    left(120)
    forward(m)
    left(120)
    forward(m)
    left(120)
    end_fill()

#triangle_noir(100)

def sierpinski(n, m):
    if (n == 0):
        triangle_noir(m)
    else:
        sierpinski(n - 1, m / 2)
        forward(m / 2)
        sierpinski(n - 1, m / 2)
        left(120)
        forward(m / 2)
        right(120)
        sierpinski(n - 1, m / 2)
        left(60)
        backward(m / 2)
        right(60)

#sierpinski(3,200)

# pour que la fenêtre reste ouverte après l'exécution
exitonclick()



