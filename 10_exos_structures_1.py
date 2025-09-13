# *********************************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Exercices sur les structures de contrôle 1
# *********************************************

# Exercice 1
# ***********
print("\n** Exercice 1:")

a = 7
b = 15

if a < b:
    print("La distance entre", a, "et", b, "est:", b - a)
else:
    print("La distance entre", a, "et", b, "est:", a - b)

# Exercice 2
# ***********
print("\n**Exercice 2:")

xA = 0
yA = 0
xB = 1
yB = 1
xC = 8
yC = 8

if (xA - xB) * (yC - yA) == (yA - yB) * (xC - xA):
    print("les points sont alignés")
else:
    print("les points ne sont pas alignés")

# Exercice 3
# ***********
print("\n** Exercice 3:")

for i in range(1, 101):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# Exercice 4 - 1)
# ****************
print("\n** Exercice 4: 1)")

n = 50
s = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        s = s + i
print("La somme des nombres impairs inférieurs à 50 est:", s)

# Exercice 4 - 2)
# ****************
print("\n** Exercice 4: 2)")

n = 50
s = 0

for i in range(1, n + 1):
    s = s + i * i
print("La somme des carrés des nombres impairs inférieurs à 50 est:", s)

# Exercice 5
# ***********
print("\n** Exercice 5:")

m = 4
n = 3

for i in range(m):
    for j in range(1, n + 1):
        print("*" * j)

# Exercice 6 - 1)
# ****************
print("\n** Exercice 6: 1)")

nombre = 10
somme = 0

for i in range(1, 7):
    for j in range(1, 7):
        if i + j == nombre:
            print(i, "+", j, "=", nombre)
            somme = somme + 1

print("Il y a", somme, "possibilités de faire 10 avec 2 dés")

# Exercice 6 - 2)
# ****************
print("\n** Exercice 6: 2)")

nombre = 10
somme = 0

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i + j + k == nombre:
                print(i, "+", j, "+", k, "=", nombre)
                somme = somme + 1

print("Il y a", somme, "possibilités de faire 10 avec 3 dés")

# Exercice 7 - 1)
# ****************
print("\n** Exercice 7: 1)")

n = 23494
print("Les diviseurs de", n, "sont: ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# Exercice 7 - 2)
# ****************
print("\n** Exercice 7: 2)")

n = 12**6
compteur = 0

for i in range(1, n + 1):
    if n % i == 0:
        compteur += 1

print("Il y a", compteur, "diviseurs de", n)

# Exercice 7 - 3)
# ****************
print("\n** Exercice 7: 3)")

n = 2020
somme = 0

for i in range(1, n + 1):
    if n % i == 0:
        somme += i

print("La somme des diviseurs de", n, "est", somme)

# Exercice 8: 1)
# ***************
print("\n** Exercice 8: 1)")

n = 8345
i = n
compteur = 0

while i > 0:
    compteur = compteur + 1
    i = i // 10

print("Le nombre de chiffres de", n, "est", compteur)

# Exercice 8: 2)
# ***************
print("\n** Exercice 8: 2)")

n = 8345
i = n
somme = 0

while i > 0:
    somme = somme + i % 10
    i = i // 10

print("La somme des chiffres de", n, "est", somme)

# Exercice 9:
# ************
print("\n** Exercice 9:")


def nom_du_jour(jour, mois, annee):
    nb_jours = 0
    for i in range(1900, annee):
        if i == 1900:
            nb_jours += 365
        elif i % 4 == 0:
            nb_jours += 366
        else:
            nb_jours += 365
    for j in range(1, mois):
        if j == 1:
            nb_jours += 31
        elif j == 2 and annee != 1900 and annee % 4 == 0:
            nb_jours += 29
        elif j == 2:
            nb_jours += 28
        elif j == 3:
            nb_jours += 31
        elif j == 4:
            nb_jours += 30
        elif j == 5:
            nb_jours += 31
        elif j == 6:
            nb_jours += 30
        elif j == 7:
            nb_jours += 31
        elif j == 8:
            nb_jours += 31
        elif j == 9:
            nb_jours += 30
        elif j == 10:
            nb_jours += 31
        elif j == 11:
            nb_jours += 30
        elif j == 12:
            nb_jours += 31
    nb_jours += jour - 1
    reste = nb_jours % 7
    if reste == 0:
        print("lundi")
    elif reste == 1:
        print("mardi")
    elif reste == 2:
        print("mercredi")
    elif reste == 3:
        print("jeudi")
    elif reste == 4:
        print("vendredi")
    elif reste == 5:
        print("samedi")
    else:
        print("dimanche")


nom_du_jour(1, 1, 1900)
nom_du_jour(1, 1, 2000)
nom_du_jour(1, 1, 2019)
nom_du_jour(1, 1, 2020)
nom_du_jour(18, 6, 1940)
nom_du_jour(20, 7, 1969)
nom_du_jour(4, 11, 2008)
nom_du_jour(25, 9, 2020)
