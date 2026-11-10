import json

class Tarea:
    def __init__(self, titulo: str, descripcion: str, prioridad: int):
        self.id = Tarea.contaodr
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "pendiente"

tareas = [{"titulo": "informe", "prioridad": 4}]

with open (tareas.json, "w", encoding="ult-8") as file:
    for tarea in tareas:
        myDict = {"titulo:"tarea.titulo, "prioridad": tarea.prioridad}
        json.dump(myDict)

