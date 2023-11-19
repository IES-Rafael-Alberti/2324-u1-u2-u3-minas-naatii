"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""
import random
FILAS = 8
COLUMNAS = 8
VACIO:int = " "
MINA:int = "*"
NUMERODEMINAS:int = 10
BANDERA:str = "🚩"
HELP = """
Esta es la ayuda del buscaminas de Natalia, creado para una actividad de clase en la cual practicamos para el examen de programación correspondiente al lenguaje de programación python.
    [^] 1: Revelar celda 
        [>] Esta función está dedicada a descubrir una celda del juego, si hay una mina habrás perdido, si no la hay sigue el juego 
    [^] 2: Marcar celda 
        [>] Esta función está dedicada a marcar la casilla deseada por el usuario así como en el juego original se puede marcar con una bandera la posición en la que se cree que hay una bandera.
    [^] 3: Salir 
        [>] Esta opción finaliza la ejecución del programa.
    [^] other: other 
        [>] Muestra este menú.
"""
celdasReveladas = set()
celdasMarcadas= set()
listaMinas = []
listaNumeros = []
listaCeldasVacías = []
estadoCeldas = {}
estadoMinas = "MINA"
estadoVacias = "VACIAS"
estadoNumero = "NUMERO"
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

def entradaDeDatos(mensaje:str)->str:
    """Funcion para la entrada de datos del juego

    Args:
        mensaje (str): Mensaje que se mostrará en el input

    Returns:
        str: Devuelve el input con el mensaje.
    """
    return input(mensaje)

def imprimirTablero(mostrarMinas:bool = False):
    """Función que imprime el trablero teniendo en cuenta minas y espacios vacíos.

    Args:
        mostrarMinas (bool, optional): booleano que indica si queremos mostrar las minas o no, esto se hace para las pruebas para poder manejar cuando quería ver las minas para comprobar el correcto funcionamiento del programa. Defaults to False.
    """
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            
            if (fila, columna) in celdasReveladas or mostrarMinas:
                print(tablero8x8[fila][columna], end=' ')
            elif (fila, columna) in celdasMarcadas:
                print(BANDERA, end=' ')
            else:
                print('-', end=' ')
        print()

def colocarMinar():
    """Función que realiza la colocación de las minas de forma aleatoria en el trablero, además calcula el número según la cantidad de minas que haya al rededor.
    """
    # ? Como hacer para que el usuario no vea donde están las minas?
    while len(listaMinas) < NUMERODEMINAS:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if (fila, columna) not in listaMinas:
            estadoCeldas[estadoMinas] = (fila, columna)
            listaMinas.append((fila, columna))
            tablero8x8[fila][columna] = MINA
            for i in range(fila - 1, fila + 2):
                for j in range(columna - 1, columna + 2):
                    if 0 <= i < FILAS and 0 <= j < COLUMNAS and (i, j) not in listaMinas:
                        if tablero8x8[i][j] == ' ':
                            estadoCeldas[estadoNumero] = '1'
                            tablero8x8[i][j] = '1'
                        else:
                            estadoCeldas[estadoNumero] = str(int(tablero8x8[i][j]) + 1)
                            tablero8x8[i][j] = str(int(tablero8x8[i][j]) + 1)

def marcarCelda(posicionX, posicionY):
    """Según la posición en el trablero marca la posición añade a un conjunto la posición de la celda marcada, 

    ANOTACION:
        quería añadir desde aquí la bandera al tablero pero me di cuanta que si se colocaba en el tablero directamente eliminaba lo que había anteriormente por lo que la colocación se hace en la función imprimirTablero
        @see imprimirTablero()
    """
    if (posicionX, posicionY) not in celdasMarcadas:
        celdasMarcadas.add((posicionX, posicionY))

def revelarCelda(posicionX:int, posicionY:int)->bool:
    """Función que realiza la acción de revelar la celda según las posiciones ingresadas por el usuario, en relación de si la celda es 0 se revelan todas las de al rededor hasta mostrar números distintos de 0.

    Args:
        posicionX (int): La posición de la fila
        posicionY (int): La posición de la columna

    Returns:
        bool: devuelve true si se puede revelar (la celda y las demás si está vacía) y false si no se puede revelar porque ya haya algo.
    """
    if (posicionX, posicionY) in celdasReveladas:
        return False
    if posicionX < 0 or posicionY < 0 or posicionX >= FILAS or posicionY >= COLUMNAS:
        return False
    if tablero8x8[posicionX][posicionY] != ' ':
        listaCeldasVacías.append((posicionX, posicionY))
        estadoCeldas[estadoVacias] = (posicionX, posicionY)
        celdasReveladas.add((posicionX, posicionY))
        return False
    tablero8x8[posicionX][posicionY] = '0'
    celdasReveladas.add((posicionX, posicionY))
    for i in range(-1, 2):
        for j in range(-1, 2):
            revelarCelda(posicionX + i, posicionY + j)
    return True

def juegoTerminado(posicionX:int, posicionY:int)->str:
    """Evalua si el juego ha terminado dependiendo de si se ha encontrado una mina o de si se ha desvelado todas las celdas sin concontrar una mina.

    Args:
        posicionX (int): La posición de la fila
        posicionY (int): La posición de la columna

    Returns:
        str: has ganado o has perdido si no es ninguna de las 2 sigue el juego.
    """
    if len(celdasReveladas) == FILAS * COLUMNAS - NUMERODEMINAS:
        return "has ganado"
    elif (posicionX, posicionY) in listaMinas: 
        return "has perdido"
    else:
        "sigue el juego"

def salir():
    """Sale del juego imprimiendo un mensaje de salida."""
    print("chaaaaaaaaaaaao chao chao chao")

def jugar():
    """
    Esta función es la función principal del programa, donde se inicializa el tablero, muestra el menú y llama a las funciones pertinentes.
    """
    imprimirTablero(False)
    colocarMinar()
    imprimirTablero(True)

    partida = True
    print(HELP)
    while partida:
        accion = int(entradaDeDatos("Selecciona la accion: "))
        print()
    
        match accion:
            case 1:
                posicionX = int(entradaDeDatos("Introduzca la primera posición: "))
                posicionY = int(entradaDeDatos("Introduzca la segunda posición: "))
                revelarCelda(posicionX, posicionY)
                imprimirTablero()
                if juegoTerminado(posicionX, posicionY) == "has perdido":
                    imprimirTablero(True)
                    print(juegoTerminado(posicionX, posicionY))
                    partida = False
                elif juegoTerminado(posicionX, posicionY) == "has ganado":
                    print(juegoTerminado(posicionX, posicionY))
                    partida = False
                    
            case 2:
                posicionX = int(entradaDeDatos("Introduzca la primera posición: "))
                posicionY = int(entradaDeDatos("Introduzca la segunda posición: "))
                imprimirTablero(marcarCelda(posicionX, posicionY))

            case 3:
                salir()
                partida = False
            case other:
                print("Error introduce un tipo de dato válido")
    print(estadoCeldas)
    print("juego terminado")
if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
