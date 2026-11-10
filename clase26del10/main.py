import tkinter as tk
from tkinter import messagebox

def borrar_tarea():
    seleccion = lista_tareas.curselection()
    if not seleccion:
        return
    confirmar = messagebox.askyesno(
    "Confirmar", "¿Eliminar la tarea seleccionada?"
    )
    if confirmar:
        lista_tareas.delete(seleccion[0])

def mostrar_error(mensaje: str) -> None:
    messagebox.showerror("Error", mensaje)

def crear_tarea():
    titulo = entrada.get()
    prioridad = entrada2.get()
    lista_tareas.insert(tk.END, f"{titulo} con prioridad {prioridad}")
    entrada.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    print(completada_var.get())

def doble_click(evento):
    seleccion = lista_tareas.curselection()
    if seleccion:
        print(f"Elemento: {lista_tareas.get(seleccion)}")
        borrar_tarea()

ventana = tk.Tk()
ventana.title("Gestor de tareas")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Titulo de la tarea")
etiqueta.pack(side=tk.TOP, fill=tk.X,pady=5)

entrada = tk.Entry(ventana)
entrada.pack(side=tk.TOP, fill=tk.X,pady=5)

etiqueta2 = tk.Label(ventana, text="Prioridad de la tarea")
etiqueta2.pack(side=tk.TOP, fill=tk.X,pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(side=tk.TOP, fill=tk.X,pady=5)

completada_var = tk.BooleanVar(value=False)
Ch_boton = tk.Checkbutton(ventana, text="Completada", variable=completada_var)
Ch_boton.pack(side=tk.LEFT, fill=tk.X,padx=5)

boton = tk.Button(ventana, text="Crear", command=crear_tarea)
boton.pack(side=tk.LEFT, fill=tk.X,padx=5)

lista_tareas = tk.Listbox(ventana)
lista_tareas.pack(side=tk.BOTTOM, fill=tk.BOTH,expand = True)

lista_tareas.bind("<Double-Button-1>", doble_click)
entrada.bind("<Return>", lambda evento: crear_tarea())

ventana.mainloop()
