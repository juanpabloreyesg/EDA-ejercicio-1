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
from DISClib.ADT import list as lt
assert cf
import time

"""
En el modelo, se crean las estructuras de datos, es decir,
las variables donde se van a guardar los datos leidos de los
archivos CSV.

El modelo debe ser el unico sitio donde se modifican y manipulan
los datos.
"""


def new_data_structs():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    modelo = {
        "bolsa": None,
    }

    # definicion de estructura
    crear_bolsa(modelo)
    return modelo

def crear_bolsa(modelo):
    '''
    Crea una bolsa vacía en el modelo a partir de la estructura elegida
    args: el modelo que contiene la bolsa
    '''
    #TODO: Crear estructura
    pass

def aniadir_elemento_a_bolsa(modelo, elems):
    '''
    Añade una colección de elementos a la bolsa en el modelo
    args: 
    - el modelo con la estructura de datos
    - una lista de elementos
    retorno:
    - el modelo que contiene la bolsa con los elementos aniadidos
    '''
    
    #TODO: implementar adición de elementos en ciclo a la estructura
    return modelo

def dar_estadisticas(modelo):
    '''
    Retorna un diccionario que contiene la estadística de número de elementos y media de los elementos.
    args:
    - el modelo con la estructura de datos.
    retorno:
    - un diccionario con la información de estadísticas
    '''
    #TODO: Implementar retorno de diccionario de estadísticas

    return None




