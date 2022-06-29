#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Pygame
#**********************************

import pygame

pygame.init()
size = (600, 400)
window = pygame.display.set_mode(size)

blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

window.fill(white)

# Exercice 1
#***********
r1 = pygame.Rect(0, 0, 200, 400)
pygame.draw.rect(window, blue, r1) # peint un rectangle bleu
r2 = pygame.Rect(200, 0, 200, 400)
pygame.draw.rect(window, white, r2) # peint un rectangle blanc
r3 = pygame.Rect(400, 0, 200, 400)
pygame.draw.rect(window, red, r3) # peint un rectangle rouge

pygame.display.update()

lock = True
while lock:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # événement de fermeture de la fenêtre
            lock = False # on passe lock à False dans ce cas

pygame.quit()