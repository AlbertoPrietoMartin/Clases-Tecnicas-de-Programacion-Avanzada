import copy

#dentro de la funcion
def crear_tarea(tareas:list)->list:
    tarea = {}
    tarea["titulo"] = input("Introduce un titulo: ")
    tarea["descripcion"] = input("Introduce una descripcion: ")
    tarea["prioridad"] = int(input("Introduce una prioridad: "))
    tarea["estado"] = "Bajo"

    tareas.append(tarea)
    return tareas

def mostrar_tarea(tareas:list):
    for tarea in tareas:
        print(tarea)

def calcular_prioridad(tareas:list):

    for tarea in tareas:
        if tarea["prioridad"]<=2 and tarea["prioridad"]>0:
            tarea["estado"]="Bajo"
        elif tarea["prioridad"]==3:
            tarea["estado"]="Media"
        elif tarea["prioridad"]==4:
            tarea["estado"]="Alta" 
        elif tarea["prioridad"]==5:
            tarea["estado"]="Crítica"
        else: 
            print("Error, prioridad debe estar entre 1 y 5")

        print(tarea["estado"])

def duplicar_tareas(tareas: list)->list:   

    return copy.deepcopy(tareas)

def archivar (tareas, archivo=[]):
    for tarea in tareas:
        archivo.append(tarea)
    tareas=[]

#diferencia entre dicc y listas es como accedes a ellos
#dicc["titulo"] y list[0]

#---MAIN---
#fuera de la funcion

print("Bienvenido a mi programa de creacion de tareas")

tareas=[]

"""
miTit = input()
miDescr = input()
miPrio = int(input())

tareas.append({"titulo: ":  miTit, "miDescr: ": miDescr, "miPrio: ": miPrio})
"""

respuesta = 0

while respuesta==0: 
    crear_tarea(tareas)
    calcular_prioridad(tareas)
    mostrar_tarea(tareas)
    duplicar_tareas(tareas)
    print("Quieres repetir la creacion de tarea?? (si=0, no=pulsa otra tecla)" )

    respuesta = int(input())

    if respuesta == 0:
        print("Bienvenido de nuevo a mi programa de creacion de tareas")
    else:
        print("Gracias por usar mi programa de creacion de tareas")
