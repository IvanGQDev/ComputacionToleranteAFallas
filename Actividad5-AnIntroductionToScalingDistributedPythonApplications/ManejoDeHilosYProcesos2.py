import concurrent.futures
import threading
import time

class Empleado:
    def __init__(self, nombre, apellido, edad, salario, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

class Administracion:
    def __init__(self):
        self.empleados = []
        self.lock = threading.Lock() 

    def agregar_empleado(self, empleado):
        with self.lock:
            self.empleados.append(empleado)
            print(f"Empleado {empleado.nombre}")

    def mostrar_empleados(self):
        with self.lock:
            for empleado in self.empleados:
                print(empleado.nombre, empleado.apellido)
    

def proceso_buscar_empleado(lista_empleados, nombre):
    print("Proceso buscar empleado iniciado")
    for empleado in lista_empleados:
        if empleado.nombre == nombre:
            print(f"Empleado: {nombre} encontrado")
            time.sleep(10)
            return empleado


def agregar_nuevo_empleado(admin, nombre, apellido, edad, salario, cargo):
    empleado_nuevo = Empleado(nombre, apellido, edad, salario, cargo)
    admin.agregar_empleado(empleado_nuevo)


if __name__ == "__main__":
    admin = Administracion()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(9):
            demonio = i < 5
            if(i == 7):
                future = executor.submit(agregar_nuevo_empleado, admin, "Ivan", "Gomez", 26, 20000, "Developer")
                print("Ivan Agregado")
            else:
                future = executor.submit(agregar_nuevo_empleado, admin, f"Empleado {i}", "Apellido", 30, 25000, "Analista")
            futures.append(future)
            print(f"Hilo {i} en proceso")

        proceso = executor.submit(proceso_buscar_empleado, admin.empleados, "Ivan")

        concurrent.futures.wait(futures + [proceso])

    print("Programa principal terminado")