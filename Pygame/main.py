# Importamos las librerías necesarias
import pygame
import os
import random
import sys
from personaje import crear_personaje, mover_personaje

# Inicializamos Pygame
pygame.init()
pygame.mixer.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Creamos la ventana principal
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Adivina el Número")

# Colores (RGB)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Fuente para los textos
fuente = pygame.font.SysFont(None, 48)

# Cargamos el sonido de error
sonido_error = pygame.mixer.Sound("error.wav")

# Función para mostrar texto en pantalla
def mostrar_texto(texto, x, y):
    superficie = fuente.render(texto, True, NEGRO)
    ventana.blit(superficie, (x, y))

# Función para dibujar cruces rojas por cada error cometido
def dibujar_cruces(errores):
    for i in range(errores):
        # Cada cruz se desplaza 50 píxeles hacia la derecha
        x = 50 + i * 60
        y = 50
        pygame.draw.line(ventana, ROJO, (x, y), (x + 30, y + 30), 5)
        pygame.draw.line(ventana, ROJO, (x + 30, y), (x, y + 30), 5)

# Función que inicia un nuevo juego, devolviendo el número secreto y estructuras iniciales
def nuevo_juego():
    numero_secreto = random.randint(1, 9)  # Número aleatorio entre 1 y 9
    intentos = []  # Lista vacía para registrar intentos
    errores = 0    # Contador de errores
    return numero_secreto, intentos, errores

# Función que procesa la tecla presionada por el jugador
def procesar_tecla(tecla, numero_secreto, intentos, errores):
    try:
        intento = int(tecla)  # Convertimos la tecla presionada en número
        if intento < 1 or intento > 9:
            return False, errores  # Ignoramos números fuera de rango

        if intento in intentos:
            return False, errores  # Ya lo intentó antes

        intentos.append(intento)  # Guardamos el intento

        if intento == numero_secreto:
            return True, errores  # ¡Adivinó!

        # Si falló, reproducimos el sonido de error y sumamos un error
        sonido_error.play()
        errores += 1
        return False, errores

    except ValueError:
        return False, errores  # Ignoramos teclas que no son números
def jugar():
    reloj = pygame.time.Clock()  # Controla la velocidad del juego
    jugando = True

    numero_secreto, intentos, errores = nuevo_juego()

    gano = False
    mostrar_resultado = False
    tiempo_final = 0
    personaje = crear_personaje()


    while jugando:
        ventana.fill(BLANCO)  # Limpiamos pantalla en cada iteración

        # Mostrar instrucciones
        mostrar_texto("Presioná un número del 1 al 9", 50, 500)
        mostrar_texto(f"Intentos: {intentos}", 50, 550)

        # Dibujamos las cruces de errores
        dibujar_cruces(errores)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

            if evento.type == pygame.KEYDOWN and not mostrar_resultado:
                tecla = evento.unicode
                # Mover personaje si se presiona flecha
                mover_personaje(personaje, evento.key)
                acierto, errores = procesar_tecla(tecla, numero_secreto, intentos, errores)
                if acierto:
                    gano = True
                    mostrar_resultado = True
                    tiempo_final = pygame.time.get_ticks()
                elif errores >= 4:
                    mostrar_resultado = True
                    tiempo_final = pygame.time.get_ticks()

        if mostrar_resultado:
            if gano:
                mostrar_texto("¡Ganaste! 🎉", 300, 200)
            else:
                mostrar_texto(f"Perdiste 😢 Era: {numero_secreto}", 250, 200)
            # Esperamos 3 segundos y salimos
            if pygame.time.get_ticks() - tiempo_final > 3000:
                jugando = False
        ventana.blit(personaje["imagen"], personaje["rect"])        
        pygame.display.flip()  # Actualizamos pantalla
        reloj.tick(30)  # Limitamos a 30 FPS

    # Cerramos Pygame correctamente
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    jugar()
