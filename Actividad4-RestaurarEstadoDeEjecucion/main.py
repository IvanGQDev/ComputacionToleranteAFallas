"""
Ivan Eduardo Gomez Quintero

Este archivo se encarga de ejecutar el programa se declara  un objeto de la clase Administracion
y se ejecutan los metodos de la clase Administracion.
"""

from administracion import Administracion

Administracion = Administracion()
print("\n")
Administracion.cargar_checkpoint()
#Administracion.agregar_empleado()
Administracion.mostrar_empleados()
exit()




