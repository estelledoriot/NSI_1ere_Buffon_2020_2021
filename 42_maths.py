#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Math
#**********************************

from math import *
from random import *
from time import time
import matplotlib as mpl

####################
### Arithmétique ###
####################

# Exercice n°1
print("\n**Exercice n°1")

def entier_est_pair(n:int) -> bool:
    """
    teste si un nombre entier naturel est pair
    """
    return n % 2 == 0

assert entier_est_pair(2) == True, "/!\ entier_est_pair()"
assert entier_est_pair(3) == False, "/!\ entier_est_pair()"

# Exercice n°2
print("\n**Exercice n°2")

def entier_est_impair(n:int) -> bool:
    """
    teste si un nombre entier naturel est impair
    """
    return n % 2 == 1

assert entier_est_impair(2) == False, "/!\ entier_est_impair()"
assert entier_est_impair(3) == True, "/!\ entier_est_impair()"

# Exercice n°3
print("\n**Exercice n°3")

def donne_chiffres(n:int,p:int) -> int:
    """
    rend en paramètres un nombre entier ainsi qu’un entier qui déterminera une puissance de 10, et renvoie le chiffre qui correspond à la puissance de 10 demandée
    """
    return (n // (10**p)) % 10

assert donne_chiffres(4059, 3) == 4, "/!\ donne_chiffres()"
assert donne_chiffres(4059, 0) == 9, "/!\ donne_chiffres()"

# Exercice n°4
print("\n**Exercice n°4")

print("Question 1")

def diviseurs_naif(n:int) -> list:
    """
    prend en paramètre un entier n et renvoie l’ensemble de ses diviseurs sous forme de liste 
    """
    diviseurs = []
    for i in range(1, n+1):
        if n % i == 0:
            diviseurs.append(i)
    return diviseurs

assert diviseurs_naif(20) == [1, 2, 4, 5, 10, 20], "/!\ diviseurs_naif()"

print("Question 2")

def diviseurs_optimise(n:int) -> list:
    """
    prend en paramètre un entier n et renvoie l’ensemble de ses diviseurs sous forme de liste 
    """
    diviseurs = [1, n]
    i = 2
    while i * i < n:
        if n % i == 0:
            diviseurs.append(i)
            diviseurs.append(n // i)
        i += 1
    
    if i * i == n:
        diviseurs.append(i)
    return diviseurs

assert sorted(diviseurs_optimise(20)) == [1, 2, 4, 5, 10, 20], "/!\ diviseurs_optimise()"
 
# Exercice n°5
print("\n**Exercice n°5")

def entier_est_premier(n:int) -> bool:
    """
    teste si un nombre entier naturel est premier, c’est-à-dire s’il n’est divisible que par 1 et par lui-même
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

assert entier_est_premier(13) == True, "/!\ entier_est_premier()"
assert entier_est_premier(51) == False, "/!\ entier_est_premier()"

# Exercice n°6
print("\n**Exercice n°6")

print("Question 1")

def premiers(n:int) -> list:
    """
    prend en paramètre un entier n et renvoie la liste des 𝑛 premiers nombres premiers.
    """
    premiers = []
    i = 2
    while len(premiers) < n:
        if entier_est_premier(i):
            premiers.append(i)
        i += 1
    return premiers

assert premiers(6) == [2, 3, 5, 7, 11, 13], "/!\ premiers()"

print("Question 2")

def premiers_inf(n:int) -> list:
    """
    prend en paramètres un entier n et renvoie la liste de tous les nombres premiers inférieurs ou égaux à n
    """
    return [i for i in range(2, n+1) if entier_est_premier(i)]

assert premiers_inf(16) == [2, 3, 5, 7, 11, 13], "/!\ premiers_inf()"

# Exercice n°7
print("\n**Exercice n°7")

def liste_chiffres(n:int) -> list:
    """
    envoie dans une liste chacun des chiffres qui composent le nombre entier passé en paramètre
    """
    chiffres = []
    i = n
    while i > 0:
        chiffres.insert(0,i % 10)
        i = i // 10
    return chiffres

assert liste_chiffres(4059) == [4, 0, 5, 9], "/!\ liste_chiffres()"

# Exercice n°8
print("\n**Exercice n°8")

def erathostene(n:int) -> list:
    """
    prend pour unique paramètre un entier naturel n et renvoie la liste des nombres premiers inférieurs ou égaux à n en utilisant l’algorithme d’ÉRATHOSTÈNE.
    """
    eratho = [i for i in range(2, n+1)]
    i = 0
    while eratho[i] <= sqrt(n):
        j = i+1
        while j < len(eratho):
            if eratho[j] % eratho[i] == 0:
                eratho.pop(j)
            else:
                j += 1
        i += 1
    return eratho

assert erathostene(20) == [2, 3, 5, 7, 11, 13, 17, 19], "/!\ erathostene()"

# Exercice n°9
print("\n**Exercice n°9")

def est_parfait(n:int) -> bool:
    """
    teste si un entier passé en paramètre est parfait ou non
    un entier naturel est dit parfait lorsqu’il est égal à la somme de tous ses diviseurs propres autres que lui-même
    """
    somme_diviseurs = 0
    for i in range(1, n):
        if n % i == 0:
            somme_diviseurs += i
    return n == somme_diviseurs

assert est_parfait(28) == True, "/!\ est_parfait()" 
assert est_parfait(5) == False, "/!\ est_parfait()"

# Exercice n°10
print("\n**Exercice n°10")

def liste_parfaits(n:int) -> list:
    """
    prend en paramètre un entier 𝑛 et qui renvoie une liste de tous les nombres parfaits inférieurs ou égaux à n
    """
    return [i for i in range(n+1) if est_parfait(i)]

# Exercice n°11
print("\n**Exercice n°11")

def pgcd(m:int, n:int) -> int:
    """
    prend en paramètres deux entiers positifs m et n retourne leur PGCD.
    """
    if m < n:
        return pgcd(n, m)
    elif m % n == 0:
        return n
    else:
        return pgcd(n, m % n)

assert pgcd(1245, 123) == 3, "/!\ pgcd()"

# Exercice n°12
print("\n**Exercice n°12")

def est_palindrome(n:int) -> bool:
    """
    teste si un entier est un palindrome 
    """
    chiffres = liste_chiffres(n)
    n = len(chiffres)
    for i in range(n//2):
        if chiffres[i] != chiffres[n-1-i]:
            return False
    return True

assert est_palindrome(121) == True, "/!\ est_palindrome()" 
assert est_palindrome(123) == False, "/!\ est_palindrome()"

#################
### Equations ###
#################

# Exercice n°13
print("\n**Exercice n°13")

def f(x:int) -> int: 
    return x**2 + 1

def tableau_valeurs(xmin:int, xmax:int, n:int) -> tuple: 
    """
    xmin: la valeur minimale du paramètre x précédemment évoqué;
    xmax: la valeur maximale de ce même paramètre x;
    n: le nombre total de valeurs équiréparties entre xmin et xmax incluses (valeurs sur lesquelles la fonction f sera évaluée).
    La fonction renvoit deux listes, la 1re contenant les différentes valeurs de x, la 2nde contenant les valeurs correspondantes de f(x).
    """
    liste_x = []
    liste_y = []
    for i in range (n):
        try:
            x = xmin + (xmax - xmin) * i / (n-1)
            y = f(x)
            liste_x.append(x)
            liste_y.append(y)
        except ZeroDivisionError:
            continue
    return liste_x,liste_y

assert tableau_valeurs(1,2,2) == ([1,2],[2,5]), "/!\ tableau_valeurs()"

# Exercice n°14
print("\n**Exercice n°14")

def f(x): 
    return x**2 - 2

def balayage(a:int, b:int, n:int) -> tuple:
    """
    [a, b]: intervalle
    n: 10**-n est le pas de l'intervalle
    la fonction balaie l'intervalle [a,b] par pas constants 
    """
    x0 = a
    x1 = a + 10**-n
    while x1 <= b:
        if f(x0) * f(x1) < 0:
            return x0,x1
        x0, x1 = x1, x1 + 10**-n
    return x1,b

print("Question 1")

def balayage1(a:int, b:int, n:int) -> float:
    """
    [a, b]: intervalle
    n: 10**-n est le pas de l'intervalle
    elle renvoie la moyenne arithmétique des valeurs xn et xn + 10**-n telles que 𝛼 ∈ [𝑥𝑛 ; 𝑥𝑛 + 10−𝑛]
    """
    x,y = balayage(a,b,n)
    return (x + y) / 2

assert abs(balayage1(1,2,6) - 1.4142135623049998) < 10**-6, "/!\ balayage()"

print("Question 2")

def balayage2(a:int, b:int, n:int) -> float:
    """
    [a, b]: intervalle
    n: 10**-n est le pas de l'intervalle
    fonction optimisée
    elle renvoie la moyenne arithmétique des valeurs xn et xn + 10**-n telles que 𝛼 ∈ [𝑥𝑛 ; 𝑥𝑛 + 10−𝑛]
    """
    i = 0
    x,y = a,b
    while i <= n:
        x,y = balayage(x,y,i)
        i += 1
    return (x + y) / 2

assert abs(balayage2(1,2,10) - 1.4142135623049998) < 10**-10, "/!\ balayage()"

# Exercice n°15
print("\n**Exercice n°15")

def dichotomie(a:int, b:int, n:int) -> float:
    """
    [a, b]: intervalle
    n: 10**-n est le pas de l'intervalle
    méthode dichotomique
    elle renvoie la moyenne arithmétique des valeurs xn et xn + 10**-n telles que 𝛼 ∈ [𝑥𝑛 ; 𝑥𝑛 + 10−𝑛]
    """
    debut = a
    fin = b
    while (fin - debut) > 10**-n:
        milieu = (debut + fin)/2
        if f(debut) * f(milieu) < 0:
            fin = milieu
        else:
            debut = milieu
    return (debut+fin)/2

assert abs(dichotomie(1,2,6) - 1.4142136573791504) < 10**-6, "/!\ dichotomie()"

# Exercice n°16
print("\n**Exercice n°16")

print("Question 1")

def mystere1(x:float) -> tuple: 
    """
    retourne un encadrement de sqrt(x) à l'unité près
    """
    a = 0
    b = 1
    while b * b < x:
        a = b
        b = b + 1
    return a, b

print("Question 2")

def mystere2(x:float, e:float) -> tuple:
    """
    retourne un encadrement de sqrt(x) à e près
    avec une méthode dichotomique
    """
    a, b = mystere1(x) 
    while b - a > e:
        m = (a + b) / 2
        if m**2 == x:
            a = b = m
        elif m**2 > x: 
            b = m
        else: 
            a = m
    return a, b

# Exercice n°17
print("\n**Exercice n°17")

def df(x):
    return 2*x

def newton(a:float, n:int) -> float:
    """
    a: une valeur « proche » de la solution de l’équation f(x) = 0 
    n: entier
    la fonction renverra la valeur xn obtenue après n itérations
    """
    x = a
    for i in range(n):
        x = x - f(x)/df(x)
    return x
    
assert abs(newton(2,6) - 1.414213562373095) <10**-16, "/!\ newton()"

##############
### Suites ###
##############

# Exercice n°18
print("\n**Exercice n°18")

print("Question 1")

def collatz(n:int) -> bool:
    """
    prend en paramètre un entier n et retourne le booléen True si le processus s’achève (donc si on finit par atteindre la valeur 1)
    """
    a = n
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
    return True

assert collatz(49) == True, "/!\ collatz()"

print("Question 2")

def temps_vol_collatz(n:int) -> int:
    """
    prend en paramètre un entier n et retourne le nombre de fois où le processus est répété avant d’atteindre la valeur 1
    """
    a = n
    i = 0
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        i += 1
    return i

assert temps_vol_collatz(127) == 46, "/!\ temps_vol_collatz()"

print("Question 3")

def hauteur_vol_collatz(n:int) -> int:
    """
    retourne la valeur maximale atteinte lors du processus, avant d’atteindre la valeur 1
    """
    a = n
    maximum = n
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        if maximum < a:
            maximum = a
    return maximum

assert hauteur_vol_collatz(127) == 4372, "/!\ hauteur_vol_collatz()"

print("Question 4")

def vol_altitude_collatz(n:int) -> int:
    """
    retourne le « temps de vol en altitude » : c’est le plus petit numéro d’étape pour lequel le résultat intermédiaire est strictement inférieur à n
    """
    a = n
    i = 0
    while a >= n:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        i += 1
    return i-1

assert vol_altitude_collatz(127) == 23, "/!\ vol_altitude_collatz()"

print("Question 5")

def temps_vol_max_collatz(m:int, n:int) -> tuple:
    """
    prend en paramètres deux entiers m et n tels que m < n 
    renvoie un tuple (k ; temps_vol_collatz(k)), 
    où l’entier k ∈ [ m ; n [ est tel que son temps_vol_collatz(k) est le plus grand de l’ensemble des temps de vols de tous les entiers compris entre m inclus et n exclus 
    """
    k = m
    vol_k = temps_vol_collatz(m)
    for i in range(m+1, n):
        vol = temps_vol_collatz(i)
        if vol > vol_k:
            vol_k = vol
            k = i
    return k,vol_k

assert temps_vol_max_collatz(3, 100) == (97, 118), "/!\ temps_vol_max_collatz()"

# Exercice n°19
print("\n**Exercice n°19")

def zenon(n:int) -> float:
    """
    prend en paramètre un entier n et renvoie la valeur du terme dn, avec:
    dn+1 = dn + 4/2**n et d1 = 4
    """
    d = 4
    for i in range(1,n):
        d = d + 4/2**i
    return d

assert abs(zenon(20) - 7.999992370605469) <= 10**-10, "/!\ zenon()"

print([zenon(n) for n in range(1,101)])

# Exercice 20
print("\n**Exercice n°20")

def heron(a:int, n:int) -> float:
    """
    a: entier
    n: entier
    renvoie une approximation de sqrt(a) correspondant au n-ème terme de la suite de Héron définie par:
    xn+1 = (xn + a/xn) /2
    """
    x = 1
    for i in range(n):
        x = (x + a/x) /2
    return x

assert abs(heron(2,4) - 1.4142135623746899) <= 10**-10, "/!\ heron()"

# Exercice 21
print("\n**Exercice n°21")

def pi_14_17(n:int) -> float:
    """
    renvoie la valeur approchée de pi corresondant au n-ème terme de la suite:
    p0 = 0 et pn+1 = pn + 4 * (-1)**n / (2n+1)
    """
    p = 0
    for i in range(n):
        p = p + 4 * (-1)**i / (2 * i + 1)
    return p

assert abs(pi_14_17(100000) - 3.1415826535897198) <= 10**-10 , "/!\ pi_14_17()"

# Exercice 22
print("\n**Exercice n°22")

def pi_16(n:int) -> float:
    """
    renvoie la valeur approchée de pi corresondant au n-ème terme de la suite:
    p0 = 2 et pn+1 = 2 pn / un+1
    où un+1 = sqrt(2+un) et u0 = 0
    """
    u = 0
    p = 2
    for i in range(n):
        u = sqrt(2 + u)
        p = 2 * p / u
    return p

assert abs(pi_16(20) - 3.1415926535850938) <= 10**-10, "/!\ pi_16()"

# Exercice 23
print("\n**Exercice n°23")

def pi_18(n:int) -> float:
    """
    renvoie la valeur approchée de pi corresondant au n-ème terme de la suite:
    p0 = 2 et pn+1 = pn + 2 * un+1
    où un+1 = un * (n+1)/(2n+3) et u1 = 1/3
    """
    i = 0
    p = 2
    u = 1/3
    while i < n:
        p = p + 2 * u
        i += 1
        u = u * (i + 1) / (2 * i + 3)
    return p

assert abs(pi_18(20) - 3.1415922987403384) <= 10**-10, "/!\ pi_18()"

# Exercice 24
print("\n**Exercice n°24")

def montecarlo_pi(n:int) -> float:
    """
    calcul de pi selon la méthode de monte-carlo
    """
    cpt = 0
    for i in range(n):
        x = random()
        y = random()
        if x * x + y * y <= 1:
            cpt += 1
    return 4 * cpt / n

print(montecarlo_pi(1000000))

# Exercice 25
print("\n**Exercice n°25")

# test pi_14_17
n = 1
while (abs(pi_14_17(n) - pi) >= 10**-5):
    n *= 10
t0 = time()
pi_14_17(n)
print("Durée d'exécution pi_14_17", time()-t0)

# test pi_16
n = 1
while (abs(pi_16(n) - pi) >= 10**-5):
    n *= 10
t0 = time()
pi_16(n)
print("Durée d'exécution pi_16", time()-t0)

# test pi_18
n = 1
while (abs(pi_18(n) - pi) >= 10**-5):
    n *= 10
t0 = time()
pi_18(n)
print("Durée d'exécution pi_18", time()-t0)

# test montecarlo_pi
'''
n = 1
while (abs(montecarlo_pi(n) - pi) >= 10**-3):
    n *= 10
t0 = time()
montecarlo_pi(n)
print("Durée d'exécution montecarlo_pi", time()-t0)
'''

# Exercice 26
print("\n**Exercice n°26")

print("Question 1")

def fibonacci(n:int) -> int:
    """
    renvoie le n-ème terme de la suite de Fibonacci
    Fn = Fn-1 + Fn-2 et F0 = F1 = 1
    """
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return b

assert fibonacci(15) == 987, "/!\ fibonacci()"

print("Question 2")

def liste_fibo(n:int) -> list:
    """
    liste des n+1 premiers termes de la suite de Fibonacci
    """
    fibo = [1,1]
    while len(fibo) <= n:
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

assert liste_fibo(4) == [1, 1, 2, 3, 5], "/!\ liste_fibo()"
    
# Exercice 27
print("\n**Exercice n°27")

print("Question 1")

def nbdor1(n:int) -> float:
    """
    approximation du nombre d'or par la suite:
    an+1 = 1 + 1/an et a0 = 2
    """
    a = 2
    for i in range(n):
        a = 1 + 1 / a
    return a

assert abs(nbdor1(8) - 1.6181818181818182) <= 10**-10, "/!\ nbdor1()"

print("Question 2")

def nbdor2(n:int) -> float:
    """
    approximation du nombre d'or par la suite:
    bn+1 = sqrt(1 + bn) et b0 = 2
    """
    b = 2
    for i in range(n):
        b = sqrt(1 + b)
    return b

assert abs(nbdor2(8) - 1.618064196086926) <= 10**-10, "/!\ nbdor2()"

print("Question 3")

def nbdor3(n:int) -> float:
    """
    approximation du nombre d'or par la suite:
    cn+1 = (cn**2 + 1)/(2cn - 1) et c0 = 2
    """
    c = 2
    for i in range(n):
        c = (c**2 + 1)/(2 * c - 1)
    return c

assert abs(nbdor3(4) - 1.618033988749989) <= 10**-10, "/!\ nbdor3()"

print("Question 4")

def nbdor4(n:int) -> float:
    """
    approximation du nombre d'or par la suite:
    Fn/Fn-1 
    """
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return b / a

assert abs(nbdor4(7) - 1.6153846153846154) <= 10**-10, "/!\ nbdor4()"

print("Question 5")

phi = (1 + sqrt(5)) / 2

# test nbdor1
n = 1
while (abs(nbdor1(n) - phi) >= 10**-5):
    n += 1
t0 = time()
nbdor1(n)
print("Durée d'exécution nbdor1", time()-t0)

# test nbdor2
n = 1
while (abs(nbdor2(n) - phi) >= 10**-5):
    n += 1
t0 = time()
nbdor2(n)
print("Durée d'exécution nbdor2", time()-t0)

# test nbdor3
n = 1
while (abs(nbdor3(n) - phi) >= 10**-5):
    n += 1
t0 = time()
nbdor3(n)
print("Durée d'exécution nbdor3", time()-t0)

# test nbdor4
n = 1
while (abs(nbdor4(n) - phi) >= 10**-5):
    n += 1
t0 = time()
nbdor4(n)
print("Durée d'exécution nbdor4", time()-t0)

# Exercice 28
print("\n**Exercice n°28")

print("Question 2")

def brouncker(n:int) -> float:
    assert n > 0, "n doit être > 0" 
    u = 0
    for k in range(1, n+1):
        u = u + 1/((2 * k - 1) * (2 * k))
    return u

assert abs(brouncker(100) - log(2)) <= 10**-2, "/!\ brouncker()"

print("Question 3")

def lst_va_ln2(p:int) -> list:
    """
    prend en paramètre un entier p et renvoie sous forme de liste les termes de la suite (un) tels que ln(2) - un > 10**-p
    """
    l = [0]
    while abs(l[-1] - log(2)) > 10**-p:
        k = len(l)
        l.append(l[-1] + 1/((2 * k - 1) * (2 * k)))
    return l

print(lst_va_ln2(3))

# Exercice 29
print("\n**Exercice n°29")

print("Question 1")

def e1(n:int) -> float:
    """
    renvoie le terme de rang n de la suite un = (1 + 1/n)**n
    """
    return (1 + 1/n)**n

assert abs(e1(100000) - 2.7182682371922975) <= 10**-10, "/!\ e1()"

print("Question 2")

def e2(n:int) -> float:
    """
    renvoie le terme de rang n de la suite bn définie par:
    bn+1 = bn + 1/an+1 et b0 = 1
    avec an+1 = (n+1) an et a0 = 1
    """
    a = 1
    b = 1
    for i in range(1, n+1):
        a = i * a
        b = b + 1 / a
    return b

assert abs(e2(7) - 2.7182539682539684) <= 10**-10, "/!\ e2()"

# Exercice 30
print("\n**Exercice n°30")

def binom(n:int, k:int) -> int:
    """
    renvoie le coefficient binomial k parmi n en utilisant la formule de Pascal
    """
    if k == 0 or k == n:
        return 1
    
    j = 1 # numero de la ligne en cours
    ligne = [1,1] # ligne courante
    ligne_suivante = [1] # ligne suivante à construire
    while j <= n:
        i = 1 # numero de la case à remplir
        while i <= k and i <= j: # on arrête de remplir la ligne suivante lorsqu'on arrive au bout (i = j) ou lorsqu'on arrive à k
            if i == j:
                ligne_suivante.append(1) 
            else:
                ligne_suivante.append(ligne[i-1]+ligne[i])
            i += 1
        ligne = ligne_suivante
        ligne_suivante = [1]
        j += 1
    return ligne[k]

assert binom(1,1) == 1, "/!\ binom()"
assert binom(2,1) == 2, "/!\ binom()"
assert binom(5,3) == 10, "/!\ binom()"
assert binom(8,4) == 70, "/!\ binom()"

# Exercice 31
print("\n**Exercice n°31")

def galton(p:int, n:int) -> list:
    """
    modélisation d'une planche de galton avec:
    - n: le nombre de billes
    - p: le nombre de niveaux
    la fonction renvoie la liste de la répartition des billes à l'issue de l'expérience
    """
    current = [n] # liste qui contient les billes à l'étape en cours. Initialement, toutes les billes vont heurter le seul clou de l'étape 0
    for i in range(1,p+1): # i est l'indice de l'étape
        next = [0]*(i+1) # liste contenant la répartition des billes à l'étape suivante
        for j in range(len(current)): # parcourt de la liste current
            for k in range(current[j]): # pour chaque bille, on détermine sa position à l'étape suivante
                p = randint(0,1)
                if p == 0:
                    next[j] = next[j] + 1
                else:
                    next[j+1] = next[j+1] + 1
        current = next
    return current

print(galton(0,10))
print(galton(1,10))
print(galton(2,50))
print(galton(5,10000))

# Exercice 32
print("\n**Exercice n°32")

def loi_geom(p:float, n:int) -> tuple:
    """

    """
    resultats = {}
    for i in range(n): # on répète l'expérience n fois
        cpt = 0
        while random() > p:
            cpt += 1
        if not resultats.get(cpt):
            resultats[cpt] = 1
        else:
            resultats[cpt] += 1
    # recherche de la plus grande répétition
    maxi = 0
    for key in resultats.keys():
        if key > maxi:
            maxi = key
    # création des deux listes de résultat
    ks = [i for i in range(maxi+1)]
    fs = []
    for i in ks:
        r = resultats.get(i)
        if r:
            fs.append(r/n)
        else:
            fs.append(0)
    return ks,fs

print(loi_geom(0.5,1000))

