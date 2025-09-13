# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Chaînes de caractères
# **********************************

m = 'il a dit: "bonjour"'
b = "bonjour "
a = "Marie"

print(b[0])
# b[0]="B" #erreur

# parcours d'une chaîne de caractères
for i in range(len(b)):
    print(b[i])

# parcours d'une chaîne de caractères (2e méthode)
for lettre in b:
    print(lettre)


# suppression des espaces
def suppr_esp(m):
    r = ""
    for lettre in m:
        if lettre != " ":
            r = r + lettre
    return r


print(suppr_esp("Veni Vidi Vici"))

# longueur: len
print(m)
print(len(m))

v = ""
print(len(v))

# concaténation
print(b + a)
print(b * 5)

s = "a b" * 2 + "ba" + "b" * 3
print(s)

# Caractères d'échappement
n = 'il a dit: "bonjour"'
print(len(m))
print(len(n))

p = "\\a"
print(p)

print("\nExercice")
