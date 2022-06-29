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

# Exercice 2 - 1)
#****************
r1 = pygame.Rect(100,0,400,400)
pygame.draw.rect(window, black, r1)
r2 = pygame.Rect(150,50,300,300)
pygame.draw.rect(window, blue, r2)
r3 = pygame.Rect(200,100,200,200)
pygame.draw.rect(window, green, r3)
r4 = pygame.Rect(250,150,100,100)
pygame.draw.rect(window, red, r4)

pygame.display.update()

lock = True
while lock:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # événement de fermeture de la fenêtre
            lock = False # on passe lock à False dans ce cas

pygame.quit()