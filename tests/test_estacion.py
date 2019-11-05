import pytest
import estacion

def test_nuevo_dato():
    test_estacion = estacion.Estacion("provincia", "municipio", "estacion", "direccion")
    test_indicador = estacion.Indicador(None, 1, 1, 1, 1, 1)
    assert test_estacion.aniadir_nuevos_indicadores(test_indicador) == 'Dato no valido'

def test_estadisticas():
    