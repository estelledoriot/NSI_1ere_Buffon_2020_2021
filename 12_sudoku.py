#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Sudoku (test)
#**********************************

# solution avec l'algorithme simple
A = [[0, 4, 0, 7, 6, 5, 0, 2, 0],
     [0, 0, 2, 9, 3, 0, 0, 0, 0],
     [6, 0, 0, 0, 0, 8, 7, 4, 0],
     [1, 5, 0, 8, 2, 0, 0, 0, 0],
     [4, 2, 0, 0, 0, 0, 0, 7, 8],
     [0, 0, 0, 0, 7, 1, 0, 6, 2],
     [0, 6, 4, 1, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 4, 3, 6, 0, 0],
     [0, 3, 0, 6, 9, 2, 0, 1, 0]]

# solution avec l'algorithme simple
B = [[0, 9, 0, 4, 0, 1, 3, 0, 0],
     [2, 0, 4, 0, 9, 5, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 5],
     [0, 0, 0, 3, 0, 0, 0, 0, 2],
     [7, 0, 0, 6, 1, 0, 0, 0, 0],
     [6, 1, 3, 0, 0, 0, 4, 7, 0],
     [0, 8, 0, 5, 3, 0, 2, 0, 1],
     [5, 0, 9, 0, 2, 0, 0, 0, 0],
     [3, 0, 0, 0, 0, 4, 6, 0, 0]]

