# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Cours sur les boucles for
# **********************************

# Exemple 1: range(n)
# *******************
print("\n** Exemple:")

print("Les 10 premiers nombres entiers:")
n = 10
for i in range(n):
    print(i)

# Exercice 1:
# ************
print("\n** Exercice 1:")

print("Les 10 premiers nombres pairs:")
for i in range(n):
    print(2 * i)

# Exercice 2:
# ************
print("\n** Exercice 2:")

print("Triangle:")
for i in range(1, 8):
    print("*" * i)

# Exercice 3:
# ************
print("\n** Exercice 3:")

print("Les nombres premiers inférieurs à 20:")
n = 20
for i in range(n):
    if i % 2 == 0:
        print(i)

# Exercice 4:
# ************
print("\n** Exercice 4:")

n = 30
compteur = 0
for i in range(n):
    if i % 3 == 0:
        compteur += 1
print("Il y a", compteur, "multiples de 3 inférieurs à 30")

# Exercice 5:
# ************
print("\n** Exercice 5:")

n = 20
somme = 0
for i in range(n):
    somme += i
print("La somme des entiers de 1 à 20 est:", somme)

# Exemple:
# *********
print("\n** Exemple:")

for i in range(5):
    for j in range(4):
        print(i, "-", j)

# Exercice 6:
# ************
print("\n** Exercice 6:")

for i in range(1, 11):
    print("\nTABLE DE ", i, ":")
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
