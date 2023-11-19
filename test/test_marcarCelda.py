from src.minas import * 

def test_CeldaMarcada():
    # Declarar posiciones
    celdasMarcadas = {(2, 3)}
    posicionX = 2
    posicionY = 3

    # Llamado a la función
    marcarCelda(posicionX, posicionY)

    # Comprobación
    assert (posicionX, posicionY) in celdasMarcadas