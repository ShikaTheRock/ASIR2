import tkinter as tk
from tkinter import *

hasstared = 0
star_label = None


def clean():
    global star_label
    star_label = None

    for elemento in ventana.winfo_children():
        elemento.destroy()


def menu1():
    clean()

    etiqueta = tk.Label(ventana, text="Menú Principal", font=("Arial", 14))
    etiqueta.pack(pady=20)

    boton1 = tk.Button(ventana, text="Opción 1", command=lang, width=15, bg="lightblue")
    boton1.pack(pady=5)

    boton2 = tk.Button(ventana, text="Opción 2", command=star, width=15, bg="lightgreen")
    boton2.pack(pady=5)

    boton3 = tk.Button(ventana, text="Opción 3", command=starstairs, width=15, bg="lightyellow")
    boton3.pack(pady=5)

    boton_salir = tk.Button(
        ventana,
        text="Salir",
        command=ventana.destroy,
        width=15,
        bg="lightcoral"
    )
    boton_salir.pack(pady=5)


def lang():
    clean()

    etiqueta = tk.Label(ventana, text="Menu2", font=("Arial", 14))
    etiqueta.pack(pady=20)

    boton1 = tk.Button(ventana, text="Castellano", command=cs, width=15, bg="lightblue")
    boton1.pack(pady=5)

    boton2 = tk.Button(ventana, text="Valenciano", command=va, width=15, bg="lightgreen")
    boton2.pack(pady=5)

    boton_salir = tk.Button(
        ventana,
        text="Salir",
        command=ventana.destroy,
        width=15,
        bg="lightcoral"
    )
    boton_salir.pack(pady=5)


def cs():
    clean()

    etiqueta = tk.Label(ventana, text="")
    etiqueta.pack(pady=10)

    etiqueta = tk.Label(ventana, text="Buenos días", font=("Arial", 14))
    etiqueta.pack(pady=70)

    boton_salir = tk.Button(
        ventana,
        text="Volver",
        command=menu1,
        width=15,
        bg="lightcoral"
    )
    boton_salir.pack(pady=5)


def va():
    clean()

    etiqueta = tk.Label(ventana, text="")
    etiqueta.pack(pady=10)

    etiqueta = tk.Label(ventana, text="Bon dia", font=("Arial", 14))
    etiqueta.pack(pady=70)

    boton_salir = tk.Button(
        ventana,
        text="Volver",
        command=menu1,
        width=15,
        bg="lightcoral"
    )
    boton_salir.pack(pady=5)


def star():
    clean()

    def solo_numeros(texto):
        return texto.isdigit() or texto == ""

    vcmd = ventana.register(solo_numeros)

    entrada = tk.Entry(
        ventana,
        width=40,
        validate="key",
        validatecommand=(vcmd, "%P")
    )

    entrada.pack(padx=20, pady=20)

    entrada.bind("<Return>", linestar)

    entrada.focus()


def linestar(event):
    global hasstared, star_label

    numero = event.widget.get()

    if numero == "":
        return

    numero = int(numero)

    # Si ya había estrellas, las eliminamos
    if star_label is not None:
        star_label.destroy()

    # Creamos las nuevas estrellas
    starrow = "*" * numero

    star_label = tk.Label(
        ventana,
        text=starrow,
        font=("Arial", 14)
    )

    star_label.pack(pady=20)

    hasstared = 1

def starstairs():
    clean()

    def solo_numeros(texto):
        return texto.isdigit() or texto == ""

    vcmd = ventana.register(solo_numeros)

    entrada = tk.Entry(
        ventana,
        width=40,
        validate="key",
        validatecommand=(vcmd, "%P")
    )

    entrada.pack(padx=20, pady=20)

    entrada.bind("<Return>", stairs)

    entrada.focus()


def stairs(event):
    global star_label

    numero = event.widget.get()

    if numero == "":
        return

    numero = int(numero)

    # Borrar las estrellas anteriores
    if star_label is not None:
        star_label.destroy()

    # Crear la escalera
    resultado = ""

    for i in range(1, numero + 1):
        resultado += "*" * i + "\n"

    # Crear el nuevo resultado
    star_label = tk.Label(
        ventana,
        text=resultado,
        font=("Arial", 14),
        justify="left"
    )

    star_label.pack(pady=20)





ventana = tk.Tk()
ventana.title("Menú con botones")
ventana.geometry("300x300")
ventana.resizable(False, False)

menu1()

ventana.mainloop()
