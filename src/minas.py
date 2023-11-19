"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""
FILAS = 8
COLUMNAS = 8
VACIO:int = " "
MINA:int = "*"
NUMERODEMINAS:int = 10
BANDERA:str = "🚩"
HELP = """
Esta es la ayuda del buscaminas de Natalia, creado para una actividad de clase en la cual practicamos para el examen de programación correspondiente al lenguaje de programación python.
    - 1: Revelar celda -> Esta función está dedicada a descubrir
            una celda del juego, si hay una mina habrás perdido, si no la hay sigue el juego 
    - 2: Marcar celda -> Esta función está dedicada a marcar la casilla deseada por el usuario así como en el juego original se puede marcar con una bandera la posición en la que se cree que hay una bandera.
    - 3: Salir -> Esta opción finaliza la ejecución del programa.
    - other: other -> Muestra este menú.
"""
celdasReveladas = set()
celdasMarcadas= set()

import random
tablero8x8:list = [
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO]
]

listaMinas = []
listaNumeros = []
listaCeldasVacías = []

def entradaDeDatos(mensaje:str):
    return input(mensaje)

def imprimirTablero(mostrarMinas:bool = False):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            
            if (fila, columna) in celdasReveladas or mostrarMinas:
                print(tablero8x8[fila][columna], end=' ')
            elif (fila, columna) in celdasMarcadas:
                print(BANDERA, end=' ')
            else:
                print('-', end=' ')
        print()

def colocarMinar()->list:
    # ? Como hacer para que el usuario no vea donde están las minas?
    while len(listaMinas) < NUMERODEMINAS:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if (fila, columna) not in listaMinas:
            listaMinas.append((fila, columna))
            tablero8x8[fila][columna] = MINA
            for i in range(fila - 1, fila + 2):
                for j in range(columna - 1, columna + 2):
                    if 0 <= i < FILAS and 0 <= j < COLUMNAS and (i, j) not in listaMinas:
                        if tablero8x8[i][j] == ' ':
                            tablero8x8[i][j] = '1'
                        else:
                            tablero8x8[i][j] = str(int(tablero8x8[i][j]) + 1)
                            

def marcarCelda():
    posicionX = int(entradaDeDatos("Introduzca la primera posición: "))
    posicionY = int(entradaDeDatos("Introduzca la segunda posición: "))
    if (posicionX, posicionY) not in celdasMarcadas:
        celdasMarcadas.add((posicionX, posicionY))
    

def revelarCelda(posicionX, posicionY):
    if (posicionX, posicionY) in celdasReveladas:
        return 
    filas = len(tablero8x8)
    columnas = len(tablero8x8[0])
    if posicionX < 0 or posicionY < 0 or posicionX >= filas or posicionY >= columnas:
        return 
    if tablero8x8[posicionX][posicionY] != ' ':
        celdasReveladas.add((posicionX, posicionY))
        return
    tablero8x8[posicionX][posicionY] = '0'
    celdasReveladas.add((posicionX, posicionY))
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                revelarCelda(posicionX + i, posicionY + j)

def juegoTerminado(posicionX, posicionY):
    if len(celdasMarcadas) == FILAS * COLUMNAS - NUMERODEMINAS:
        return False
    elif (posicionX, posicionY) in listaMinas: 
        return True

def salir():
    print("chaaaaaaaaaaaao chao chao chao")

def jugar():
    """
    Esta función ejecuta el juego.
    """
    imprimirTablero(False)
    colocarMinar()

    partida = True
    print(HELP)
    while partida:
        accion = int(entradaDeDatos("Selecciona la accion: "))
        print()
    
        match accion:
            case 1:
                posicionX = int(entradaDeDatos("Introduzca la primera posición: "))
                posicionY = int(entradaDeDatos("Introduzca la segunda posición: "))
                if juegoTerminado(posicionX, posicionY):
                    imprimirTablero(True)
                    partida = False
                else:
                    revelarCelda(posicionX, posicionY)
                    imprimirTablero()
            case 2:
                imprimirTablero(marcarCelda())

            case 3:
                salir()
            case other:
                print("Error introduce un tipo de dato válido")
    print("Has perdido")
if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
