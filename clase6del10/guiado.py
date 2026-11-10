class Tarea:
    def __init__(self, titulo, descripcion, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad

class TareaConEtiquetas:
    def __init__(self, tarea: Tarea, etiquetas: list[str]):
        self._tarea = tarea
        self.etiquetas = etiquetas

    @property
    def tarea(self):
        return self._tarea

    def __getattr__(self, nombre):
        return getattr(self._tarea, nombre)

    def resumen(self)->str:
        base = f"[{self._tarea.categoria}] {self._tarea.titulo}"
        return base + f"({', '.join(self.etiquetas)})"

miTarea = Tarea("test")
miEtiqueta = TareaConEtiquetas(miEtiqueta, "etiqueta")
print(miEtiqueta.tarea.titulo) 

miTarea2 = Tarea({"titulo": "test", "descripcion": "esto es un test", "prioridad": 2})