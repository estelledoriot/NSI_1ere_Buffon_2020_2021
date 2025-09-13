# ***********************************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD compléments sur les chaines de caractères
# ***********************************************

# Exercice n°1
# *************
print("\n** Exercice n°1:")

ch = "bonjour"
x = ch[len(ch) - 1]
print(x)

# Exercice n°2
# *************
print("\n** Exercice n°2:")

# 1)
print("\n**1)")


def est_numerique(c):
    ptc = ord(c)
    return ord("0") <= ptc and ptc <= ord("9")


print("Est-ce que 7 est un chiffre?", est_numerique("7"))
print("Est-ce que A est un chiffre?", est_numerique("A"))

# 2)
print("\n**2)")


def format_date_valide(ch):
    if len(ch) != 10:
        return False
    if ch[2] != "/" or ch[5] != "/":
        return False
    for i in range(len(ch)):
        if i != 2 and i != 5:
            if not (est_numerique(ch[i])):
                return False
    return True


print("Est-ce que 06/01/2020 est une date valide?", format_date_valide("06/01/2020"))
print("Est-ce que 06/0172020 est une date valide?", format_date_valide("06/0172020"))
print("Est-ce que 06/01/20209 est une date valide?", format_date_valide("06/01/20209"))
print("Est-ce que 06/j1/2020 est une date valide?", format_date_valide("06/j1/2020"))
print("Est-ce que ////////// est une date valide?", format_date_valide("//////////"))

# 3)
print("\n**3)")


def bissextile(annee):
    return (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0)


def date_valide(ch):
    mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not format_date_valide(ch):
        return False

    aaaa = int(ch[6] + ch[7] + ch[8] + ch[9])
    mm = int(ch[3] + ch[4])
    jj = int(ch[0] + ch[1])

    if mm < 1 or mm > 12:
        return False

    if jj < 1:
        return False

    if bissextile(aaaa) and mm == 2 and jj > 29:
        return False

    if jj > mois[mm - 1]:
        return False

    return True


print("Est-ce que 01/01/2000 est une date valide?", date_valide("01/01/2000"))
print("Est-ce que 29/02/2000 est une date valide?", date_valide("29/02/2000"))
print("Est-ce que 29/02/2001 est une date valide?", date_valide("29/02/2001"))
print("Est-ce que 35/05/2000 est une date valide?", date_valide("35/05/2000"))
print("Est-ce que 00/05/2000 est une date valide?", date_valide("00/05/2000"))
print("Est-ce que 12/37/2000 est une date valide?", date_valide("12/37/2000"))

# Exercice n°3
# *************
print("\n** Exercice n°3:")

# 1)
print("\n**1)")


def char_minuscule(c):
    ptc = ord(c)
    if ord("A") <= ptc and ptc <= ord("Z"):
        return chr(ptc + 32)
    else:
        return c


print("G en minuscule:", char_minuscule("G"))
print("h en munuscule:", char_minuscule("h"))
print("! en minuscule:", char_minuscule("!"))

# 2)
print("\n**2)")


def minuscules(ch):
    r = ""
    for l in ch:
        r = r + char_minuscule(l)
    return r


print("Hello World ! en minuscules:", minuscules("Hello World !"))

# Exercice n°4
# *************
print("\n** Exercice n°4:")

# 1)
print("\n**1)")


def binaire_valide(ch):
    for l in ch:
        if l != "0" and l != "1":
            return False
    return True


print("Est-ce que 1010001 est du binaire?", binaire_valide("1010001"))
print("Est-ce que 124533 est du binaire?", binaire_valide("124533"))

# 2)
print("\n**2)")


def bin_to_dec(ch):
    n = len(ch)
    s = 0
    for i in range(n):
        if ch[n - 1 - i] == "1":
            s = s + 2**i
    return s


print("10 en décimal:", bin_to_dec("10"))
print("11111111 en décimal:", bin_to_dec("11111111"))

# 3)
print("\n**3)")


def hexa_valide(ch):
    for l in ch:
        ptc = ord(l)
        if not (ord("0") <= ptc and ptc <= ord("9")) and not (
            ord("A") <= ptc and ptc <= ord("F")
        ):
            return False
    return True


print("Est-ce que 1023556 est de l'hexadécimal?", hexa_valide("1023556"))
print("Est-ce que FF73DD est de l'hexadécimal?", hexa_valide("FF73DD"))
print("Est-ce que 4556MM est de l'hexadécimal?", hexa_valide("4556MM"))

# 4)
print("\n**4)")


def convert_hexa(c):
    ptc = ord(c)
    if ord("0") <= ptc and ptc <= ord("9"):
        return ptc - ord("0")
    if ord("A") <= ptc and ptc <= ord("F"):
        return ptc - ord("A") + 10


def hexa_to_dec(ch):
    n = len(ch)
    s = 0
    for i in range(n):
        s = s + (16**i) * convert_hexa(ch[n - 1 - i])
    return s


print("A en décimal:", hexa_to_dec("A"))
print("FF en décimal:", hexa_to_dec("FF"))
print("10 en décimal:", hexa_to_dec("10"))

