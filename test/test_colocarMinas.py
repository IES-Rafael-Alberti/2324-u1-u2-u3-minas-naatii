from src.minas import *
def test_MinasColocadasCorrectamente():
    colocarMinar()
    assert len(listaMinas) == NUMERODEMINAS