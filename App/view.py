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
 * contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 """

import config as cf
import sys
import controller
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""



def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    print("Opciones:")
    print("1- Crear nueva bolsa")
    print("2- Añadir elemento a bolsa")
    print("3- Dar estadisticas de bolsa")
    print("0- Salir")

def crear_bolsa(control):
    '''
    Informa al controlador que se debe crear una bolsa e informa de su creación exitosa
    '''
    #TODO: Completar
    pass

def aniadir_elemento_a_bolsa(control):
    '''
    Solicita al usuario una lista de elementos separados por coma y los envía para ser aniadidos en la bolsa al controlador
    '''
    #TODO: Completar
    pass

def dar_estadisticas_de_bolsa(control):
    '''
    Solicita al controlador las estadísticas de elementos y las muestra por consola
    '''
    #TODO: Completar
    pass


# Se crea el controlador asociado a la vista
control = newController()

# main del ejercicio
if __name__ == "__main__":

    """
    Menu principal
    """
    working = True
    # ciclo del menu
    while working:
        printMenu()
        inputs = input("Seleccione una opción para continuar\n")
        if int(inputs[0]) == 1:
            crear_bolsa(control)
        elif int(inputs[0]) == 2:
            aniadir_elemento_a_bolsa(control)
        elif int(inputs[0]) == 3:
            dar_estadisticas_de_bolsa(control)
        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            print("Opcion erronea, vuelva a elegir.\n")
    sys.exit(0)
