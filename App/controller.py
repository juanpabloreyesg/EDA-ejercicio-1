"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 """

import config as cf
import model
import csv
import os


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def crear_bolsa(control):
    '''
    Solicita al modelo crear una nueva bolsa vacía
    '''
    #TODO: Completar
    pass

def aniadir_elemento_a_bolsa(control, elems):
    '''
    Solicita al modelo aniadir una lista de elementos
    '''
    #TODO: Completar
    pass

def dar_estadisticas_de_bolsa(control):
    '''
    Solicita al modelo estadísticas sobre la bolsa
    '''
    #TODO: Completar
    pass