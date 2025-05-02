# Proyecto integrador - Opción 2
### Proyecto Final: Buscaminas en Python
### Objetivo: Desarrollar una versión funcional del juego clásico Buscaminas:
Listas
Vectores y matrices

Modularidad (dividir el programa en funciones)

Estructuras de control (for, while)

Manejo básico de fechas (para el reto opcional)

## Estructuras principales:
### Registro de usuarios
Guardar los usuarios con la siguiente información.
usuario: "nombre_usuario", "correo_usuario", "id_usuario"
El id_usuario puede generarse automáticamente (por ejemplo, usando la librería random).
### Dificultades definidas:
Definir los niveles de dificultad del juego:
“Easy”, “Medium”, “Expert”.
Para cada nivel definir el tablero de juego, (predeterminado en el código):

Easy: Tamaño del tablero 6x6 y 4 bombas.

Medium: Tamaño del tablero 8x8 y 9 bombas.

Expert: Tamaño del tablero 10x10 y 15 minas.

El usuario debe poder elegir el nivel antes de empezar.
### Puntaje (score):

• Cada casilla descubierta sin mina suma 1 punto.

• Si el jugador gana, se otorgan 10 puntos extra.

• Si pierde, conserva los puntos acumulados antes de explotar la mina.

El nombre del jugador y su puntaje deben registrarse como “nombre_usuario”,
“puntaje”, “nivel de dificultad” y si fue una partida ganada o pérdida. Si al guardar un
nuevo store ya existe para ese usuario y nivel un registro actualizar.

## Casos de uso a implementar:
### 1. Registrar un nuevo usuario.
Preguntar nombre, correo y generar un ID de identificación automáticamente.
Agregar el nuevo usuario al registro de users.
### 2. Iniciar nuevo juego:
Validar el usuario que jugará, solicitar nivel y luego de validar la casilla ingresada
mostrar el tablero actualizado con la cantidad de minas al rededor o indicar si finalizo
el juego. Mostrar en cada intento el puntaje acumulado.
Validar que la celda indicada sea válida y que no haya sido ingresada anteriormente.
### 3. Encontrar usuario con mayor puntaje por nivel. Mostrar correo, nivel y puntaje
(partida ganada).
## Bono:
### 1. Imprimir partidas de un usuario en un formato legible.
### 2. Usar la librería time para medir cuánto tiempo tomó la partida. 
Guardar al finalizar la partida ese tiempo. Mostrar el top 3 de partidas ganadas del nivel HARD ordenados por tiempo

## Problemas encontrados

# Randomizar el tablero

Tomamos la decisión como equipo de que el tablero sea generado de manera distinta cada vez, esto, para evitar que el jugador se aprenda el tablero y mejore sus tiempos con base en este conocimiento previo del tablero; lo cual nos llevó al primer problema que encontramos:
¿Cómo hacer que el tablero se genere de manera aleatoria cada vez que se inicia una partida?
Utilizamos la librería random para crear 4, 9 o 15 valores dependiendo de la dificultad elegida, con estos valores, calculamos sus posiciones en el apartado 3 de la función generar_tablero y cambiamos los valores en las posiciones de 0 a M, para indicar la presencia de una mina.

## Conclusiones
