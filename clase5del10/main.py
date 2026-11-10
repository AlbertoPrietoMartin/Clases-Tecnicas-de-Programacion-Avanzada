class GestorTareas:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.tareas = []
        return cls._instancia

    def agregar(self, tarea: Tarea)->None:
        self.tareas.append(tarea)

class Tarea:
    def __init__(self, titulo: str, categoria: str):
        self.titulo = titulo
        self.categoria = categoria

    def crear_tarea(tipo: str, titulo: str, adicional: str)->Tarea:
        fabricas = {
            "persoanal": lambda t, a: TareaPersonal(t, a),
            "trabajo": lambda t, a: TareaTrabajo(t, a),
            "estudio": lambda t, a: TareEstudio(t, a),
            "recurrente": lambda t, a: TareaRecurrente(t, a),
            "salud": lambda t, a: TareaSalud(t, a),
        }
        return fabricas[tipo](titulo, adicional)

class TareaBuilder:
    def __init__(self, titulo: str):
        self._tarea = Tarea(titulo, categoria="personal")
        self._tarea.subtareas = []
        self._tarea.etiquetas = []
        self._tarea.fecha = -1
    def con_categoria(self, categoria: str) -> "TareaBuilder":
        self._tarea.categoria = categoria
        return self
    def con_subtarea(self, descripcion: str) -> "TareaBuilder":
        self._tarea.subtareas.append(descripcion)
        return self
    
    def con_fechalimite(self, nuevaFecha: int)->TareaBuilder:
        self._tarea.fecha = nuevaFecha
        return self
    
    def construir(self) -> Tarea:
        return self._tarea
    
tarea = (
    TareaBuilder("Preparar entrega")
    .con_categoria("trabajo")
    .con_subtarea("Redactar informe")
    .con_subtarea("Revisar rúbrica")
    .con_fecha(5)
    .construir() #lo ultimo   
)

gestor1 = GestorTareas()
gestor2 = GestorTareas()

print(id(gestor1))
print(id(gestor2))
print(gestor1 is gestor2)