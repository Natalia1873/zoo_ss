from app.modelos import Entrada, TipoEntrada, Grupo_Entrada
import pytest

def test_crear_entrada():
    entrada = Entrada(12)
    assert entrada.tipo == TipoEntrada.NIÑO
    assert entrada.precio == 14

    entrada = Entrada(35)
    assert entrada.tipo == TipoEntrada.ADULTO
    assert entrada.precio == 23

    entrada = Entrada(70)
    assert entrada.tipo == TipoEntrada.JUBILADO
    assert entrada.precio == 18

    entrada = Entrada(1)
    assert entrada.tipo == TipoEntrada.BEBE
    assert entrada.precio == 0

def test_crear_entrada_edad_negativa_error():
    with pytest.raises(ValueError):
        Entrada(-2)    
    
    """ try:
        entrada = Entrada(-2)
        assert False, "No ha saltado ValueError"
    except ValueError:
        assert True """


def xtest_crear_entrada_edad_centenario_error():
    pass  

def test_crear_grupo_entradas():
    grupo = Grupo_Entrada()
    assert grupo.total == 0
    assert grupo.num_entradas == 0

def test_anyadir_entradas_a_grupo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(35)
    assert grupo.num_entradas == 1
    assert grupo.total == 23

    grupo.add_entrada(12)
    assert grupo.num_entradas == 2
    assert grupo.total == 37

    grupo.add_entrada(70)
    assert grupo.num_entradas == 3
    assert grupo.total == 55

    grupo.add_entrada(2)
    assert grupo.num_entradas == 4
    assert grupo.total == 55

def test_cantidad_entradas_por_tipo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(10)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.NIÑO) == 1

    grupo.add_entrada(36)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.ADULTO) == 1

    grupo.add_entrada(13)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.ADULTO) == 2
    
    
def test_subtotal_por_tipo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(10)
    assert grupo.subtotal_tipo(TipoEntrada.NIÑO) == 14


   