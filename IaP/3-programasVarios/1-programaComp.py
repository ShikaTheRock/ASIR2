import tkinter as tk
from tkinter import *

def clean():
    # Busca todos los elementos dibujados directamente en la ventana y los destruye
    for elemento in ventana.winfo_children():
        elemento.destroy()

def menu1():
    clean()

    # title del menu
    etiqueta = tk.Label(ventana, text="Menú Principal", font=("Arial", 14))
    etiqueta.pack(pady=20)

    # Crear el primer 
    boton1 = tk.Button(ventana, text="Opción 1", command=lang, width=15, bg="lightblue")
    boton1.pack(pady=5)

    # Crear el segundo 
    boton2 = tk.Button(ventana, text="Opción 2", command=star, width=15, bg="lightgreen")
    boton2.pack(pady=5)

    # Crear el tercer0
    boton2 = tk.Button(ventana, text="Opción 3", command=starstairs, width=15, bg="lightyellow")
    boton2.pack(pady=5)

    #  para cerrar la app
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, width=15, bg="lightcoral")
    boton_salir.pack(pady=5)

def lang():
    clean()

    etiqueta = tk.Label(ventana, text="Menu2", font=("Arial", 14))
    etiqueta.pack(pady=20)

    # Crear el primer 
    boton1 = tk.Button(ventana, text="Castellano", command=menu1, width=15, bg="lightblue")
    boton1.pack(pady=5)

    # Crear el segundo 
    boton2 = tk.Button(ventana, text="Valenciano", command=menu1, width=15, bg="lightgreen")
    boton2.pack(pady=5)

    #  para cerrar la app
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, width=15, bg="lightcoral")
    boton_salir.pack(pady=5)


def star():
    print("Has presionado el  2")

def starstairs():
    print("Has presionado el  2")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú con botones")
ventana.geometry("300x300")
ventana.resizable(False, False)

menu1()



# Mantener la ventana abierta
ventana.mainloop()