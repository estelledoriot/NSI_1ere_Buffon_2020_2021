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

# Question 5
#***********
for i in range(20):
    r = pygame.Rect(100 + i * 10, i * 10, 400 - i * 20, 400 - i * 20)
    if i % 2 == 0:
        color = black
    else:
        color = white
    pygame.draw.rect(window, color, r)

pygame.display.update()

lock = True
while lock:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # événement de fermeture de la fenêtre
            lock = False # on passe lock à False dans ce cas

pygame.quit()