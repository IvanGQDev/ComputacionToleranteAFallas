"""
Ivan Eduardo Gomez Quintero

Clase Empleado:
Esta clase se encarga de crear un empleado, con los atributos:
    - id: Identificador del empleado
    - nombre: Nombre del empleado
    - apellido: Apellido del empleado
    - edad: Edad del empleado
    - salario: Salario del empleado
    - posicion: Cargo del empleado

    y el metodo __str__ para imprimir los atributos del empleado.
"""

class Empleado:
    def __init__(self, id,nombre, apellido, edad, salario, posicion):
        self.id = id
        self.name = nombre
        self.lastname = apellido
        self.age = edad
        self.salary = salario
        self.position = posicion

    def __str__(self):
        return f'ID: {self.id},Nombre: {self.name}, Apellido: {self.lastname}, Edad: {self.age}, Salario: {self.salary}, Cargo: {self.position}'  

