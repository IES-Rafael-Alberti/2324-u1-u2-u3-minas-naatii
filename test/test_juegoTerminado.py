from src.minas import *
def test_has_perdido():
    # Arrange
    posicionX = 1
    posicionY = 1
    global celdasReveladas, listaMinas, FILAS, COLUMNAS, NUMERODEMINAS
    celdasReveladas = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    listaMinas = [(1, 1)]
    FILAS = 3
    COLUMNAS = 3
    NUMERODEMINAS = 1

    # Act
    assert juegoTerminado(posicionX, posicionY) == None

def test_sigue_el_juego():
    # Arrange
    posicionX = 1
    posicionY = 1
    celdasReveladas = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    listaMinas = [(2, 2)]
    FILAS = 3
    COLUMNAS = 3
    NUMERODEMINAS = 1

    # Act
    assert juegoTerminado(posicionX, posicionY) == None
