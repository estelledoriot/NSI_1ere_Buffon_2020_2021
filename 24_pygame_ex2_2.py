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

# Exercice 2 - 2
#***************
for i in range(12):
    for j in range(8):
        r = pygame.Rect(i * 50, j * 50, 50, 50)
        if (i + j) % 2 == 0:
            color = white
        else:
            color = black
        pygame.draw.rect(window, color, r)

pygame.display.update()

lock = True
while lock:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # événement de fermeture de la fenêtre
            lock = False # on passe lock à False dans ce cas

pygame.quit()