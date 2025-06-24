# Modelo_de_Parcial_Pygame
Modelo de Parcial  Adivina el Número (con Pygame)

Ejercicio Práctico:
Este ejercicio tiene como objetivo implementar un juego interactivo utilizando la biblioteca Pygame.
El jugador debe adivinar un número secreto entre 1 y 9. 
Cada intento fallido será registrado y visualmente representado por una cruz roja en la pantalla. 
Al adivinar correctamente el número o cometer el máximo de errores permitidos (4), se muestra un mensaje final en pantalla indicando el resultado. 

Objetivos:
Aplicar estructuras de control, funciones, listas y condicionales.
Utilizar eventos del teclado. 
Dibujar en pantalla elementos gráficos según la lógica del juego. 
Reproducir sonido en situaciones específicas (errores).
 Estructurar correctamente el ciclo de vida de un juego con Pygame. 
Utilizar funciones y estructurar código en archivos e incorporarlos con import.

Instrucciones:
Crear un proyecto en una carpeta que contenga el archivo `error.wav`. 
Inicializar Pygame y crear la ventana principal con tamaño 800x600. 
Definir colores, fuente, y cargar el sonido de error usando pygame.mixer. 
Crear una función `mostrar_texto()` para mostrar texto en pantalla con coordenadas. 
Crear una función `dibujar_cruces(errores)` que dibuje una cruz roja por cada error cometido (máximo 4). 
Crear la función `nuevo_juego()` que retorne un número aleatorio del 1 al 9, una lista vacía de intentos, y contador de errores en 0.
Crear la función `procesar tecla(tecla, número secreto, intentos, errores)` que reciba la letra presionada. 
Si es el número correcto, retornar que ganó.
Si no, reproducir el sonido y sumar un error. 
En la función principal `jugar()`: - Iniciar el bucle principal del juego (`while jugando:`) con reloj a 30 FPS.
Crear un personaje(archivo aparte personaje.py, con sus funciones y diccionario→verificar la ppt de personajes),  con una imagen y un cuadrado que se muestre inicialmente en una posición de la ventana que no perjudique el juego, y 
que se pueda mover de izquierda a derecha(opcional agregar el personaje abajo en la ventana)
Si el personaje colisionó contra un obstáculo que se ejecute un sonido diferente al anterior.

Limpiar la pantalla en cada iteración con un fondo blanco. 
Dibujar los textos: instrucciones y lista de intentos. 
Dibujar las cruces según los errores. 
Capturar eventos del teclado y evaluar la letra presionada con `procesar tecla`. 
Si acierta, mostrar mensaje de victoria. Si llega a 4 errores, mostrar derrota con el número correcto. 
Actualizar la pantalla en cada ciclo.

Finalizar Pygame correctamente luego de mostrar el resultado final con un pequeño retardo (3 segundos). quit, sys.exit
Comentar todo el código línea por línea explicando claramente cada instrucción. 

Recomendaciones: 
Probar constantemente cada función antes de avanzar. 
Usar nombres de variables descriptivos. 
Cuidar la organización del código y la indentación. 
Consultar la documentación oficial de Pygame o los ejemplos trabajados en clase.
