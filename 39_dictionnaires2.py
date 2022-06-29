#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD dictionnaire 2
#**********************************

def affiche_dico(dico):
    """
    fonction qui prend en argument un dictionnaire et qui affiche ses données en alignant les clés et les valeurs
    """
    for key,value in dico.items():
        print(key, ":\t", value)

# Question 2 a)
#**************

import PIL.Image # importation du module Image de PIL 2
img = PIL.Image.open("image_mystere.jpg") # ouverture du fichier jpg
exif_dico = img._getexif() # récupération des données EXIF

# affichage des données EXIF
print("\nDonnées EXIF:")
affiche_dico(exif_dico)

# Question 2 b)
#**************

# Les clés du dictionnaire sont des entiers

# Question 3 a)
#**************

from PIL.ExifTags import TAGS
print("\nTAGS des données EXIF:")
affiche_dico(TAGS)

# Question 3 b) et c)
#********************

print(TAGS[306])
print(TAGS[36867])
print(TAGS[36868])

# Question 3 d)
#**************

def get_original_time(filename):
    img = PIL.Image.open(filename) 
    exif_dico = img._getexif() 
    for key,value in TAGS.items():
        if value == 'DateTimeOriginal':
            return exif_dico[key]

print("\nDate et heure de la photo: ", get_original_time("image_mystere.jpg"))

# Question 4 a)
#**************

for key,value in TAGS.items():
    if value == 'GPSInfo':
        gps = key

print("\nClé TAGS correspondant à GPSInfo: ", gps)

# Question 4 b)
#**************

print("\nInformations GPS de la photo: ")
affiche_dico(exif_dico[gps])
# La valeur renvoyée est un dictionaire

# Question 4 c)
#**************

from PIL.ExifTags import GPSTAGS
print("\nGPSTAGS:")
affiche_dico(GPSTAGS)

# Question 4 d)
#**************

for key,value in GPSTAGS.items():
    if value == 'GPSLatitude':
        latitude = exif_dico[gps][key]
    elif value == 'GPSLongitude':
        longitude = exif_dico[gps][key]

print("\nLatitude de la photo: ", latitude)
print("Longitude de la photo: ", longitude)

# Question 4 e)
#**************

latitude_degres = latitude[0] + latitude[1]/60 + latitude[2]/3600
longitude_degres = longitude[0] + longitude[1]/60 + longitude[2]/3600

print("\nLatitude de la photo (degres): ", float(latitude_degres))
print("Longitude de la photo (degres): ", float(longitude_degres))

# Question 5
#***********

def exif_clair(filename):
    """
    crée un dictionnaire de données EXIF avec des clés éloquentes
    """
    img = PIL.Image.open(filename) 
    exif_dico = img._getexif() 
    exif_c = {}
    for key,value in exif_dico.items():
        for cle,valeur in TAGS.items():
            if key == cle:
                exif_c[valeur] = value
                break
    gps = exif_c['GPSInfo']
    gps_c = {}
    for key,value in gps.items():
        for cle,valeur in GPSTAGS.items():
            if key == cle:
                gps_c[valeur] = value
                break
    exif_c['GPSInfo'] = gps_c
    return exif_c

print("\nDonnées EXIF claires de la photo:")
affiche_dico(exif_clair("image_mystere.jpg"))

# Question 6
#***********

def exif_clair2(filename):
    """
    crée un dictionnaire de données EXIF avec des clés éloquentes
    écrit les résultats dans un fichier csv
    """
    img = PIL.Image.open(filename) 
    exif_dico = img._getexif() 
    nom_photo = filename.split(".")[0]
    fichier = open("EXIF_" + nom_photo + ".csv", 'w', encoding = "utf-8")
    fichier.write("balise EXIF,valeur\n")
    for key,value in exif_dico.items():
        for cle,valeur in TAGS.items():
            if key == cle:
                if valeur == 'GPSInfo':
                    gps_c = {}
                    for k,v in value.items():
                        for k2,v2 in GPSTAGS.items():
                            if k == k2:
                                gps_c[v2] = v
                                break
                    fichier.write(valeur + "," + str(gps_c) + "\n")
                else:
                    fichier.write(valeur + "," + str(value) + "\n")
                break
    fichier.close()

exif_clair2("image_mystere.jpg")