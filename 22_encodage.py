# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Encodage
# **********************************

# lecture du fichier
reader = open("encodage.txt", "r", encoding="latin-1")
s = reader.read()
reader.close()
print(s)

# création et écriture dans le nouveau fichier
writer = open("encodage_utf8.txt", "a", encoding="utf−8")
writer.write(s)
writer.close()
