import threading
import time

contador = 0
bloqueo = threading.Lock()
miBloqueo = False

def incrementar():
    global contador
    for _ in range(10000):
        if miBloqueo:
            actual = contador
            time.sleep(0.00001)
            contador = actual + 1
            miBloqueo = False
        else:
            miBloqueo = True
            
hilos = [threading.Thread(target = incrementar) for _ in range(2)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()
print(contador)