#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Sudoku complet
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

# fonction possibles (règle 1)
def possibles(sudoku,i,j):
    # si la case est déjà remplie, il n'est pas possible de la remplir
    # on renvoie donc la liste vide
    if sudoku[i][j]!=0:
        return []
    else:
        liste=[]
        for a in range(1,10):
            possible=True
            for k in range(9):
                if sudoku[i][k]==a:
                    possible=False
            for l in range(9):
                if sudoku[l][j]==a:
                    possible=False
            i1=3*(i//3)
            j1=3*(j//3)
            for k in range(i1,i1+3):
                for l in range(j1,j1+3):
                    if sudoku[k][l]==a:
                        possible=False
            if possible:
                liste.append(a)
        return liste

#print(possibles(C,0,1))

# fonction remplir_cases (règle 1)
def remplir_cases(sudoku):
    # on remplace les 0 dans les cases où il n'y a qu'un seul chiffre possible
    changement=False
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0 and len(possibles(sudoku,i,j))==1:
                sudoku[i][j] = possibles(sudoku,i,j)[0]
                changement=True
    return changement

#remplir_cases(C)
#afficher(C)

# fonction manquants_ligne (règle 2)
def manquants_ligne(sudoku,i):
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

# fonction remplir_lignes (règle 2)
def remplir_lignes(sudoku):
    # place un chiffre dans une case si c'est la seule case vide de sa ligne
    # où le chiffre peut être placé
    changement = False
    for i in range(9):
        manquants = manquants_ligne(sudoku,i)
        for a in manquants:
            possibilite=0
            indice=0
            for j in range(9):
                for e in possibles(sudoku,i,j):
                    if e==a:
                        indice=j
                        possibilite+=1
            if possibilite==1:
                sudoku[i][indice]=a
                changement = True
    return changement

#remplir_lignes(C)
#afficher(C)

# fonction manquants_colonne (règle 3)
def manquants_colonne(sudoku,j):
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

# fonction remplir_colonnes (règle 3)
def remplir_colonnes(sudoku):
    # place un chiffre dans une case si c'est la seule case vide de sa colonne
    # où le chiffre peut être placé
    changement=False
    for j in range(9):
        manquants = manquants_colonne(sudoku,j)
        for a in manquants:
            possibilite=0
            indice=0
            for i in range(9):
                for e in possibles(sudoku,i,j):
                    if e==a:
                        indice=i
                        possibilite+=1
            if possibilite==1:
                sudoku[indice][j]=a
                changement=True
    return changement

#remplir_colonnes(C)
#afficher(C)

# fonction manquants_carre (règle 4)
def manquants_carre(sudoku,i,j):
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

# fonction remplir_carres (règle 4)
def remplir_carres(sudoku):
    # place un chiffre dans une case si c'est la seule case vide de son carré
    # où le chiffre peut être placé
    changement = False
    i=0
    while i<9:
        j=0
        while j<9:
            manquants = manquants_carre(sudoku,i,j)
            for a in manquants:
                possibilite=0
                indicei=0
                indicej=0
                for k in range(3):
                    for l in range(3):
                        for e in possibles(sudoku,i+k,j+l):
                            if e==a:
                                indicei=i+k
                                indicej=j+l
                                possibilite+=1
                if possibilite==1:
                    sudoku[indicei][indicej]=a
                    changement=True
            j=j+3
        i=i+3
    return changement

#remplir_carres(C)
#afficher(C)

# fonction resolution_simple
def resolution_simple(sudoku):
    # resolution simple d'un sudoku
    changement=True
    while changement:
        changement = remplir_carres(sudoku) or remplir_lignes(sudoku) or remplir_colonnes(sudoku) or remplir_cases(sudoku)

resolution_simple(C)
afficher(C)
