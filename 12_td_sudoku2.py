#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Sudoku 2
#**********************************

# grille
C = [[7, 0, 8, 0, 1, 9, 5, 0, 0],
     [0, 9, 3, 0, 7, 6, 8, 0, 0],
     [0, 5, 0, 3, 0, 0, 0, 0, 9],
     [0, 0, 0, 0, 4, 1, 0, 6, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [9, 4, 0, 7, 6, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 5, 0, 8, 0],
     [0, 0, 9, 6, 3, 0, 4, 1, 0],
     [0, 0, 6, 4, 2, 0, 9, 0, 5]]

# fonction afficher
#******************

def afficher(grille):
    for i in range(9):
        if i % 3 == 0:
            print("-" * 25)
        for j in range(9):
            if j % 3 == 0:
                print("|", end = " ")
            print(grille[i][j], end = " ")
        print("|")
    print("-" * 25)

# Question 1:
#************
print("\n** Question 1:")

print(C[5][0])

# Question 2:
#************
print("\n** Question 2:")

print(C[5])

# Question 3:
#************
print("\n** Question 3:")

C[5][0] = 0
afficher(C)

C = [[7, 0, 8, 0, 1, 9, 5, 0, 0],
     [0, 9, 3, 0, 7, 6, 8, 0, 0],
     [0, 5, 0, 3, 0, 0, 0, 0, 9],
     [0, 0, 0, 0, 4, 1, 0, 6, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [9, 4, 0, 7, 6, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 5, 0, 8, 0],
     [0, 0, 9, 6, 3, 0, 4, 1, 0],
     [0, 0, 6, 4, 2, 0, 9, 0, 5]]

# Question 4:
#************
print("\n** Question 4:")

for j in range(9):
    print(C[5][j])

# Question 5:
#************
print("\n** Question 5:")

for i in range(9):
    print(C[i][2])

# Question 6:
#************
print("\n** Question 6:")

for i in range(9):
    for j in range(9):
        C[i][j] = 0
afficher(C)

C = [[7, 0, 8, 0, 1, 9, 5, 0, 0],
     [0, 9, 3, 0, 7, 6, 8, 0, 0],
     [0, 5, 0, 3, 0, 0, 0, 0, 9],
     [0, 0, 0, 0, 4, 1, 0, 6, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [9, 4, 0, 7, 6, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 5, 0, 8, 0],
     [0, 0, 9, 6, 3, 0, 4, 1, 0],
     [0, 0, 6, 4, 2, 0, 9, 0, 5]]

# Question 7:
#************
print("\n** Question 7:")

for j in range(9):
    if C[3][j] != 0:
        print(C[3][j])

# Question 8:
#************
print("\n** Question 8:")

compteur = 0
for j in range(9):
    if C[3][j] != 0:
        compteur = compteur + 1
print(compteur)

# Question 9:
#************
print("\n** Question 9:")

for i in range(9):
    if C[i][4] != 0:
        print(C[i][4])

# Question 10:
#************
print("\n** Question 10:")

compteur = 0
for i in range(9):
    if C[i][4] != 0:
        compteur = compteur + 1
print(compteur)

# Question 11:
#************
print("\n** Question 11:")

for a in range(1, 10):
    present = False
    for j in range(9):
        if C[3][j] == a:
            present = True
    if not present:
        print(a)

# Question 12:
#************
print("\n** Question 12:")

for a in range(1, 10):
    present = False
    for i in range(9):
        if C[i][4] == a:
            present = True
    if not present:
        print(a)

# Question 13:
#************
print("\n** Question 13:")

for i in range(3):
    for j in range(3):
        print(C[i][j])

# Question 14:
#************
print("\n** Question 14:")

for i in range(3, 6):
    for j in range(6,9):
        print(C[i][j])