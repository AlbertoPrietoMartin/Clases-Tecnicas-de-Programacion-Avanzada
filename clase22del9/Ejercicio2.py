class Tarea:
    def __init__(self, titulo: str, descripcion: str, prioridad: int):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "pendiente"

    @property
    def prioridad(self) -> int:
        return self.__prioridad

    @property
    def estado(self) -> str:
        return self.__estado

    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @prioridad.setter
    def prioridad(self, value: int):
        if value < 1 or value > 5:
            raise ValueError("Error la tarea debe tener una prioridad entre 1-5")
        else:
            self.__prioridad = value

    @estado.setter
    def estado(self, value: str):
        self.__estado = value

    @titulo.setter
    def titulo(self, value: str):
        if value.strip() == "":
            raise ValueError("Error la tarea debe contener un titulo")
        else:
            self.__titulo = value

tarea = Tarea("Titulo", "descripcion", 3)
tarea.prioridad = 4
print(tarea.prioridad)

tarea2 = Tarea("", "AAA", 4)
print(tarea2.titulo)