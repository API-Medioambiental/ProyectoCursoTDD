#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:41:19 2019

"""

class Estadisticas:
    
    # Crear datos 
    def __init__(self, so2_media, n_medio_part, no2_media, co_media, o3_media):
        self.so2_media = so2_media
        self.n_medio_part = n_medio_part
        self.no2_media = no2_media
        self.co_media = co_media
        self.o3_media = o3_media
        
    def actualizar_estadisticas(self, indicadores):
        self.so2_media = self.n_medio_part = self.no2_media = self.co_media = self.o3_media = 0
        for indicador in range(len(indicadores)):
            self.so2_media += indicadores[indicador].so2
            self.n_medio_part += indicadores[indicador].part
            self.no2_media += indicadores[indicador].no2
            self.co_media += indicadores[indicador].no2
            self.o3_media += indicadores[indicador].o3
        
        return Estadisticas(self.so2_media, self.n_medio_part, self.no2_media, self.co_media, self.o3_media)
