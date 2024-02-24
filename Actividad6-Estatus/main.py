import psutil
from tkinter import messagebox
import sys

program_was_started = False
show_negative_message = True
show_positive_message = True
process_list = []

def check_arguments():
    if len(sys.argv) < 2:
        print('No se han ingresado argumentos')
        sys.exit()

def check_process(target):
    global program_was_started, show_negative_message, show_positive_message, process_list
    while True:
        for proc in psutil.process_iter():
            process_list.append(proc.name().lower())
            
        if target.lower() in process_list:
            if show_positive_message:
                print(f'Proceso {target} iniciado')
                show_alert(2)
                program_was_started = True
                show_negative_message = True
                show_positive_message = False
        else:
            if show_negative_message == True:
                if program_was_started:
                    print(f'Proceso {target} Terminado')
                    show_alert(3)
                    show_negative_message = False
                    show_positive_message = True
                    program_was_started = False
                else:
                    print(f'Proceso {target} No Encontrado')
                    show_alert(1)
                    show_negative_message = False
                    show_positive_message = True
        process_list.clear()

def show_alert(number):
    if number == 1:
        messagebox.showwarning("O_O", "Proceso No Encontrado")
    elif number == 2:
        messagebox.showinfo(":D", "Proceso Iniciado")
    elif number == 3:
        messagebox.showinfo(":C", "Proceso Detenido")


if __name__ == '__main__':
    check_arguments()
    target = sys.argv[1]
    check_process(target)