#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD : données en tables
#**********************************

def split(texte,sep):
    resultat = []
    r = ""
    for lettre in texte:
        if lettre == sep:
            resultat.append(r)
            r = ""
        else:
            r += lettre
    if sep == '\n' and r == '':
        pass
    else:
        resultat.append(r)
    return resultat

def create_dataset(nom_fichier):
    fichier = open(nom_fichier, "r")
    texte = fichier.read()
    fichier.close()
    donnees = split(texte,"\n")
    resultat = []
    for ligne in donnees:
        resultat.append(split(ligne,","))
    return resultat

base = create_dataset("indicateurs.csv")

print("\nNombre de lignes:", len(base))
print("\nIndicateurs:")
print(base[0])
print("\n")
print(base[5459])
print(base[9365])
print(base[9390])

# Question 1
def q1(indicateurs):
    for ligne in indicateurs:
        lycee = ligne[0]
        annee = ligne[1]
        tauxS = ligne[7]
        if lycee == 'LYCEE BUFFON' and annee == '2018':
            return tauxS

print("\nTaux de réussite en S à Buffon en 2018:", q1(base))

# Question 2 a)
def q2a(indicateurs):
    cpt = 0
    for ligne in indicateurs:
        annee = ligne[1]
        tauxS = ligne[7]
        if annee == '2017' and tauxS == '100':
            cpt += 1
    return cpt

print("\nNombre de lycées ayant eu 100% de réussite en S en 2017:", q2a(base))

# Question 2 b)
def q2b(indicateurs):
    cpt = 0
    for ligne in indicateurs:
        annee = ligne[1]
        tauxS = ligne[7]
        pupr = ligne[4]
        if annee == '2017' and tauxS == '100' and pupr == 'PU':
            cpt += 1
    return cpt

print("\nNombre de lycées publics ayant eu 100% de réussite en S en 2017:", q2b(base))

# Question 3
def q3(indicateurs):
    cpt = 0
    for ligne in indicateurs:
        annee = ligne[1]
        tauxL = ligne[5]
        ac = ligne[3]
        if annee == '2016' and tauxL == '100' and ac == 'PARIS':
            cpt += 1
    return cpt

print("\nLycées ayant eu 100% de réussite en L en 2016:", q3(base))

# Question 4
def est_100(taux):
    return taux == '100' or taux == ''

def q4(indicateurs):
    resultat = []
    for ligne in indicateurs:
        lycee = ligne[0]
        annee = ligne[1]
        tauxL = ligne[5]
        tauxES = ligne[6]
        tauxS = ligne[7]
        ac = ligne[3]
        pupr = ligne[4]
        if annee == '2018' and ac == 'PARIS' and pupr == 'PU' and est_100(tauxL) and est_100(tauxES) and est_100(tauxS):
            resultat.append(lycee)
    return resultat

print("\nLycée ayant eu 100% de réussite au bac dans toutes les filières:", q4(base))

# Question 5
def plus_value_L(ligne):
    if ligne[5] == '' or ligne[8] == '':
        return None
    else:
        return int(ligne[5]) - int(ligne[8])

def plus_value_ES(ligne):
    if ligne[6] == '' or ligne[9] == '':
        return None
    else:
        return int(ligne[6]) - int(ligne[9])

def plus_value_S(ligne):
    if ligne[7] == '' or ligne[10] == '':
        return None
    else:
        return int(ligne[7]) - int(ligne[10])

def maximum(a,b):
    if a == None:
        return b
    if b == None:
        return a
    return max(a,b)

def plus_value_max(ligne):
    pvs = plus_value_S(ligne)
    pvl = plus_value_L(ligne)
    pves = plus_value_ES(ligne)
    return maximum(maximum(pvs,pvl),pves)

#  a)
def q5a(indicateurs):
    lyceemax = ''
    plusvaluemax = 0
    for ligne in indicateurs:
        lycee = ligne[0]
        annee = ligne[1]
        ac = ligne[3]
        if annee == '2012':
            plusvalue = plus_value_ES(ligne)
            if plusvalue != None and plusvalue > plusvaluemax:
                plusvaluemax = plusvalue
                lyceemax = lycee + " " + ac
    return lyceemax

print("\nLycée avec la plus grande plus-value en ES en 2012:", q5a(base))

def q5b(indicateurs):
    lyceemax = ''
    plusvaluemax = 0
    for ligne in indicateurs:
        lycee = ligne[0]
        annee = ligne[1]
        ac = ligne[3]
        if annee == '2016':
            plusvalueligne = plus_value_max(ligne)
            if plusvalueligne != None and plusvalueligne > plusvaluemax:
                plusvaluemax = plusvalueligne
                lyceemax = lycee + " " + ac
    return lyceemax

print("\nLycée avec la plus grande plus-value globale en 2016:", q5b(base))