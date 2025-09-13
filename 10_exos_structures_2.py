# **********************************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Exercices sur les structures de contrôle 2
# **********************************************

# Exercice 1
# ***********
print("\n** Exercice 1:")

a = 9
b = 17
c = 5
if a <= b and a <= c:
    print("Le minimum est:", a)
elif b <= a and b <= c:
    print("Le minimum est:", b)
else:
    print("Le minimum est:", c)

# Exercice 2
# ***********
print("\n** Exercice 2:")


def prix_cinema(age, troisD):
    prix_enfant = 5.60
    prix_reduit = 7.80
    prix_plein = 13.00
    sup_3D = 2.00
    prix = 0
    if age < 14:
        prix = prix_enfant
    elif age < 26:
        prix = prix_reduit
    elif age > 65:
        prix = prix_reduit
    else:
        prix = prix_plein
    if troisD:
        prix = prix + sup_3D
    print("Il faut payer", prix)


prix_cinema(25, True)

# Exercice 3
# ***********
print("\n** Exercice 3:")

n = 30
produit = 1

for i in range(1, n + 1):
    if i % 2 == 0:
        produit = produit * i

print("Le produit des nombres impairs inférieurs à 30 est:", produit)

# Exercice 4
# ***********
print("\n** Exercice 4:")

n = 40000
nb_malades = 1
nb_nouveaux_malades = 0
nb_jours = 1
while nb_malades < n:
    nb_nouveaux_malades = nb_malades * 2
    nb_malades = nb_malades + nb_nouveaux_malades
    nb_jours = nb_jours + 1

print("Au bout de", nb_jours, "jours, tout le monde est malade")

# Exercice 5
# ***********
print("\n** Exercice 5:")

n = 10
couples_lapins_adultes = 0
couples_lapins_enfants = 1
for i in range(n):
    nouveaux_lapins = couples_lapins_adultes
    couples_lapins_adultes = couples_lapins_adultes + couples_lapins_enfants
    couples_lapins_enfants = nouveaux_lapins

print(
    "Au bout de 10 générations, il y a",
    couples_lapins_adultes + couples_lapins_enfants,
    "lapins",
)

# Exercice 6 - 1)
# ****************
print("\n** Exercice 6: 1)")


def jubilaire(annee):
    nb_jours = 0
    for i in range(1900, annee):
        if i == 1900:
            nb_jours += 365
        elif i % 4 == 0:
            nb_jours += 366
        else:
            nb_jours += 365
    if annee != 1900 and annee % 4 == 0:
        nb_jours += 206
    else:
        nb_jours += 205
    reste = nb_jours % 7
    return reste == 6


def prochaine_jubilaire():
    annee = 2020
    arret = False
    while not arret:
        arret = jubilaire(annee)
        if arret:
            print("La prochaine année jubilaire est:", annee)
        annee = annee + 1


prochaine_jubilaire()

# Exercice 6 - 2)
# ****************
print("\n** Exercice 6: 2)")


def jubilaires_21e():
    annee = 2000
    while annee <= 2100:
        if jubilaire(annee):
            print(annee)
        annee = annee + 1


print("Les années jubilaires du XXIe siècle sont:")
jubilaires_21e()

# Exercice 7 - 1)
# ****************
print("\n** Exercice 7: 1)")


def infernale(annee):
    mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    compteur = 0
    nb_jours = 0
    for i in range(1900, annee):
        if i == 1900:
            nb_jours += 365
        elif i % 4 == 0:
            nb_jours += 366
        else:
            nb_jours += 365
    for i in range(12):
        if annee != 1900 and annee % 4 == 0 and i == 2:
            nb_jours += mois[i] + 1
        else:
            nb_jours += mois[i]
        reste = (nb_jours + 12) % 7
        if reste == 4:
            compteur = compteur + 1
    return compteur == 3


def infernales_21e():
    annee = 2000
    while annee <= 2100:
        if infernale(annee):
            print(annee)
        annee = annee + 1


print("Les années infernales du XXIe siècle sont:")
infernales_21e()

# Exercice 7 - 2)
# ****************
print("\n** Exercice 7: 2)")


def infernale_jubilaire():
    annee = 2020
    inf = False
    jub = False
    while not (inf and jub):
        annee = annee + 1
        inf = infernale(annee)
        jub = jubilaire(annee)
    print(annee)


infernale_jubilaire()
