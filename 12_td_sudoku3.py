# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Sudoku 3
# **********************************

# grille
C = [
    [7, 0, 8, 0, 1, 9, 5, 0, 0],
    [0, 9, 3, 0, 7, 6, 8, 0, 0],
    [0, 5, 0, 3, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 4, 1, 0, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 4, 0, 7, 6, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 5, 0, 8, 0],
    [0, 0, 9, 6, 3, 0, 4, 1, 0],
    [0, 0, 6, 4, 2, 0, 9, 0, 5],
]


# fonction afficher
# ******************
def afficher(grille):
    for i in range(9):
        if i % 3 == 0:
            print("-" * 25)
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            print(grille[i][j], end=" ")
        print("|")
    print("-" * 25)


# Question 1:
# ************
print("\n** Question 1:")


def pairs(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


print(pairs(10))

# Question 2:
# ************
print("\n** Question 2:")


def fini(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True


print(fini(C))

# Question 3:
# ************
print("\n** Question 3:")


def chiffres_ligne(sudoku, i):
    liste = []
    for j in range(9):  # on parcourt les colonnes sur la ligne i
        if (
            sudoku[i][j] != 0
        ):  # si la case i,j est non nulle, on ajoute sa valeur à la liste
            liste.append(sudoku[i][j])
    return liste


print(chiffres_ligne(C, 0))

# Question 4:
# ************
print("\n** Question 4:")


def manquants_ligne(sudoku, i):
    liste = []
    for a in range(1, 10):  # on parcourt les entiers de 1 à 9
        manquant = True
        for j in range(9):  # on parcourt les colonnes sur la ligne i
            if sudoku[i][j] == a:
                manquant = False
        if manquant:  # si a est manquant dans la ligne i, on l'ajoute à la liste
            liste.append(a)
    return liste


print(manquants_ligne(C, 0))

# Question 5:
# ************
print("\n** Question 5:")


def chiffres_colonne(sudoku, j):
    liste = []
    for i in range(9):  # on parcourt les lignes sur la colonne j
        if (
            sudoku[i][j] != 0
        ):  # si la case i,j est non nulle, on ajoute sa valeur à la liste
            liste.append(sudoku[i][j])
    return liste


print(chiffres_colonne(C, 0))

# Question 6:
# ************
print("\n** Question 6:")


def manquants_colonne(sudoku, j):
    liste = []
    for a in range(1, 10):  # on parcourt les entiers de 1 à 9
        manquant = True
        for i in range(9):  # on parcourt les lignes sur la colonne j
            if sudoku[i][j] == a:
                manquant = False
        if manquant:  # si a est manquant dans la colonne j, on l'ajoute à la liste
            liste.append(a)
    return liste


print(manquants_colonne(C, 0))

# Question 9:
# ************
print("\n** Question 9:")


def chiffres_carre(sudoku, i, j):
    liste = []
    i1 = 3 * (i // 3)
    j1 = 3 * (j // 3)
    for k in range(i1, i1 + 3):  # on parcourt les lignes du carre de la case i,j
        for l in range(j1, j1 + 3):  # on parcourt les colonnes du carre de la case i,j
            if sudoku[k][l] != 0:
                liste.append(sudoku[k][l])
    return liste


print(chiffres_carre(C, 1, 1))

# Question 10:
# ************
print("\n** Question 10:")


def manquants_carre(sudoku, i, j):
    liste = []
    i1 = 3 * (i // 3)
    j1 = 3 * (j // 3)
    for a in range(1, 10):  # on parcourt les entiers de 1 à 9
        manquant = True
        for k in range(i1, i1 + 3):  # on parcourt les lignes du bloc de la case i,j
            for l in range(
                j1, j1 + 3
            ):  # on parcourt les colonnes du bloc de la case i,j
                if sudoku[k][l] == a:
                    manquant = False
        if manquant:  # si a est manquant dans le bloc, on l'ajoute à la liste
            liste.append(a)
    return liste


print(manquants_carre(C, 1, 1))
