import random
import time
import signal
import msvcrt

running = True
task_count = 0

def signal_handler(signum, frame):
    global running
    print('\nSeñal SIGINT recibida (Interrupción de usuario).')
    print('Finalizando tareas antes de salir...')
    clean_up()
    print('Programa finalizado correctamente.')
    running = False

signal.signal(signal.SIGINT, signal_handler)

def perform_task():
    global task_count
    task_count += 1
    random_number = random.randint(000000, 999999)
    print(f'Tarea #{task_count}: Clave Solicitada: {random_number}')

def clean_up():
    print('Limpiando recursos...')
    print(f'Total de tareas realizadas: {task_count}')

print('Iniciando programa. q para interrumpir.')

while running:
    perform_task()
    
    if msvcrt.kbhit():
            key = msvcrt.getch().decode()
            if key == 'q':
                user_input = input('¿Deseas continuar? (s/n): ')
                if user_input.lower() == 'n':
                    print('Finalizando programa bajo solicitud del usuario...')
                    running = False
                else:
                    print('continuando...')

    time.sleep(2)
    
clean_up() 