# Exercice n°5
# *************
print("\n** Exercice n°5:")


def est_palindrome(ch):
    n = len(ch)
    for i in range(n // 2):
        if ch[i] != ch[n - 1 - i]:
            return False
    return True


print("Est-ce que été est un palindrome?", est_palindrome("été"))
print("Est-ce que ressasser est un palindrome?", est_palindrome("ressasser"))

# Exercice n°6
# *************
print("\n** Exercice n°6:")

# 1)
print("\n**1)")


def miroir(ch):
    r = ""
    for lettre in ch:
        r = lettre + r
    return r


print("bonjour en miroir:", miroir("bonjour"))

# 2)
print("\n**2)")


def est_palindrome2(ch):
    c = miroir(ch)
    return c == ch


print("Est-ce que ressasser est un palindrome?", est_palindrome2("ressasser"))
print("Est-ce que bonjour est un palindrome?", est_palindrome2("bonjour"))

# Exercice n°7
# *************
print("\n** Exercice n°7:")

# 1)
print("\n**1)")

d = "01/02/1997"
lst = d.split("/")
print(lst)

# 2)
print("\n**2)")


def nom_prenom(lst):
    for i in range(len(lst)):
        personne = lst[i].split(" ")
        lst[i] = personne[1] + " " + personne[0]
    return lst


print(
    nom_prenom(
        [
            "Alan Turing",
            "Ada Lovelace",
            "Donald Knuth",
            "Claude Shannon",
            "Grace Hopper",
        ]
    )
)

# Exercice n°8
# *************
print("\n** Exercice n°8:")


def suppr_espaces(ch):
    lst = list(ch)
    for i in range(len(lst)):
        if lst[i] == " ":
            lst[i] = "_"
    return "".join(lst)


print(suppr_espaces("ma photo de vacances.jpg"))

# Exercice n°9
# *************
print("\n** Exexcice n°9:")


def hamming(ch1, ch2):
    if len(ch1) != len(ch2):
        return -1
    n = 0
    for i in range(len(ch1)):
        if ch1[i] != ch2[i]:
            n = n + 1
    return n


print("Distance de hamming aaba et aaha:", hamming("aaba", "aaha"))
print("Distance de hamming poire et pomme:", hamming("poire", "pomme"))
print("Distance de hamming stylo et bouteille:", hamming("stylo", "bouteille"))

# Exercice n°10
# **************
print("\n** Exexcice n°10:")

# 1)
print("\n**1)")


def nb_occurrences(texte, lettre):
    n = 0
    for l in texte:
        if l == lettre:
            n = n + 1
    return n


print(
    "Nombre d'occurrences de a dans alea jacta est:",
    nb_occurrences("alea jacta est", "a"),
)

# 2)
print("\n**2)")


def lettre(n):
    return chr(n + ord("a"))


def numero(l):
    return ord(l) - ord("a")


def index_max(lst):
    m = lst[0]
    n = 0
    for i in range(len(lst)):
        if lst[i] > m:
            m = lst[i]
            n = i
    return n


def lettre_plus_frequente(texte):
    occurrences = [0] * 26
    for l in minuscules(texte):
        a = numero(l)
        if 0 <= a and a <= 25:
            occurrences[a] += 1
    return lettre(index_max(occurrences))


print(
    "Lettre la plus fréquente:",
    lettre_plus_frequente(
        "Le francais est une langue romane de la famille des langues indo europeennes"
    ),
)

# Exercice n°11
# **************
print("\n** Exexcice n°11:")


def vigenere(m, k, s):
    t = [""] * len(m)
    for i in range(len(m)):
        t[i] = lettre((numero(m[i]) + s * numero(k[i % (len(k))])) % 26)
    return "".join(t)


# 1)
print("\n**1)")


def chiffre_vigenere(msg, key):
    return vigenere(msg.lower(), key.lower(), 1)


print(chiffre_vigenere("lyceebuffon", "nsi"))

# 2)
print("\n**2)")


def dechiffre_vigenere(msg, key):
    return vigenere(msg.lower(), key.lower(), -1)


print(dechiffre_vigenere("yqkrwjhxnbf", "nsi"))

# Exercice n°12
# **************
print("\n** Exexcice n°12:")


def plus_long_palindrome(mot):
    n = len(mot)
    lmax = 0
    m = ""
    for i in range(n):
        d = 1
        while d <= i and d <= n - 1 - i and mot[i - d] == mot[i + d]:
            d += 1
        if 2 * d - 1 > lmax:
            lmax = 2 * d - 1
            m = mot[i - d + 1 : i + d]
    for i in range(n - 1):
        d = 0
        while d <= i and d <= n - 2 - i and mot[i - d] == mot[i + 1 + d]:
            d += 1
        if 2 * d > lmax:
            lmax = 2 * d
            m = mot[i - d + 1 : i + d + 1]
    return m


print("Plus long palindrome de abracadabra:", plus_long_palindrome("abracadabra"))
print("Plus long palindrome d laval:", plus_long_palindrome("laval"))
print("Plus long palindrome de abcd:", plus_long_palindrome("abcd"))
