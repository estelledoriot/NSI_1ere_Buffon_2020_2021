# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Exercices sur les fonctions
# **********************************

from math import *

# Exercice 1
# ***********
print("\n** Exercice 1:")


def aire_trapeze(a, b, h):
    return (a + b) * h / 2


print("L'aire du trapèze est:", aire_trapeze(2, 4, 5))

# Exercice 2
# ***********
print("\n** Exercice 2:")


def aire_triangle(a, b, c):
    p = (a + b + c) / 2
    a = sqrt(p * (p - a) * (p - b) * (p - c))
    return a


print("L'aire du triangle est:", aire_triangle(3, 4, 5))

# Exercice 3
# ***********
print("\n** Exercice 3:")


def distance_au_carre(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def est_rectangle(xa, ya, xb, yb, xc, yc):
    ab2 = distance_au_carre(xa, ya, xb, yb)
    ac2 = distance_au_carre(xa, ya, xc, yc)
    bc2 = distance_au_carre(xb, yb, xc, yc)
    return (bc2 == ab2 + ac2) or (ab2 == ac2 + bc2) or (ac2 == ab2 + bc2)


if est_rectangle(5, 2, 2, 2, 2, 6):
    print("Le triangle est rectangle")
else:
    print("Le triangle n'est pas rectangle")

# Exercice 4
# ***********
print("\n** Exercice 4:")


def est_premier(n):
    if n == 1:
        return False  # 1 n'est pas premier
    for i in range(2, floor(sqrt(n)) + 1):
        if (
            n % i == 0
        ):  # si n admet un diviseur autre que 1 et lui-même il n'est pas premier
            return False
    return True  # sinon il est premier


def ex4_1():
    for i in range(41):
        if not est_premier(i * i - i + 41):
            return False
    return True


if ex4_1():
    print("Tous les f(n) pour n entre 0 et 40 sont premiers")
else:
    print("Il existe un f(n) non premier pour n entre 0 et 40")


def ex4_2():
    compteur = 0
    for i in range(101):
        if not est_premier(i * i - i + 41):
            compteur = compteur + 1
    return compteur


print("Il y a", ex4_2(), "f(n) non premiers pour n inférieur à 100")

# Exercice 5
# ***********
print("\n** Exercice 5:")


def somme_1(n):
    somme = 0
    for i in range(1, n + 1):
        somme = somme + i
    return somme


print("La somme des entiers de 1 à 100 est:", somme_1(100))


def somme_3(n):
    somme = 0
    for i in range(1, n + 1):
        somme = somme + i * i * i
    return somme


print("La somme des cubes des entiers de 1 à 100 est:", somme_3(100))
if somme_3(100) == somme_1(100) ** 2:
    print("s3(100) = s1(100 ** 2")
else:
    print("s3(100) != s1(100 ** 2")
