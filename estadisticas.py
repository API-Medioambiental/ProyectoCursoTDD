#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:41:19 2019

"""

import numpy as np

class Estadisticas:
    
    # Crear datos 
    def __init__(self, so2_media, n_medio_part, no2_media, co_media, o3_media):
        self.so2_media = so2_media
        self.n_medio_part = n_medio_part
        self.no2_media = no2_media
        self.co_media = co_media
        self.o3_media = o3_media
        
    def actualizar_estadisticas(self, so2_datos, part_datos, no2_datos, co_datos, o3_datos):
        self.so2_media = np.mean(so2_datos)
        self.n_medio_part = np.mean(part_datos)
        self.no2_media = np.mean(no2_datos)
        self.co_media = np.mean(co_datos)
        self.o3_media = np.mean(o3_datos)
        return [self.so2_media, self.n_medio_part, self.no2_media, self.co_media, self.o3_media]
        

        
