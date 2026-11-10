class Tarea():

    def __init__(self, titulo, descripcion, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "pendiente"

    def mostrar(self):
        print(f"Titulo: {self.titulo} Descripcion: {self.descripcion} Prioridad: {self.prioridad} y Estado: {self.estado}")

    def completar(self):
        self.estado = "finalizada"

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor):
        if 1 <= valor <= 5:
            self._prioridad = valor
        else:
            print("La prioridad debe estar entre 1 y 5")