# solution avec l'algorithme simple
C = [[7, 0, 8, 0, 1, 9, 5, 0, 0],
     [0, 9, 3, 0, 7, 6, 8, 0, 0],
     [0, 5, 0, 3, 0, 0, 0, 0, 9],
     [0, 0, 0, 0, 4, 1, 0, 6, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [9, 4, 0, 7, 6, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 5, 0, 8, 0],
     [0, 0, 9, 6, 3, 0, 4, 1, 0],
     [0, 0, 6, 4, 2, 0, 9, 0, 5]]

# solution avec l'algorithme simple
D = [[0, 2, 3, 0, 0, 0, 0, 0, 1],
     [8, 0, 0, 9, 0, 0, 2, 6, 0],
     [0 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,0],
     [1 ,3 ,5 ,0 ,0, 8 ,4 ,9 ,0],
     [0 ,0 ,0 ,4 ,5 ,9 ,0 ,0 ,0],
     [0 ,9 ,6 ,3 ,0 ,0 ,8 ,5 ,2],
     [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0],
     [0 ,8 ,9 ,0 ,0 ,7 ,0 ,0 ,3],
     [3 ,0 ,0 ,0 ,0 ,0 ,6 ,7 ,0]]

# solution avec l'algorithme simple
E = [[0, 0, 0, 1, 0, 8, 0, 0, 4],
     [4, 5, 0, 0, 3, 6, 8, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 6],
     [0, 7, 1, 0, 0, 5, 0, 0, 0],
     [0, 3, 0, 9, 0, 1, 0, 5, 0],
     [0, 0, 0, 6, 0, 0, 3, 1, 0],
     [9, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 6, 2, 1, 0, 0, 4, 3],
     [3, 0, 0, 5, 0, 4, 0, 0, 0]]

F = [[0, 5, 0, 1, 0, 4, 3, 8, 0],
     [2, 0, 0, 8, 0, 0, 0, 0, 0],
     [3, 8, 0, 6, 0, 0, 1, 0, 0],
     [0, 0, 2, 0, 9, 0, 5, 0, 0],
     [4, 0, 0, 0, 8, 0, 0, 0, 2],
     [0, 7, 0, 0, 1, 0, 0, 0, 0],
     [6, 0, 0, 0, 0, 3, 0, 0, 0],
     [0, 0, 0, 2, 4, 0, 0, 5, 0],
     [0, 1, 3, 0, 0, 0, 0, 0, 0]]

G = [[0, 3, 0, 4, 2, 0, 0, 0, 0],
     [0, 6, 0, 0, 9, 0, 0, 0, 3],
     [0, 0, 0, 8, 0, 0, 0, 4, 2],
     [0, 0, 3, 0, 0, 9, 8, 0, 0],
     [0, 2, 0, 0, 3, 0, 0, 5, 0],
     [0, 0, 1, 5, 0, 0, 3, 0, 0],
     [1, 8, 0, 0, 0, 5, 0, 0, 0],
     [7, 0, 0, 0, 8, 0, 0, 6, 0],
     [0, 0, 0, 0, 1, 7, 0, 9, 0]]

H = [[0, 0, 2, 0, 8, 0, 0, 0, 0],
     [0, 0, 0, 4, 0, 0, 0, 0, 9],
     [8, 1, 0, 0, 0, 0, 3, 0, 0],
     [2, 0, 4, 0, 0, 8, 0, 0, 0],
     [0, 0, 0, 3, 0, 9, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 5, 0, 3],
     [0, 0, 8, 0, 0, 0, 0, 7, 4],
     [1, 0, 0, 0, 0, 2, 0, 0, 0],
     [0, 0, 0, 0, 7, 0, 6, 0, 0]]

I = [[0, 0, 0, 9, 0, 0, 0, 0, 6],
     [0, 5, 0, 0, 0, 0, 8, 0, 0],
     [0, 0, 0, 8, 0, 7, 0, 9, 4],
     [0, 0, 4, 0, 0, 0, 0, 6, 0],
     [1, 7, 0, 6, 0, 9, 0, 3, 2],
     [0, 6, 0, 0, 0, 0, 9, 0, 0],
     [2, 4, 0, 1, 0, 6, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 8, 0],
     [6, 0, 0, 0, 0, 3, 0, 0, 0]]

J = [[9, 0, 4, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 2, 3, 9],
     [0, 0, 0, 0, 0, 0, 7, 0, 0],
     [2, 0, 5, 0, 0, 4, 0, 0, 0],
     [8, 1, 0, 9, 0, 7, 0, 6, 5],
     [0, 0, 0, 5, 0, 0, 3, 0, 2],
     [0, 0, 1, 0, 0, 0, 0, 0, 0],
     [5, 2, 6, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 6, 0, 0, 8, 0, 7]]

K = [[0, 7, 0, 0, 0, 0, 0, 0, 5],
     [5, 0, 0, 0, 1, 9, 0, 0, 0],
     [0, 6, 4, 5, 0, 0, 0, 0, 0],
     [0, 0, 9, 0, 8, 5, 3, 0, 0],
     [8, 4, 0, 0, 0, 0, 0, 5, 9],
     [0, 0, 7, 9, 3, 0, 6, 0, 0],
     [0, 0, 0, 0, 0, 3, 9, 1, 0],
     [0, 0, 0, 2, 5, 0, 0, 0, 6],
     [4, 0, 0, 0, 0, 0, 0, 3, 0]]

# on utilise l'indice i pour les lignes et j pour les colonnes

def copie_sudoku(sudoku):
    '''fait une copie du sudoku'''
    copie = []
    for i in range(9):
        ligne=[]
        for j in range(9):
            ligne.append(sudoku[i][j])
        copie.append(ligne)
    return copie

def afficher(sudoku):
    '''affiche une sudoku de sudoku'''
    for i in range(9): # on parcourt les lignes
        for j in range(9): # on parcourt les colonnes
            print(sudoku[i][j],end=" ")
        print("")

#afficher(B)

def elements_ligne(sudoku,i):
    '''renvoie les éléments présents sur la ligne i du sudoku'''
    liste=[]
    for j in range(9): # on parcourt les colonnes sur la ligne i
        if sudoku[i][j]!=0: # si la case i,j est non nulle, on ajoute sa valeur à la liste
            liste.append(sudoku[i][j])
    return liste

#print(elements_ligne(B,0))

def manquants_ligne(sudoku,i):
    '''renvoie les éléments manquants sur la ligne i du sudoku'''
    liste=[]
    for a in range(1,10): # on parcourt les entiers de 1 à 9
        manquant=True
        for j in range(9): # on parcourt les colonnes sur la ligne i
            if sudoku[i][j]==a:
                manquant=False
                break
        if manquant: # si a est manquant dans la ligne i, on l'ajoute à la liste
            liste.append(a)
    return liste

#print(manquants_ligne(B,0))

def elements_colonne(sudoku,j):
    '''renvoie les éléments présents sur la colonne j du sudoku'''
    liste=[]
    for i in range(9): # on parcourt les lignes sur la colonne j
        if sudoku[i][j]!=0: # si la case i,j est non nulle, on ajoute sa valeur à la liste
            liste.append(sudoku[i][j])
    return liste

#print(elements_colonne(B,0))

def manquants_colonne(sudoku,j):
    '''renvoie les éléments manquants sur la colonne j du sudoku'''
    liste=[]
    for a in range(1,10): # on parcourt les entiers de 1 à 9
        manquant=True
        for i in range(9): # on parcourt les lignes sur la colonne j
            if sudoku[i][j]==a:
                manquant=False
                break
        if manquant: # si a est manquant dans la colonne j, on l'ajoute à la liste
            liste.append(a)
    return liste

#print(manquants_colonne(B,0))

def elements_bloc(sudoku,i,j):
    '''renvoie les éléments présents dans le bloc de la case i,j'''
    liste=[]
    for k in range(3*(i//3),3*(i//3)+3): # on parcourt les lignes du bloc de la case i,j
        for l in range(3*(j//3),3*(j//3)+3): # on parcourt les colonnes du bloc de la case i,j
            if sudoku[k][l]!=0:
                liste.append(sudoku[k][l])
    return liste

#print(elements_bloc(B,0,3))

def manquants_bloc(sudoku,i,j):
    '''renvoie les éléments manquants sur le bloc de la case i,j du sudoku'''
    liste=[]
    for a in range(1,10): # on parcourt les entiers de 1 à 9
        manquant=True
        for k in range(3*(i//3),3*(i//3)+3): # on parcourt les lignes du bloc de la case i,j
            for l in range(3*(j//3),3*(j//3)+3): # on parcourt les colonnes du bloc de la case i,j
                if sudoku[k][l]==a:
                    manquant=False
        if manquant: # si a est manquant dans le bloc, on l'ajoute à la liste
            liste.append(a)
    return liste

#print(manquants_bloc(B,0,3))

def possibles(sudoku,i,j):
    '''renvoie les éléments qui sont possibles pour la case i,j'''
    if sudoku[i][j]!=0: # si la case est déjà remplie, il n'y a pas d'éléments possibles
        return []
    else:
        liste=[]
        for a in range(1,10):
            possible=True
            for k in range(9):
                if sudoku[i][k]==a: # si a est dans la ligne i, il n'est pas possible pour la case i,j
                    possible=False
                    break
            if possible:
                for l in range(9):
                    if sudoku[l][j]==a:# si a est dans la colonne j, il n'est pas possible pour la case i,j
                        possible=False
                        break
            if possible:
                for k in range(3*(i//3),3*(i//3)+3): # on parcourt les lignes du bloc de la case i,j
                    for l in range(3*(j//3),3*(j//3)+3): # on parcourt les colonnes du bloc de la case i,j
                        if sudoku[k][l]==a: # si a est dans le bloc de i,j, il n'est pas possible pour la case i,j
                            possible=False
            if possible:
                liste.append(a)
        return liste

#print(possibles(B,0,8))

def resoud_cases(sudoku):
    '''remplace les 0 dans les cases où il n'y a qu'une seule valeur possible'''
    changement = False
    for i in range(9): # on parcourt les lignes
        for j in range(9): # on parcourt les colonnes
            if sudoku[i][j]==0 and len(possibles(sudoku,i,j))==1:
                sudoku[i][j] = possibles(sudoku,i,j)[0]
                changement=True
    return changement

#resoud_cases(B)

def resoud_lignes(sudoku):
    '''remplace les 0 dans une case si c'est le seul endroit possible sur une ligne'''
    changement = False
    for i in range(9): # on parcourt les lignes
        manquants = manquants_ligne(sudoku,i)
        for a in manquants: # on regarde chaque élément manquant dans la ligne i
            possibilite=0
            indice=0
            for j in range(9): # on parcourt les cases de la ligne i
                for e in possibles(sudoku,i,j): # on parcourt tous les éléments possibles de la case i,j
                    if e==a:
                        indice=j
                        possibilite+=1
                        break
            if possibilite==1: # s'il n'y a qu'une seule case possible dans la ligne i
                sudoku[i][indice]=a
                changement=True
    return changement

#resoud_lignes(B)

def resoud_colonnes(sudoku):
    '''remplace les 0 dans une case si c'est le seul endroit possible sur une colonne'''
    changement = False
    for j in range(9): # on parcourt les colonnes
        manquants = manquants_colonne(sudoku,j)
        for a in manquants: # on regarde chaque élément manquant dans la colonne j
            possibilite=0
            indice=0
            for i in range(9): # on parcourt les cases de la colonne j
                for e in possibles(sudoku,i,j): # on parcourt tous les éléments possibles de la case i,j
                    if e==a:
                        indice=i
                        possibilite+=1
                        break
            if possibilite==1: # s'il n'y a qu'une seule case possible dans la colonne j
                sudoku[indice][j]=a
                changement=True
    return changement

#resoud_colonnes(B)

def resoud_blocs(sudoku):
    '''remplace les 0 dans une case si c'est le seul endroit possible dans un bloc'''
    changement = False
    i=0
    while i<9:
        j=0
        while j<9:
            manquants = manquants_bloc(sudoku,i,j)
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
                                break
                if possibilite==1: # s'il n'y a qu'une seule case possible dans la colonne j
                    sudoku[indicei][indicej]=a
                    changement=True
            j=j+3
        i=i+3
    return changement

#resoud_blocs(B)

def resolution_simple(sudoku):
    '''resolution simple d'un sudoku sans faire d'hypothèses'''
    copie=copie_sudoku(sudoku)
    changement=True
    while changement:
        changement_cases = resoud_cases(copie)
        changement_lignes = resoud_lignes(copie)
        changement_colonnes = resoud_colonnes(copie)
        changement_blocs = resoud_blocs(copie)
        changement = changement_cases or changement_lignes or changement_colonnes or changement_blocs
    return copie

afficher(resolution_simple(C))

def fini(sudoku):
    '''renvoie si un sudoku est terminé ou non'''
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                return False
    return True

#print(fini(resolution_simple(A)))

def impossible(sudoku):
    '''renvoie si un sudoku est impossible ou non'''
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0 and possibles(sudoku,i,j)==[]:
                return True
    return False

#print(impossible(resolution_Simple(A)))

def case_hypothese(sudoku):
    '''renvoie les coordonnées de la case sur laquelle on va faire une hypothèse (la case qui a le moins d'éléments possibles'''
    nb_possibles=10
    indicei=9
    indicej=9
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                nb = len(possibles(sudoku,i,j))
                if nb<nb_possibles:
                    nb_possibles=nb
                    indicei=i
                    indicej=j
    return indicei,indicej

#print(case_hypothese(resolution_simple(F)))

# résolution complète d'un sudoku
def solution_complete(g):
    sudoku = copie_sudoku(g)
    sudoku = resolution_simple(sudoku)
    if impossible(sudoku):
        return True,False,sudoku
    elif fini(sudoku):
        return False,True,sudoku
    else:
        i,j=case_hypothese(sudoku)
        p = possibles(sudoku,i,j)
        for k in range(len(p)):
            sudoku1=copie_sudoku(sudoku)
            sudoku1[i][j]=p[k]
            imp,fin,test = solution_complete(sudoku1)
            if fin:
                return imp,fin,test

#afficher(solution_complete(J)[2])

def poss(grid,x,y,n):
    for i in range(9):
        if grid[i][y]==n:
            return False
    for j in range(9):
        if grid[x][j]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j]==n:
                return False
    return True

def solve(grille):
    for x in range(9):
        for y in range(9):
            if grille[x][y]==0:
                for n in range(1,10):
                    if poss(grille,x,y,n):
                        grille[x][y]=n
                        solve(grille)
                        grille[x][y]=0
                return
