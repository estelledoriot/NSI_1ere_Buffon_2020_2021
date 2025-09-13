# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD : données en tables 2
# **********************************

## Partie A


def split(texte, sep):
    resultat = []
    r = ""
    for lettre in texte:
        if lettre == sep:
            resultat.append(r)
            r = ""
        else:
            r += lettre
    if sep == "\n" and r == "":
        pass
    else:
        resultat.append(r)
    return resultat


def create_dataset(nom_fichier):
    fichier = open(nom_fichier, "r")
    texte = fichier.read()
    fichier.close()
    donnees = split(texte, "\n")
    resultat = []
    for ligne in donnees:
        resultat.append(split(ligne, "\t"))
    return resultat


movies = create_dataset("movies.tsv")
names = create_dataset("names.tsv")
casting = create_dataset("casting.tsv")
directors = create_dataset("directors.tsv")

print("Nombre de lignes de movies:", len(movies))
print("Nombre de lignes de names:", len(names))
print("Nombre de lignes de casting:", len(casting))
print("Nombre de lignes de directors:", len(directors))

print(movies[68761])
print(names[942])
print(casting[129523])

## Partie B


# Question 1
def q1():
    cpt = 0
    for ligne in movies:
        annee = ligne[2]
        if annee == "2019":
            cpt += 1
    return cpt


print("\nNombre de films parus en 2019:", q1())


# Question 2
def est_comedie(ligne):
    genres = split(ligne[4], ",")
    for elt in genres:
        if elt == "Comedy":
            return True
    return False


def q2():
    cpt = 0
    for ligne in movies:
        annee = ligne[2]
        if annee == "2018" and est_comedie(ligne):
            cpt += 1
    return cpt


print("\nNombre de comédies parues en 2018:", q2())


# Question 3
def q3():
    maxfilm = ""
    maxduree = 0
    for ligne in movies:
        film = ligne[1]
        annee = ligne[2]
        if annee == "2016":
            duree = ligne[3]
            if duree != "\\N" and int(duree) > maxduree:
                maxduree = int(duree)
                maxfilm = film
    return maxfilm, maxduree


print("\nPlus long film sorti en 2016:", q3()[0], "avec pour durée:", q3()[1])


# Question 4 a)
def get_id(name):
    for ligne in names:
        identifiant = ligne[0]
        nom = ligne[1]
        if nom == name:
            return identifiant


print("\nIdentifiant de Virginie Efira:", get_id("Virginie Efira"))


# Question 4 b)
def q4():
    ident = get_id("Virginie Efira")
    cpt = 0
    for ligne in casting:
        idacteur = ligne[1]
        if idacteur == ident:
            cpt += 1
    return cpt


print("Nombre de films:", q4())


# Question 5
def get_movie_name(idfilm):
    for ligne in movies:
        idfilm2 = ligne[0]
        film = ligne[1]
        if idfilm2 == idfilm:
            return film


def q5():
    ident = get_id("Catherine Corsini")
    resultat = []
    for ligne in directors:
        idfilm = ligne[0]
        directeurs = split(ligne[1], ",")
        if ident in directeurs:
            resultat.append(get_movie_name(idfilm))
    return resultat


print("\nFilms de Catherine Corsini depuis 2015:", q5())


## Partie C
def film_realisateur():
    fichier = open("resultats.tsv", "w", encoding="utf-8")
    fichier.write("tconst\tprimaryTitle\tdirectors\n")
    for i in range(1, len(movies)):
        idfilm = movies[i][0]
        film = movies[i][1]
        realisateurs = directors[i][1]
        fichier.write(idfilm + "\t" + film + "\t" + realisateurs + "\n")
    fichier.close()


film_realisateur()


## Partie D
def get_name(ident):  # version naive
    for ligne in names:
        identifiant = ligne[0]
        nom = ligne[1]
        if identifiant == ident:
            return nom
    return "\\N"


def film_realisateur2():
    fichier = open("resultats2.tsv", "w", encoding="utf-8")
    fichier.write("tconst\tprimaryTitle\tdirectorsName\n")
    for i in range(1, len(movies)):
        idfilm = movies[i][0]
        film = movies[i][1]
        idreal = split(directors[i][1], ",")
        r = []
        for elt in idreal:
            r.append(get_name(elt))
            realisateurs = ",".join(r)
        fichier.write(idfilm + "\t" + film + "\t" + realisateurs + "\n")
    fichier.close()


# film_realisateur2()


def get_name2(ident):
    if ident == "\\N":
        return ident
    debut = 0
    fin = len(names) - 1
    while debut <= fin:
        c = (debut + fin) // 2
        idt = names[c][0]
        nom = names[c][1]
        if idt == ident:
            return nom
        elif idt > ident:
            fin = c - 1
        else:
            debut = c + 1
    return "\\N"


def film_realisateur3():
    fichier = open("resultats3.tsv", "w", encoding="utf-8")
    fichier.write("tconst\tprimaryTitle\tdirectorsName\n")
    for i in range(1, len(movies)):
        idfilm = movies[i][0]
        film = movies[i][1]
        idreal = split(directors[i][1], ",")
        r = []
        for elt in idreal:
            r.append(get_name2(elt))
            realisateurs = ",".join(r)
        fichier.write(idfilm + "\t" + film + "\t" + realisateurs + "\n")
    fichier.close()


film_realisateur3()
