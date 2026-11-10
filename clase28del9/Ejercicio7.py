class Tarea:
    contaodr = 0
    def __init__(self, titulo: str, descripcion: str, prioridad: int):
        self.id = Tarea.contaodr
        Tarea.contador += 1
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "pendiente"

def pendientes (tareas: list[Tarea]) -> list[Tarea]:
    pendientes[]
    for tarea in tareas:
        if tarea.estado == "pendiente":
            pendientes.append(tarea)
    return pendientes

tarea = pendientes(mis_tareas, "pendiente")
print(tarea)


listaTareas = [tarea1, tarea2, tarea3]
listaPendientes = pendientes(listaTareas)