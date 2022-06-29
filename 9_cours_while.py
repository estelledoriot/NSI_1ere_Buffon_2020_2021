#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * La boucle while
#**********************************

# Exercice 1
#***********
print("\n** Exercice 1:")

def truc(n):
    p = 1
    while p < n :
        p = p * 2
    print(n)
truc(100)

# Exemple
#********
print("\n** Exemple:")

def horloge():
    n = 1
    while n > 0:
        if n % 2 == 0:
            print("tic")
        else:
            print("tac")
        n += 1

#horloge()

# Exercice 3:
#************
print("\n** Exercice 3:")

def exemple(m, n):
    a = m
    b = m + n
    while a < b :
        a = a + 1
        b = b + 1

# Exercice 4:
#************
print("\n** Exercice 4:")

# fonction truc avec une boucle while
def truc2(n):
    x = 1
    k = 1
    while k < n:
        x = 2 * x
        k = k + 1
    print(x)
    
truc2(5)

# fonction truc2 avec une boucle for
def truc3(n):
    x = 1
    for k in range(1, n):
        x = 2 * x
    print(x)
    
truc3(5)

# Exercice: écrire un programme qui affiche tous les diviseurs d'un entier n en utilisant une boucle while
print("\n** Exemple:")

n = 36
k = 1
while k <= n:
    if n % k == 0:
        print(k)
    k = k + 1

# Exercice: écrire un programme qui affiche la somme de tous les diviseurs d'un entier n en utilisant une boucle while
print("\n** Exemple:")

n = 36
k = 1
somme = 0
while k <= n:
    if n % k == 0:
        somme = somme + k
    k = k + 1
print(somme)