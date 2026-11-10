import random

alumnos=[]

alumnos.append("Maria")
alumnos.append("José")

print(alumnos)

for alumno in alumnos:
    print(alumno)

#uno enseña todo del tirón y otro de uno a uno o los que tu quieras meterle

for i in range(5):
    nombre = input("Dame un nombre ")
    alumnos.append(nombre)

print(alumnos)

#del 0 al 10
num = random.randint(0, 10)

eleccion = 0

while eleccion != num:
    eleccion = int(input("Mete un numero "))
    if eleccion <= 10 and eleccion >= 0:
        if eleccion == num:
            print("ACERTASTE")
            break
        elif eleccion > num:
            print("Menor")
        else:
            print("Mayor")
    else:
        print("Error")
        
         
tareas= []

for i in range(3):
    miTitulo = input("Dame un titulo ")
    miDescripcion = input("Dame una descripcion ")
    miPrioridad = int(input("Dame una prioridad "))

    while miPrioridad < 1 or miPrioridad > 5:
        #miPrioridad = int(input error) 
    tareas.append({"titulo: ": miTitulo, "descripcion: ": miDescripcion, "prioridad: ": miPrioridad, "estado: ": estado})