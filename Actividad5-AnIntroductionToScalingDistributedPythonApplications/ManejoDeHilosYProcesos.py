import multiprocessing
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
            print(f"Empleado {nombre} encontrado")
            time.sleep(10)
            return empleado


def agregar_nuevo_empleado(admin, nombre, apellido, edad, salario, cargo):
    empleado_nuevo = Empleado(nombre, apellido, edad, salario, cargo)
    admin.agregar_empleado(empleado_nuevo)



if __name__ == "__main__":
    admin = Administracion()

    proceso = multiprocessing.Process(target=proceso_buscar_empleado, args=(admin.empleados, "Ivan"))

    hilos = []
    for i in range(9):
        demonio = i < 5
        if(i == 7):
            hilo = threading.Thread(target=agregar_nuevo_empleado, args=(admin, f"Ivan", "Gomez", 26, 20000, "Developer"), daemon=demonio)
            print("Ivan Agregado")
        else:
            hilo = threading.Thread(target=agregar_nuevo_empleado, args=(admin, f"Empleado {i}", "Apellido", 30, 25000, "Analista"), daemon=demonio)
        hilos.append(hilo)
        hilo.start()
        print(f"Hilo {i} en proceso")
        time.sleep(0.5)

    print("\n\nIniciar proceso de búsqueda de empleado")
    proceso.start()

    print("\n\nEsperar a que los hilos terminen")
    for hilo in hilos[5:]:
        print(f"Proceso en hilo principal {hilo}")
        hilo.join()
        print(f"Hilo {hilo} terminado")

    proceso.join()
    print("Programa principal terminado")
