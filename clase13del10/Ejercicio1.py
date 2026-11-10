class TareaPersonal:
    def __init__(self, lugar: str, proyecto: str, asignatura: str):
        self.lugar = lugar
        self.proyecto = proyecto
        self.asignatura = asignatura
        
class TareaTrabajo:
    def __init__(self, lugar: str, proyecto: str, asignatura: str):
        self.lugar = lugar
        self.proyecto = proyecto
        self.asignatura = asignatura

class TareaEstudios:
    def __init__(self, lugar: str, proyecto: str, asignatura: str):
        self.lugar = lugar
        self.proyecto = proyecto
        self.asignatura = asignatura

#no es necesario q sea una clase
class FactoryMethod:
    def crear_tarea(tipo, titulo, dato):
        if tipo == "personal":
            return TareaPersonal(titulo, dato)
        elif tipo == "trabajo":
            return TareaTrabajo(titulo, dato)
        elif tipo == "estudio":
            return TareaEstudios(titulo, dato)
        else:
            raise ValueError("Error tarea no asignada")

#Ejercicio 2
class Producto:
    def __init__(self):
        pass

class Agotado:
    def __init__(self, productos: ust[Producto]):
        self. productos = productos
        self.indice = 0

    def __iter__ (self):
        return self

    def __next__(self):
        while self.indice < len(self.productos):
            productos = self.productos[self.indice]
            self.indice += 1
            if productos.stock == 0:
                return productos
            
        raise StopIteration

class Articulo:
    def __init__(self):
        pass

class AtriculoDestacado:
    def __init__(self, atriculo: Articulo):
        self.articulo = articulo

    def resumen(self):
        newstr = "*"
        newstr += self.articulo.resumen()
        return newstr

