import threading
import time

def enviar_recordatorio() -> None:
    print(f"Soy: {threading.current_thread().name}")
    time.sleep(5)

hilo = threading.Thread(target = enviar_recordatorio)
hilo2 = threading.Thread(target = enviar_recordatorio)
hilo.start()
print(threading.active_count())
hilo2.start()
print(threading.active_count())
print(f"Soy: {threading.current_thread().name}")
hilo.join()
print(threading.active_count())
hilo2.join()

print(hilo.is_alive())
print(threading.active_count())
print(threading.current_thread().name)
