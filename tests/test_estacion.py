import estacion

# Test comprobando que da fallo si el campo fecha es nulo
def test_nuevo_dato():
    test_estacion = estacion.Estacion("provincia", "municipio", "estacion", "direccion")
    test_indicador = estacion.Indicador(None, 1, 1, 1, 1, 1)
    assert test_estacion.aniadir_nuevos_indicadores(test_indicador) == 'Dato no valido'

# Test comprobando que se generan correctamente las estadísticas
def test_estadisticas():
    est = estacion.Estacion("Granada", "Granada",
      "Estación Sierra Nevada", "Calle Sierra Nevada")
    indicadores = estacion.Indicador("06/11/2019", 0.5, 256, 25.96, 50.0, 15.89)
    est.aniadir_nuevos_indicadores(indicadores)
    assert est.generar_estadisticas() == 'Estadisticas correctas'
