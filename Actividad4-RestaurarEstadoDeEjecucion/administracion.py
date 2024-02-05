""" 
Ivan Eduardo Gomez Quintero

Clase Administracion:
Esta clase se encarga de administrar los empleados almacenandonos en una lista, 
los metodos que se encuentran en esta clase son:

    - agregar_empleado: Agrega un empleado a la lista de empleados
    - mostrar_empleados: Muestra la lista de empleados
    - eliminar_empleado: Elimina un empleado de la lista de empleados
    - buscar_empleado: Busca un empleado en la lista de empleados
    - guardar_checkpoint: Guarda la lista de empleados en un archivo
    - cargar_checkpoint: Carga la lista de empleados desde un archivo
    - __str__: Imprime la lista de empleados

Con respecto al uso de pickle para guardar y cargar la lista de empleados, el metodo guardar_checkpoint
se llama cada vez que se agrega o elimina un empleado, y el metodo cargar_checkpoint se llama al inicio 
del programa para cargar la lista de empleados desde un archivo, si no se encuentra el archivo de checkpoint
se imprime un mensaje de error y se continua con la ejecucion del programa.

""" 
from empleado import Empleado
import pickle

class Administracion:
    def __init__(self):
        self.__empleados = []

    def agregar_empleado(self):
        print('Ingrese los datos del empleado: ')
        id = self.__empleados.__len__() + 1
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        edad = int(input('Edad: '))
        salario = float(input('Salario: '))
        cargo = input('Cargo: ')
        NewEmpleado = Empleado(id, nombre, apellido, edad, salario, cargo)
        self.__empleados.append(NewEmpleado)

        self.guardar_checkpoint()

    def mostrar_empleados(self):
        if self.__empleados.__len__() == 0:
            print('No hay empleados registrados')
        else:
            for empleado in self.__empleados:
                print(empleado)

    def eliminar_empleado(self, id):
        if self.__empleados.__len__() == 0: 
            print('No hay empleados registrados')
        else:
            for empleado in self.__empleados:
                if empleado.id == id:
                    self.__empleados.remove(empleado)
                    self.guardar_checkpoint()
                else:
                    print('Empleado no encontrado') 

    def buscar_empleado(self, nombre):
        for empleado in self.__empleados:
            if empleado.nombre == nombre:
                return empleado
        return None

    def __str__(self) -> str:
        return "\n".join(map(str, self.__empleados))

    def guardar_checkpoint(self):
        with open('checkpoint_empleados.pkl', 'wb') as file:
            pickle.dump(self.__empleados, file)

    def cargar_checkpoint(self):
        try:
            with open('checkpoint_empleados.pkl', 'rb') as file:
                self.__empleados = pickle.load(file)
        except FileNotFoundError:
            print('No se encontró el archivo de checkpoint')
            pass 

