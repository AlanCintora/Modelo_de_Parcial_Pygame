# personaje.py

import pygame

# Diccionario del personaje con imagen y posición inicial
def crear_personaje():
    imagen = pygame.image.load("personaje.png")
    imagen = pygame.transform.scale(imagen, (80, 80))  # Ajustá tamaño si necesitás
    rect = imagen.get_rect()
    rect.midbottom = (400, 580)  # Lo colocamos abajo, en el centro
    return {"imagen": imagen, "rect": rect}

# Función para mover al personaje con teclas izquierda/derecha
def mover_personaje(personaje, tecla):
    if tecla == pygame.K_LEFT:
        personaje["rect"].x -= 10
    elif tecla == pygame.K_RIGHT:
        personaje["rect"].x += 10

    # Limitar el movimiento a los bordes de la pantalla
    personaje["rect"].x = max(0, min(800 - personaje["rect"].width, personaje["rect"].x))
