#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Exercices sur les diviseurs
#**********************************

from math import *

# Exercice 2 - 1)
#****************
print("\n** Exercice 2: 1)")

def diviseurs(n):
    for i in range(1, n+1): # on parcourt tous les entiers de 1 a n pour trouver les diviseurs de n
        if n % i == 0: # si i divise n
            print(i) # alors on affiche i

print("Les diviseurs de 23494 sont :")
diviseurs(23494)

# Exercice 2 - 2)
#****************
print("\n** Exercice 2: 2)")

def nb_diviseurs(n):
    a = 0 # on definit un compteur a
    for i in range(1, n+1):
        if n % i == 0: # si i divise n
            a = a + 1 # on incremente le compteur
    return a

print("12**6 a", nb_diviseurs(12**6), "diviseurs")

# Exercice 2 - 3)
#****************
print("\n** Exercice 2: 3)")

def q2_3():
    a = 1 # nombre qui a le plus grand nombre de diviseurs
    b = 1 # plus grand nombre de diviseurs
    for i in range(1, 1001):
        if nb_diviseurs(i) > b: # si le nombre de diviseurs de i est plus grand que b
            b = nb_diviseurs(i) # on remplace b par le nombre de diviseurs de i
            a = i # on remplace a par i
    return a

print("Le nombre entre 1 et 1000 qui a le plus de diviseurs est:", q2_3())

# Exercice 3 - 1)a)
#******************
print("\n** Exercice 3: 1)a)")

def est_premier(n):
    if n == 1:
        return False # 1 n'est pas premier
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0: # si n admet un diviseur autre que 1 et lui-même il n'est pas premier
            return False
    return True # sinon il est premier

if est_premier(2**(2**3)+1):
    print("2**(2**3)+1 est premier")
else:
    print("2**(2**3)+1 n'est pas premier")

# Exercice 3 - 1)b)
#******************
print("\n** Exercice 3: 1)b)")

def test_Fermat():
    n = 0
    while est_premier(2**(2**n)+1): # tant que le nombre de Fermat est premier
        n = n + 1 # on calcule le nombre de Fermat suivant
    return n

print("Le premier nombre de Fermat qui n'est pas premier est: F", test_Fermat())

# Exercice 3 - 2)
#****************
print("\n** Exercice 3: 2)")

def test_Mersenne():
    n = 2
    while not est_premier(n) or est_premier(2**n-1):
        n = n + 1
    return n

print("Le premier nombre de Mersenne qui n'est pas premier est le n°", test_Mersenne())

# Exercice 3 -3)
#***************
print("\n** Exercice 3: 3)")

def nb_premiers(n):
    nb = 0 # nb est un compteur qui compte le nombre de nombres premiers
    i = 2
    while i <= n: # tant que i est plus petit que n
        if est_premier(i): # si i est premier
            nb = nb + 1 # on incremente le compteur
        i = i + 1
    return nb

print("Il y a", nb_premiers(1000), "nmobres premiers inférieurs à 1000")

# Exercice 4 - 1)
#****************
print("\n** Exercice 4: 1)")

def somme_diviseurs(n):
    somme = 0 # somme va contenir la somme des diviseurs
    for i in range(1, n + 1):
        if n % i == 0: # si i est un diviseur de n
            somme = somme + i # on ajoute i a la somme des diviseurs
    return somme

print("La somme des diviseurs de 2020 est:", somme_diviseurs(2020))

# Exercice 4 - 2)
#****************
print("\n** Exercice 4: 2)")

def q4_2():
    nb = 1 # contient la plus grande somme de diviseurs
    maxi = 1 # contient le nombre qui a la plus grande somme de diviseurs
    for i in range(1, 1001):
        r = somme_diviseurs(i)
        if r > nb: # si la somme des diviseurs de i est plus grande que nb
            nb = r # on remplace nb par la somme des diviseurs de i
            maxi = i # on remplace maxi par i
    return maxi

print("Le nombre entre 1 et 1000 dont la somme des diviseurs est la plus grande est:", q4_2())

# Exercice 5 - 1)
#****************
print("\n** Exercice 5: 1)")

def parfait(n):
    return(somme_diviseurs(n) == 2 * n)

if parfait(28):
    print("Le nombre 28 est parfait")
else:
    print("Le nombre 28 n'est pas parfait")

# Exercice 5 - 2)
#****************
print("\n** Exercice 5: 2)")

def q5_2():
    for i in range(1, 10001):
        if parfait(i):
            print(i)

print("Les nombres parfaits entre 1 et 10000 sont:")
q5_2()

# Exercice 6 - 1) a)
#*******************
print("\n** Exercice 6: 1) a)")
def syracuse(n):
    a = n
    i = 0
    while  a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = a * 3 + 1
        i += 1
    return(i)

print("Le temps de vol de 2020 est égal à", syracuse(2020))

# Exercice 6 - 1) b)
#*******************
print("\n** Exercice 6: 1) b)")

def q6():
    a = 1
    t = 0
    for i in range(1, 1001):
        r = syracuse(i)
        if r > t:
            t = r
            a = i
    return(a)

print("Parmi les nombres entre 1 et 1000, celui qui a le temps de vol le plus long est:", q6())

# Exercice 6 - 2) a)
#******************
print("\n** Exercice 6: 2)a)")

def altitude(n):
    a = n
    i = n
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = a * 3 + 1
        if a > i:
            i = a
    return(i)

print("L'altitude maximale de 255 est:", altitude(255))

# Exercice 6 - 2) b)
#*******************
print("\n**Exercice 6: 2)b)")

def q6b():
    a = 0
    j = 1
    for i in range(1, 1001):
        r = altitude(i)
        if r > a:
            a = r
            j = i
    return j

print("Parmi les nombres entre 1 et 1000, celui a l'altitude la plus grande est", q6b())

# Exercice 7 - 1)
#****************
print("\n** Exercice 7: 1)")

def fibo(n):
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a+b
    return a

print("F12 =", fibo(12))

# Exercice 7 - 2)
#****************
print("\n** Exercice 7: 2)")

def q7():
    a = fibo(100)
    i = 0
    while a >= 1:
        a = a / 10
        i += 1
    return i

print("F100 est composé de", q7(), "chiffres")

# Exercice 7 - 3)
#****************
print("\n** Exercice 7: 3)")

def q7b():
    a = 1
    b = 1
    for i in range(1, 100):
        a, b = b, a + b
        if est_premier(a):
            print("F_"+str(i)+"="+str(a))

print("Les nombres de Fibonacci premiers sont:")
q7b()

# Exercice 7 - 4) a)
#*******************
print("\n** Exercice 7: 4)a)")

def quotient(n):
    a = 1
    b = 1
    q = 1
    for i in range(n - 1):
        a, b = b, a + b
        q = b / a
    return q

print("La suite converge vers:", quotient(1000))