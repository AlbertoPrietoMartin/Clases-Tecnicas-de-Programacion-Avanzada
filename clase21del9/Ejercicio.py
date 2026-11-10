from abc import ABC, abstractmethod

class Tarea:
    def __init__(self, titulo, prioridad):
        self.titulo = titulo
        self.prioridad = prioridad

    def resumen(self):
        return f"[Prioridad: {self.prioridad}] Titulo: {self.titulo}"

class Personal(Tarea):
    def __init__(self, titulo, prioridad, lugar):
        super().__init__(titulo, prioridad)
        self.lugar = lugar  

    def resumen(self): 
      return f"{self.resumen()} Lugar: {self.lugar}"

class Trabajo(Tarea):
    def __init__(self, titulo, prioridad, proyecto):
        super().__init__(titulo, prioridad)
        self.proyecto = proyecto  

    def resumen(self): 
      return f"{self.resumen()} Proyecto: {self.proyecto}"

class Estudio(Tarea):
    def __init__(self, titulo, prioridad, asignatura):
        super().__init__(titulo, prioridad)
        self.asignatura = asignatura  

    def resumen(self): 
      return f"{self.resumen()} Asignatura: {self.asignatura}"

class TareaAbstracta(ABC):
    @abstractmethod
    def resumen(self):
        pass
"""
class Tarea(TareaAbstracta):
        def __init__(self, titutlo, prirodiad):
        self.titulo = titulo
        self.prioridad = prioridad

    def resumen(self):
        return f"[Prioridad: {self.prioridad}] Titulo: {self.titulo}"
"""
    

miTarea = Tarea("Recoger", 3)

print(miTarea.resumen())