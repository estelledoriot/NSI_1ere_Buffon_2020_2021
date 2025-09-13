# **********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * Exemple pygame
# **********************************

import pygame

pygame.init()  # initialisation du module

size = (600, 400)  # taille de la fenêtre
window = pygame.display.set_mode(size)  # ouverture de la fenêtre
# window prend la valeur de l'objet qui représente la fenêtre

gray = (128, 128, 128)
window.fill(gray)  # peint la fenêtre en gris

blue = (0, 0, 255)
r = pygame.Rect(200, 100, 200, 100)  # syntaxe : (left, top, width, height)
pygame.draw.rect(window, blue, r)  # peint un rectangle bleu

yellow = (255, 255, 0)
r = pygame.Rect(300, 50, 50, 100)
pygame.draw.rect(window, yellow, r)  # peint un rectangle jaune

pygame.display.update()  # mise à jour de la fenêtre

lock = True
while lock:  # boucle pour maintenir la fenêtre ouverte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # événement de fermeture
            lock = False

pygame.quit()  # fermeture de la fenêtre
