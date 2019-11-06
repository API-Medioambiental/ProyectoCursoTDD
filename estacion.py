#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:41:46 2019
"""
from estadisticas import actualizar_estadisticas
import math

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
    
    # Asumimos que en el argumento se encuentran solo seis elementos correspondientes
    # a las seis columnas de la web de datos medioambientales.
    # Cada fila tiene 6 columnas: fecha, so2, part, no2, co, o3.
    def aniadir_nuevos_indicadores(self, nuevos_indicadores):
        if nuevos_indicadores.fecha_hora == None:
            return 'Dato no valido'
        else: 
            self.indicadores.append(nuevos_indicadores)
            return 'Dato valido'
    
    # Los datos estadísticos comparten la misma estructura que los indicadores
    # exceptuando la fecha.
    # Cada fila tiene 5 columnas: la media de so2, part, no2, co, o3.
    def generar_estadisticas(self):
        nuevas_estadisticas = actualizar_estadisticas(self.indicadores[:,1], 
             self.indicadores[:,2], self.indicadores[:,3], self.indicadores[:,4],
             self.indicadores[:,5])
        if (math.isnan(nuevas_estadisticas)):
            return 'Estadísticas incorrectas'
        else:
            self.datos_estadisticos.append(nuevas_estadisticas)
            return 'Estadísticas correctas'

        
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
