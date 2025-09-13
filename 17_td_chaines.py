# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Chaînes de caractères
# **********************************

# Exercice n°1
# *************
print("\n** Exercice n°1")

s = "ab" * 2 + "ba" + "b" * 3
print(s, len(s))

# Exercice n°2
# *************
print("\n** Exercice n°2")

s = 'abn\nn\\"'
print(len(s))

# Exercice n°3
# *************
print("\n** Exercice n°3")

s = "abcdefghij"
n = len(s)
print(s[1], s[5])
s = 2 * s
print(n)
print(s[12])

# Exercice n°4
# *************
print("\n** Exercice n°4")


def nb_lettres(s, l):
    c = 0
    for i in s:
        if i == l:
            c += 1
    return c


print("Il y a", nb_lettres("estelle", "e"), "e dans estelle")

# Exercice n°5
# *************
print("\n** Exercice n°5")


def filtre(s, mask):
    r = ""
    for lettre in s:
        if not lettre in mask:
            r = r + lettre
    return r


alea = "alea jacta est"
print(alea, "sans e et a donne:", filtre(alea, "ea"))


def suppr_voyelles(s):
    return filtre(s, "aeiouy")


print(alea, "sans les voyelles donne:", suppr_voyelles(alea))

# Exercice n°6
# *************
print("\n** Exercice n°6")


def miroir(message):
    r = ""
    for lettre in message:
        r = lettre + r
    return r


print(alea, "en miroir donne:", miroir(alea))


def miroir2(message):
    r = ""
    i = len(message) - 1
    while i >= 0:
        r = r + message[i]
        i = i - 1
    return r


# Exercice n°7
# *************
print("\n** Exercice n°7")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rang(l):
    for i in range(len(alphabet)):
        if alphabet[i] == l:
            return i


print("Le rang de la lettre E est:", rang("E"))


def lettre(r):
    return alphabet[r]


print("La lettre n°4 est:", lettre(4))

# Exercice n°8
# *************
print("\n** Exercice n°8")


def codage_cesar(message, d):
    code = ""
    for l in message:
        if l == " ":
            code = code + " "
        else:
            i = rang(l)
            code = code + lettre((i + d) % 26)
    return code


m1 = "LES SANGLOTS LONGS DES VIOLONS DE L AUTOMNE"
print(m1, "est codé en:", codage_cesar(m1, 5))


def decodage_cesar(message, d):
    return codage_cesar(message, -d)


m2 = "QJX XFSLQTYX QTSLX IJX ANTQTSX IJ Q FZYTRSJ"
print(m2, "est décodé ! :", decodage_cesar(m2, 5))


def dec_cesar(message):
    for d in range(26):
        print(decodage_cesar(message, d))


m3 = "ATRWXUUGTBTCIEPGHJQHIXIJIXDCTHIJCTITRWCXFJTSTRWXUUGTBTCIJIXAXHTTSTEJXHQXTCADCVITBEHEJXHFJTATRWXUUGTSTRTHPGTCTHIJCRPHEPGIXRJAXTG"
print("Les différentes possibilités sont:")
dec_cesar(m3)

# Exercice n°9
# *************
print("\n** Exercice n°9")


def code_transp(message, l):
    r = ""
    for i in range(l):
        k = i
        while k < len(message):
            r = r + message[k]
            k = k + l
    return r


m4 = "LESSANGLOTSLONGSDESVIOLONSDELAUTOMNE"
print(code_transp(m4, 7))
