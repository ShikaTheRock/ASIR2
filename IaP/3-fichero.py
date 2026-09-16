import pygame as pyg

#texto a poner
texto = """Bienvenido a Python
1: Saludo
2: Clase
3: Despedida
"""
#tengo que definir los colores?¿?¿?
white = pyg.Color(255, 255, 255)
black = pyg.Color(0,0,0)
#tamaño ventana
X = 400
Y = 300

pyg.init()

# set el tamaño de pantalla y meter en jna variable
display_surface = pyg.display.set_mode((X, Y))
#set nombre ventana
pyg.display.set_caption('Bienvenido a Python')
# fuente asi hacker
font = pyg.font.Font('/usr/share/fonts/TTF/3270NerdFontMono-Condensed.ttf', 32)

#Bucle para crear un array con todas las lineas
lineas = texto.splitlines()
textos = []
for linea in lineas:
    text = font.render(linea, True, black)
    textos.append(text)


while True:
    #Supuestamente, si pulsas la q se cierra el programa
    #Realmente, si pulsas cualquier tecla se crashea
    #quien cojones me manda a mi a hacer esto
    #DIOS MIO YA FUNCIONA
    keyinput = pyg.key.get_pressed()
    if keyinput is not None:
        if keyinput[pyg.K_q]:
            pyg.quit()
    for event in pyg.event.get(): 
        if event.type == pyg.QUIT:
            # deactivates the pyg library
            pyg.quit()

            # quit el programa.
            quit()

    #para que el fondo sea blanco
    display_surface.fill(white)

    #pega todas las lineas de texto
    y = 50
    for text in textos:
        textRect = text.get_rect(center=(X // 2, y))
        display_surface.blit(text, textRect)
        y += 45
    pyg.display.flip()
