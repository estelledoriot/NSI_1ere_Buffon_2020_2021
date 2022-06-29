#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD dictionnaire
#**********************************

# Exercice 1

# Question 2
def split(texte,sep):
    '''
    Fonction split qui découpe des chaines de caractères au niveau du séparateur sep
    '''
    resultat = []
    r = ""
    for lettre in texte:
        if lettre == sep:
            resultat.append(r)
            r = ""
        else:
            r += lettre
    if r != "":
        resultat.append(r)
    return resultat

def create_dataset(nom_fichier):
    '''
    Fonction create_dataset qui prend en entrée un nom de fichier, et qui renvoie une liste de dictionnaires
    (chaque dictionnaire contient les informations relatives à une rue de Paris)
    '''
    fichier = open(nom_fichier, "r")
    texte = fichier.read()
    fichier.close()
    donnees = split(texte,"\n")
    descripteurs = split(donnees[0],";")
    resultat = []
    for i in range(1,len(donnees)):
        r = split(donnees[i],";")
        dico = {}
        for j in range(len(r)):
            dico[descripteurs[j]] = r[j]
        resultat.append(dico)
    return resultat

# la variable rue contient les données découpées provenant du fichier "noms_voies_paris.csv"
rues = create_dataset("noms_voies_paris.csv")

# Question 3 a)
print("\n** Question 3a):")
def q3a():
    for el in rues:
        if el['Libellé'] == 'boulevard Pasteur':
            return el['Longueur']

print("La longueur du boulevard Pasteur est:", q3a())

# Question 3 b)
print("\n** Question 3b):")
def q3b():
    lmax = 0
    ruemax = ''
    for el in rues:
        if el['Longueur'] != '' and float(el['Longueur']) > lmax:
            lmax = float(el['Longueur'])
            ruemax = el['Libellé']
    return ruemax,lmax

r = q3b()
print("La plus longue rue de Paris est:",r[0], " et sa longueur est:", r[1])

# Question 3 c)
print("\n** Question 3c):")
def q3c():
    cpt = 0
    for el in rues:
        if 'XVe' in el['Arrondissement']:
            cpt += 1
    return cpt

print("Dans le XVe, il y a: ",q3c(), " rues")

# Question 3 d)
print("\n** Question 3d):")
def q3d():
    quartiers = {}
    for el in rues:
        if not quartiers.get(el['Quartier']):
            quartiers[el['Quartier']] = 1
        else:
            quartiers[el['Quartier']] += 1
    maxi = 0
    quart = ''
    for key,value in quartiers.items():
        if value > maxi:
            maxi = value
            quart = key
    return quart

print("Le quartier qui a le plus de rues est:", q3d())

