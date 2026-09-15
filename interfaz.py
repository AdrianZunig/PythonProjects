import tkinter as tk # Importa la librería tkinter

ventana = tk.Tk() # Crear ventana
ventana.title("YAP") # encabezado
ventana.geometry("600x400+100+100") # ancho x alto + posicion x + posicion y
ventana.minsize(200,100) # tamaño minimo de la ventana
ventana.configure(bg="bisque4",bd=20) # color de fondo
# ventana.attributes("-alpha", 0.9) # transparencia de la ventana

# contenedor
frame1 = tk.Frame(ventana) # contenedor dentro de la ventana
frame1.configure(width=200, height=200, bg="bisque3",bd=20) # tamaño y color del contenedor
frame1.pack() # contenedor visible

frame2 = tk.Frame(frame1) # contenedor dentro del contenedor
frame2.configure(width=100, height=100, bg="ivory2",bd=5) # tamaño y color del contenedor
frame2.pack() # contenedor dentro del contenedor visible

ventana.mainloop() # Mantener la ventana visible