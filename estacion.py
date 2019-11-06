#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:41:46 2019
"""
from estadisticas import Estadisticas

### Clase que representa los datos de una determinada localización
class Estacion:
    
    # Crear datos 
    def __init__(self, provincia, municipio, estacion, direccion):
        self.indicadores = []
        self.provincia = provincia
        self.municipio = municipio
        self.estacion = estacion
        self.direccion = direccion
        self.datos_estadisticos = []
    
    # Vector de indicadores
    def aniadir_nuevos_indicadores(self, nuevos_indicadores):
        if nuevos_indicadores.fecha_hora == None:
            return 'Dato no valido'
        else: 
            self.indicadores.append(nuevos_indicadores)
            return 'Dato valido'
    
    # Generar estadísticas de cada medidor 
    def generar_estadisticas(self):
        nuevas_estadisticas = Estadisticas.actualizar_estadisticas(self,
           self.indicadores)
        if nuevas_estadisticas == None:
            return 'Estadisticas no validas'
        else:
            self.datos_estadisticos.append(nuevas_estadisticas)
            return 'Estadisticas correctas'

### Clase que representa la estructura de los datos medioambientales
class Indicador:
    
    # Crear un dato
    def __init__(self, fecha_hora, so2, part, no2, co, o3):
        self.so2 = so2
        self.part = part
        self.no2 = no2
        self.co = co
        self.o3 = o3
        self.fecha_hora = fecha_hora
