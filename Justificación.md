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

### Randomizar el tablero

Tomamos la decisión como equipo de que el tablero sea generado de manera distinta cada vez, esto, para evitar que el jugador se aprenda el tablero y mejore sus tiempos con base en este conocimiento previo del tablero; lo cual nos llevó al primer problema que encontramos:
¿Cómo hacer que el tablero se genere de manera aleatoria cada vez que se inicia una partida?
Utilizamos la librería random para crear 4, 9 o 15 valores dependiendo de la dificultad elegida, con estos valores, calculamos sus posiciones en el apartado 3 de la función generar_tablero y cambiamos los valores en las posiciones de 0 a M, para indicar la presencia de una mina.

### Indicadores de minas

Como ahora el tablero es aleatorio necesitamos una manera de generar las indicaciones de cuando una casilla tiene una mina adyacente en las 8 direcciones, para eso usamos el apartado 1 de la función indicadores_minas, que indica la posición de la mina en términos (x,y). Ahora miramos en apartado 2 y 3, que revisa las 9 posiciones en un cuadrado 3x3, si no se está revisando la misma mina (4), se suma uno a la celda utilizando el apartado 5, y se itera con todas las posiciones del cuadrado 3x3 correspondiente a cada mina.

### Legibilidad del tablero

El tablero se imprime de manera correcta, pero las diferencias en tamaños de los caracteres, las columnas no son rectas, por lo que la legibilidad se ve comprometida.
Optamos por imprimir espacios entre cada caracter para garantizar que estén ordenados, adicional, añadimos indicadores de finlas y de columnas para que el jugador las ingrese.
Añadimos un nuevo tablero con las entradas ocultas, utilizando el caracter ■.

### Guardar las partidas
(...)

## Conclusiones

### Modularidad

El uso de modularidad es clave para el funcionamiento del programa, la legibilidad y la resolución de problemas en el código. Así mismo, ayuda a que los comentarios al código sean claros y concisos

### Listas

El uso de listas facilita el registro, actualización y búsqueda de datos, permite ordenar de manera fácil la información y disponerla de manera rápida y efectiva.

### Estructuras de control
(...)
