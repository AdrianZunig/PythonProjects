import tkinter as tk # Importa la librería tkinter 
from tkinter import ttk # sublibrería ttk para crear interfaces gráficas
# metodo para saludar
def saludar():
    etiqueta_resultado.config(text=f"Hola, {entrada_nombre.get()}!") # actualiza el texto de la etiqueta 

# Crear ventana 
ventana = tk.Tk()
ventana.title("Mi primera interfaz") # encabezado
ventana.geometry("300x200+50+100") # ancho x alto + posicion x + posicion y
# crear ventana2
ventana2 = tk.Tk()
ventana2.title("Bienvenido") # encabezado
ventana2.geometry("300x200+400+100") # ancho x alto + posicion x + posicion y
# Widgets
etiqueta = ttk.Label(ventana, text="         !Bienvenido¡\n¿Quien eres? Ingresa tu nombre:") # etiqueta
etiqueta.pack(pady=10) # espacio entre widgets
# campo de texto
entrada_nombre = ttk.Entry(ventana) # entrada de datos
entrada_nombre.pack(pady=5) # ejspacio entre widgets

boton = ttk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10) # espacio entre widgets

etiqueta_resultado = ttk.Label(ventana2, text="") # etiqueta
etiqueta_resultado.pack(pady=10) # espacio entre widgets

# Mantener la ventana visible
ventana.mainloop()