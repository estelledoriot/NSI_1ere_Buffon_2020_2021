#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Sudoku 4
#**********************************

# grilles
C = [[7, 0, 8, 0, 1, 9, 5, 0, 0],
     [0, 9, 3, 0, 7, 6, 8, 0, 0],
     [0, 5, 0, 3, 0, 0, 0, 0, 9],
     [0, 0, 0, 0, 4, 1, 0, 6, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [9, 4, 0, 7, 6, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 5, 0, 8, 0],
     [0, 0, 9, 6, 3, 0, 4, 1, 0],
     [0, 0, 6, 4, 2, 0, 9, 0, 5]]

A = [[0, 4, 0, 7, 6, 5, 0, 2, 0],
     [0, 0, 2, 9, 3, 0, 0, 0, 0],
     [6, 0, 0, 0, 0, 8, 7, 4, 0],
     [1, 5, 0, 8, 2, 0, 0, 0, 0],
     [4, 2, 0, 0, 0, 0, 0, 7, 8],
     [0, 0, 0, 0, 7, 1, 0, 6, 2],
     [0, 6, 4, 1, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 4, 3, 6, 0, 0],
     [0, 3, 0, 6, 9, 2, 0, 1, 0]]

B = [[0, 9, 0, 4, 0, 1, 3, 0, 0],
     [2, 0, 4, 0, 9, 5, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 5],
     [0, 0, 0, 3, 0, 0, 0, 0, 2],
     [7, 0, 0, 6, 1, 0, 0, 0, 0],
     [6, 1, 3, 0, 0, 0, 4, 7, 0],
     [0, 8, 0, 5, 3, 0, 2, 0, 1],
     [5, 0, 9, 0, 2, 0, 0, 0, 0],
     [3, 0, 0, 0, 0, 4, 6, 0, 0]]

# fonction afficher
def afficher(grille):
    for i in range(9):
        if i%3==0:
            print("-"*25)
        for j in range(9):
            if j%3==0:
                print("|",end=" ")
            print(grille[i][j],end=" ")
        print("|")
    print("-"*25)

afficher(C)

# fonction fini
def fini(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                return False
    return True

#print(fini(C))

# Question 1:
def possibles(sudoku,i,j):
    # si la case est déjà remplie, il n'est pas possible de la remplir
    # on renvoie donc la liste vide
    if sudoku[i][j]!=0:
        return []
    else:
        # on va combiner le code écrit au td précédent dans les fonctions
        # manquants_ligne, manquants_colonne et manquants_carre
        # si un chiffre n'est present ni dans la ligne, ni dans la colonne, ni dans le carré
        # de la case (i,j), on l'ajoute a la liste des chiffres possibles
        liste=[]
        for a in range(1,10): # on parcourt les entiers de 1 à 9
            # a est possible tant qu'il n'a pas été trouvé dans la ligne, la colonne ou le carré
            possible=True
            # on parcourt la ligne i
            for k in range(9):
                # si a est dans la ligne i, il n'est pas possible pour la case (i,j)
                if sudoku[i][k]==a:
                    possible=False
            # on parcourt la colonne j
            for l in range(9):
                # si a est dans la colonne j, il n'est pas possible pour la case (i,j)
                if sudoku[l][j]==a:
                    possible=False
            # on parcourt le carré contenant la case (i,j)
            i1=3*(i//3)
            j1=3*(j//3)
            for k in range(i1,i1+3): # on parcourt les lignes du carre de la case i,j
                for l in range(j1,j1+3): # on parcourt les colonnes du carre de la case i,j
                    # si a est dans le carre de i,j, il n'est pas possible pour la case i,j
                    if sudoku[k][l]==a:
                        possible=False
            # si a n'est ni dans la ligne, ni dans la colonne, ni dans le carre
            # on l'ajoute à la liste des chiffres possibles
            if possible:
                liste.append(a)
        return liste

#print(possibles(C,0,1))

# Question 2:
def remplir_cases(sudoku):
    # on remplace les 0 dans les cases où il n'y a qu'un seul chiffre possible
    for i in range(9): # on parcourt les lignes
        for j in range(9): # on parcourt les colonnes
            # si la case est vide et qu'il n'y a qu'un seule chiffre possible
            if sudoku[i][j]==0 and len(possibles(sudoku,i,j))==1:
                sudoku[i][j] = possibles(sudoku,i,j)[0]

#remplir_cases(C)
#afficher(C)

# Question 3:
def manquants_ligne(sudoku,i):
    # fonction manquants_ligne du td précédent
    # renvoie la liste des chiffres manquants dans la ligne i
    liste=[]
    for a in range(1,10):
        manquant=True
        for j in range(9):
            if sudoku[i][j]==a:
                manquant=False
        if manquant:
            liste.append(a)
    return liste

def remplir_lignes(sudoku):
    # place un chiffre dans une case si c'est la seule case vide de sa ligne
    # où le chiffre peut être placé
    for i in range(9): # on parcourt les lignes du sudoku
        manquants = manquants_ligne(sudoku,i) # liste des chiffres manquants sur la ligne i
        # pour chaque chiffre a manquant sur la ligne i, on regarde dans quelle case (i,j)
        # il peut être placé
        for a in manquants:
            possibilite=0 # nombre de cases possibles pour a
            indice=0 # indice de la case possible
            for j in range(9): # on parcourt les cases de la ligne i
                # on cherche si a fait partie des chiffres possibles à placer dans la case (i,j)
                for e in possibles(sudoku,i,j):
                    if e==a:
                        indice=j
                        possibilite+=1
            # s'il n'y a qu'une seule case possible pour a sur la ligne i,
            # on écrit a dans cette case
            if possibilite==1:
                sudoku[i][indice]=a

#remplir_lignes(C)
#afficher(C)

# Question 4:
def manquants_colonne(sudoku,j):
    # fonction manquants_colonne du td précédent
    # renvoie la liste des chiffres manquants dans la colonne j
    liste=[]
    for a in range(1,10):
        manquant=True
        for i in range(9):
            if sudoku[i][j]==a:
                manquant=False
        if manquant:
            liste.append(a)
    return liste

def remplir_colonnes(sudoku):
    # place un chiffre dans une case si c'est la seule case vide de sa colonne
    # où le chiffre peut être placé
    for j in range(9): # on parcourt les colonnes
        manquants = manquants_colonne(sudoku,j) # liste des chiffres manquants dans la colonne j
        # pour chaque chiffre a manquant sur la colonne j, on regarde dans quelle case (i,j)
        # il peut être placé
        for a in manquants:
            possibilite=0 # nombre de cases possibles pour a
            indice=0 # indice de la case possible
            for i in range(9): # on parcourt les cases de la colonne j
                # on cherche si a fait partie des chiffres possibles à placer dans la case (i,j)
                for e in possibles(sudoku,i,j):
                    if e==a:
                        indice=i
                        possibilite+=1
            # s'il n'y a qu'une seule case possible pour a sur la colonne j,
            # on écrit a dans cette case
            if possibilite==1:
                sudoku[indice][j]=a

#remplir_colonnes(C)
#afficher(C)

# Question 5:
def manquants_carre(sudoku,i,j):
    # fonction manquants_carre du td précédent
    # renvoie la liste des chiffres manquants dans le carre de la case (i,j)
    liste=[]
    i1 = 3*(i//3)
    j1 = 3*(j//3)
    for a in range(1,10):
        manquant=True
        for k in range(i1,i1+3):
            for l in range(j1,j1+3):
                if sudoku[k][l]==a:
                    manquant=False
        if manquant:
            liste.append(a)
    return liste

def remplir_carres(sudoku):
    # place un chiffre dans une case si c'est la seule case vide de son carré
    # où le chiffre peut être placé
    i=0
    # on parcourt tous les carrés: (i,j) sont les coordonnées de la case
    # en haut à gauche de chaque carré
    while i<9:
        j=0
        while j<9:
            manquants = manquants_carre(sudoku,i,j) # liste des chiffres manquants dans le carré
            # pour chaque chiffre a manquant dans le carré, on regarde
            # dans quelle case il peut être placé
            for a in manquants:
                possibilite=0 # nombre de cases possibles pour a
                indicei=0 # indice i de la case possible
                indicej=0 # indice j de la case possible
                # on parcourt les cases du carré
                for k in range(3):
                    for l in range(3):
                        # on cherche si a fait partie des chiffres possibles
                        # à placer dans la case
                        for e in possibles(sudoku,i+k,j+l):
                            if e==a:
                                indicei=i+k
                                indicej=j+l
                                possibilite+=1
                # s'il n'y a qu'une seule case possible pour a sur la colonne j,
                # on écrit a dans cette case
                if possibilite==1:
                    sudoku[indicei][indicej]=a
            j=j+3
        i=i+3

#remplir_carres(C)
#afficher(C)

