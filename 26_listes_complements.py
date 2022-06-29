#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD: complément sur les listes
#**********************************

from random import randint
from math import sqrt
import pygame

# Exercice n°1
#*************
print("\n** Exercice n°1:")

lst = [2*n+1 for n in range(5)]
print(lst)
lst = [n for n in range(10) if n % 3 == 1]
print(lst)
lst = [n for n in range(1, 12) if 12 % n == 0]
print(lst)
lst = [(n, n ** 2) for n in range(5)]
print(lst)

# Exercice n°2
#*************
print("\n** Exercice n°2:")

def notes_au_hasard(nb):
    return [randint(0, 20) for i in range(nb)]

print("Notes au hasard:", notes_au_hasard(5))

# Exercice n°3
#*************
print("\n** Exercice n°3:")

alphabet = [chr(i + ord('A')) for i in range(26)]
print("Alphabet:", alphabet)

# Exercice n°4
#*************
print("\n** Exercice n°4:")

lst = []
for idx in range(5):
    lst = lst + [idx] * idx
print(lst)

# Exercice n°5
#*************
print("\n** Exercice n°5:")

def carre(lst):
    return [el ** 2 for el in lst]

print("Carrés des 5 premiers entiers:", carre([1,2,3,4,5]))

# Exercice n°6
#*************
print("\n** Exercice n°6:")

def echange(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

l = [5,1,8,2,3,4]
echange(l,0,3)
print("Liste après échange:", l)

# Exercice n°7
#*************
print("\n** Exercice n°7:")

def croissante(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True

print("[1,2,3,4,5] est croissante:", croissante([1,2,3,4,5]))
print("[1,6,3,4] est croissante:", croissante([1,6,3,4]))

# Exercice n°8
#*************
print("\n** Exercice n°8:")

def nombres_premiers(n):
    l = []
    i = 2
    while len(l) < n:
        premier = True
        for e in l:
            if i % e == 0:
                premier = False
                break
        if premier:
            l.append(i)
        i += 1
    return l

print("Nombres premiers inférieurs à 20:", nombres_premiers(20))

# Exercice n°9
#*************
print("\n** Exercice n°9:")

def truc1(lst):
    lst2 = []
    for el in lst :
        if el % 2 == 0 :
            lst2.append(el)
    return lst2

print("Eléments pairs de la liste [12, 5, 14, 17]:", truc1([12, 5, 14, 17]))

def truc2(lst):
    idx = 0
    while idx < len(lst):
        el = lst[idx]
        if el % 2 != 0 :
            lst.remove(el)
        else :
            idx = idx + 1

lst = [12, 5, 14, 17]
truc2(lst)
print("Eléments pairs de la liste [12, 5, 14, 17]:", lst)

# Exercice n°10
#**************
print("\n** Exercice n°10:")

def bonnes_notes(notes):
    l = []
    for e in notes:
        if e >= 10:
            l.append(e)
    return l

print("Notes supérieures à 10:", bonnes_notes([16,8,12,6,15]))

def supprime_mauvaises_notes(notes):
    i = 0
    while i < len(notes):
        if notes[i] < 10:
            notes.pop(i)
        else:
            i += 1

notes = [16,8,12,6,15]
supprime_mauvaises_notes(notes)
print("Notes supérieures à 10:", notes)

# Exercice n°11
#**************
print("\n** Exercice n°11:")

def miroir(lst):
    n = len(lst)
    for i in range(n // 2):
        echange(lst, i, n - 1 - i)

lst = [1,2,3,4,5,6]
miroir(lst)
print("Liste miroir:", lst)

def miroir2(lst):
    n = len(lst)
    l = []
    for i in range(n):
        l.append(lst[n-1-i])
    return l

print("Liste miroir:", miroir2([1,2,3,4,5,6]))

# Exercice n°12
#**************
print("\n** Exercice n°12:")

def moyenne_ponderee(notes, coeffs):
    total = 0
    somme_coeffs = 0
    for i in range(len(notes)):
        total += notes[i] * coeffs[i]
    for i in range(len(coeffs)):
        somme_coeffs += coeffs[i]
    return total/somme_coeffs

print("Moyenne pondérée:", moyenne_ponderee([15,16,14,12],[2,1,2,0.5]))

# Exercice n°13
#**************
print("\n** Exercice n°13:")

def inserer(lst, el, idx):
    l = [0]*(len(lst)+1)
    for i in range(idx):
        l[i] = lst[i]
    l[idx] = el
    for i in range(idx + 1,len(lst) + 1):
        l[i] = lst[i-1]
    return l

print("Insérer 8 en position 2:", inserer([1,2,3,4,5],8,2))

# Exercice n°14
#**************
print("\n** Exercice n°14:")

def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def plus_proche_voisin(liste, p):
    ppv = liste[0]
    for e in liste:
        if distance(e, p) < distance(ppv, p):
            ppv = e
    return ppv

print("Plus proche voisin de (2,0):", plus_proche_voisin([(0,0),(1,1),(4,5),(3,7),(5,1)],(2,0)))

# Exercice n°15
#**************
print("\n** Exercice n°15:")

couleurs = ('♠','♥','♦','♣')
valeurs = (7,8,9,10,'V','D','R','A')

def creer_jeu(couleurs, valeurs):
    l = []
    for e1 in couleurs:
        for e2 in valeurs:
            l.append((e1, e2))
    return l

jeu = creer_jeu(couleurs, valeurs)
print("Jeu:", jeu)

def carte_hasard(jeu):
    n = len(jeu)
    return jeu[randint(0,n-1)]

print("Carte au hasard:", carte_hasard(jeu))

def main(nb_cartes,jeu):
    l = []
    for i in range(nb_cartes):
        n = len(jeu)
        carte = jeu[randint(0, n-1)]
        l.append(carte)
        jeu.remove(carte)
    return l

print("Créer une main:", main(5,jeu))

def melange(jeu):
    return main(len(jeu),jeu)

jeu = creer_jeu(couleurs,valeurs)
jeu_melange = melange(jeu)
print("Jeu mélangé:", jeu_melange)

# Exercice n°16
#**************
print("\n** Exercice n°16:")

def doublons(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

print("Doublons dans [1,2,3,4,5,6]:", doublons([1,2,3,4,5,6]))
print("Doublons dans [1,4,5,2,1,6,3,4]:", doublons([1,4,5,2,1,6,3,4]))

def suppr_doublons(lst):
    l = []
    for e in lst:
        if e not in l:
            l.append(e)
    return l

print("Suppression des doublons:", suppr_doublons([1,4,5,2,1,6,3,4]))

# Exercice n°17
#**************
print("\n** Exercice n°17:")

def simulations(n):
    l = [0] * 6
    for i in range(n):
        l[randint(0, 5)] += 1
    return l

def frequences(lst, n):
    return [e/n for e in lst]

def histogramme(fenetre, freq):
    grey = (128, 128, 128)
    font = pygame.font.Font(None, 16)
    for i in range(6):
        r = pygame.Rect(30 + 100 * i, 350 - 300 * freq[i], 40, 300 * freq[i])
        pygame.draw.rect(fenetre, grey, r)
        no = font.render(str(i + 1), 1, grey)
        rec = no.get_rect(center = (50 + 100 * i, 375))
        fenetre.blit(no, rec)

def programme(n):
    pygame.init()

    size = (600, 400)
    window = pygame.display.set_mode(size)

    white = (255, 255, 255)
    window.fill(white)

    histogramme(window, frequences(simulations(n), n))
    pygame.display.update()

    lock = True
    while lock:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                lock = False
    pygame.quit()

programme(1000)

