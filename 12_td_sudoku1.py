# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Sudoku 1
# **********************************

# tableau
t = [4, 0, 0, 9, 0, 5, 0, 3, 6]

# Question 1:
# ************
print("\n** Question 1:")

print(t[4])

# Question 2:
# ************
print("\n** Question 2:")

print(t[3])

# Question 3:
# ************
print("\n** Question 3:")

t[8] = 8  # le dernier element du tableau a pour indice 8
print(t)

# Question 4:
# ************
print("\n** Question 4:")

for i in range(9):  # on fait une boucle pour parcourir le tableau
    t[i] = 0  # i est l'indice de la case, t[i] est le contenu de la case d'indice i
print(t)

# tableau
t = [4, 0, 0, 9, 0, 5, 0, 3, 6]

# Question 5:
# ************
print("\n** Question 5:")

for i in range(9):
    if i % 2 == 0:  # on teste si l'indice de la case (i) est pair
        print(t[i])  # on affiche le contenu de la case

# Question 6:
# ************
print("\n** Question 6:")

for i in range(9):
    if t[i] % 2 == 0:  # on teste si le contenu de la case (t[i]) est pair
        print(t[i])  # on affiche le contenu de la case

# Question 7:
# ************
print("\n** Question 7:")

for i in range(9):
    if t[i] != 0:  # les cases remplies ne contienent pas de 0
        print(t[i])

# Question 8:
# ************
print("\n** Question 8:")

for i in range(9):
    if t[i] != 0 and t[i] % 2 == 0:  # les cases sont paires et differentes de 0
        print(t[i])

# Question 9:
# ************
print("\n** Question 9:")

c = 0  # pour compter, on utilise une variable compteur c
for i in range(9):
    if t[i] == 0:
        c = c + 1  # si la case est vide (contenant 0), on incremente le compteur c
print(c)

# Question 10:
# ************
print("\n** Question 10:")

c = 0  # pour compter, on utilise une variable compteur c
for i in range(9):
    if t[i] != 0 and t[i] % 2 == 0:
        c = c + 1  # si la case contient un nombre pair, on incremente le compteur c
print(c)

# Question 11:
# ************
print("\n** Question 11:")

s = 0  # s contient la somme des cases parcourues
for i in range(9):
    s = s + t[i]  # a chaque tour de boucle, on rajoute a s le contenu de la case i
print(s)

# Question 12:
# ************
print("\n** Question 12:")

m = t[0]  # m contient le maximum des cases deja parcourues
for i in range(9):
    if t[i] > m:
        m = t[i]  # si la case i est plus grande que m, on remplace m par t[i]
print(m)

# Question 13:
# ************
print("\n** Question 13:")

m = t[0]  # m contient le maximum des cases deja parcourues
j = 0  # j contient l'indice de la case maximum
for i in range(9):
    if t[i] > m:
        m = t[i]  # si la case i est plus grande que m, on remplace m par t[i]
        j = i  # on remplace j par i
print(j)

# Question 14:
# ************
print("\n** Question 14:")

# on teste tous les entiers de 1 a 9 (pour voir si ils sont dans t)
for a in range(1, 10):
    present = False  # present represente le fait que a est contenu dans t
    for i in range(9):  # on parcourt le tableau t pour voir si a est dedans
        if t[i] == a:
            present = True  # si a est egal a t[i], a est present dans le tableau
    if not present:
        print(a)  # si a n'est pas present dans t, on l'affiche
