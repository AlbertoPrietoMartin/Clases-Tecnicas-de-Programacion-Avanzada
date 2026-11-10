import time
import functools

class Tarea:
    def __init__(self, titulo, tipo):
        self.titulo = titulo
        self.tipo = tipo


def crear_medidor(func):
    total = 0

    @functools.wraps(func)
    def medir():
        nonlocal total
        inicio = time.perf_counter()
        tarea = Tarea("Compra", "Personal")
        fin = time.perf_counter()
        duracion = inicio - fin
        total += duracion
        print(f"La tarea se ha creado en {total}  segs")

        return tarea
    return medir

#@medir_tiempo
def crear_tarea(titulo):
    return Tarea(titulo, "personal")

crearTarea = crear_medidor()
tareas = []
tiempo_total = 0 

for titulo in ["Compra", "Estudiar", "Deporte"]:
    miTarea, tiempo = crearTarea(titulo, "personal")
    tareas.append(miTarea)
    tiempo_total = tiempo

print(f"las tareasse han creado en {tiempo_total} segs")
print(tareas)