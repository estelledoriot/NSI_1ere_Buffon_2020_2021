# *******************************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Cours sur les structures conditionnelles
# *******************************************

# Exemple sur la différence entre égalité (==) et affectation (=)
print("** Exemple: **")

a = 3  # on affecte la valeur 3 à la variable a
print(a)  # on affiche la valeur de la variable a -> 3
print(a == 3)  # on teste si a est égal à 3 -> True
print(a == 2)  # on teste si a est égal à 2 -> False

# Exercice 1: Expliquer la procédure qui suit
print("\n** Exercice 1: **")

a = 5
b = 7
v = False
if (
    a > b or v
):  # la condition est fausse, les instructions qui suivent ne seront pas exécutées
    a = 8
    v = True
v = not (v)
if a > b or v:  # la condition est vraie, les instructions qui suivent seront exécutées
    b = 9
print(a, b, v)

# Exercice 2: Ecrire une procédure qui affiche le maximum entre deux nombres
print("\n** Exercice 2: **")

a = 15
b = 7
if a >= b:
    print("Le maximum est:", a)
else:
    print("Le maximum est:", b)

# Exercice 3: Écrire une procédure qui teste si trois nombres peuvent être les côtés d’un triangle
# pour que trois nombres a,b et c puissent être les longueurs des côtés d'un triangle, il faut qu'ils vérifient les trois conditions suivantes: a < b+c, b < a+c, c < a+b
print("\n** Exercice 3: **")

a = 4
b = 3
c = 5

# les trois conditions doivent être vérifiées en même temps, donc on utilise "and" pour les combiner
if (a < b + c) and (b < a + c) and (c < a + b):
    print("triangle")
else:
    print("pas un triangle")

# une autre version: si une des trois conditions n'est pas vérifiée, on n'a pas un triangle
if a >= b + c:
    print("pas un triangle")
elif b >= a + c:
    print("pas un triangle")
elif c >= a + b:
    print("pas un triangle")
else:
    print("triangle")

# Exercice 4:
print("\n** Exercice 4: **")

annee = 1900

if annee % 4 == 0 and annee % 100 != 0:  # l'année est divisible par 4 mais pas par 100
    print("bissextile")
elif annee % 400 == 0:  # l'annee est divisible par 400
    print("bissextile")
else:
    print("pas bissextile")

# une autre version: avec une seule condition
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("bissextile")
else:
    print("pas bissextile")

# une autre version sans "and" et "or": l'ordre des conditions est important
if annee % 400 == 0:
    print("bissextile")
elif annee % 100 == 0:
    print("pas bissextile")
elif annee % 4 == 0:
    print("bissextile")
else:
    print("pas bissextile")
