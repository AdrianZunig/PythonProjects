import yt_dlp 
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Función para descargar audio o video
def descargar_contenido(url, tipo, carpeta="Descargas"):
    """
    Descarga audio o video de YouTube según el tipo seleccionado. 
    :param url: Enlace del video de YouTube
    :param tipo: 'audio' para solo audio, 'video' para video completo
    :param carpeta: Carpeta donde se guardará el archivo
    """
    try: 
        # Crear carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Opciones para descargar solo audio
        if tipo == "audio":
            opciones = {
                'format': 'bestaudio/best', # Descargar el mejor audio disponible
                'outtmpl': f'{carpeta}/%(title)s.%(ext)s', # Guardar música con el título del video
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio', # Usa FFmpeg para extraer el audio
                        'preferredcodec': 'mp3', # Convierte a formato MP3
                        'preferredquality': '192', # Calidad del audio (192 kbps)
                    },
                    {
                        'key': 'FFmpegMetadata', # Inserta metadatos básicos
                    },
                    {
                        'key': 'EmbedThumbnail', 
                        'already_have_thumbnail': False, # Añade la portada del video
                    },
                ],
                'writethumbnail': True, # Descargar thumbnail
            }
        # Opciones para descargar video completo
        elif tipo == "video":  
            opciones = {
                'format': 'bestvideo+bestaudio/best', # Descargar el mejor video y audio disponible
                'outtmpl': f'{carpeta}/%(title)s.%(ext)s', # Guardar video con el título del video
                'merge_output_format': 'mp4', # Combinar video y audio en un solo archivo MP4
                'postprocessors': [
                    {
                        'key': 'FFmpegMetadata', # Inserta metadatos básicos
                    },
                    {
                        'key': 'EmbedThumbnail', # Añade la portada del video
                        'already_have_thumbnail': False, 
                    },
                ],
                'writethumbnail': True, # Descargar thumbnail
            }
        else:
            raise ValueError("Opción no válida. Debe ser 'audio' o 'video'.") # Manejo de errores

        # Iniciar la descarga
        with yt_dlp.YoutubeDL(opciones) as ydl: 
            ydl.download([url]) # Descargar el contenido
        return "¡Descarga completa!👌"
    except Exception as e:
        return f"El link no pertenece a YouTube" # Manejo de errores

# Función que se ejecuta al presionar el botón en la interfaz
def iniciar_descarga(): 
    url = entrada_url.get().strip() # Obtener el enlace del campo de texto
    tipo = opcion_tipo.get() # Obtener el tipo de descarga (audio o video)
    # Validar que el enlace no esté vacío
    if not url:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un enlace de YouTube.")
        return
    # Validar que el enlace sea de YouTube
    if not ("youtube.com" in url or "youtu.be" in url):
        messagebox.showerror("Error", "Solo se permiten enlaces de YouTube.")
        return
    etiqueta_estado.config(text="Descargando, espera por favor...") # Actualizar la etiqueta de estado
    ventana.update() # Actualizar la ventana
    resultado = descargar_contenido(url, tipo) # Llamar a la función de descarga
    etiqueta_estado.config(text=resultado) # Actualizar la etiqueta de estado con el resultado

# Parte de la interfaz gráfica

# Crear ventana principal
ventana = tk.Tk() # Crear ventana
ventana.title("Descargador de Audio y Video") # Encabezado
ventana.geometry("430x320+230+100") # Ancho x alto + posición x + posición y
ventana.minsize(430,320) # tamaño minimo de la ventana
ventana.maxsize(500,400) # tamaño maximo de la ventana
ventana.configure(bg="gray21", bd=0) # Color de fondo y borde

# Estilos personalizados para ttk (todos con fondo igual a la ventana)
style = ttk.Style() 
style.theme_use('clam') # Estilo de tema
style.configure("TLabel", background="gray21", foreground="#ffffff", font=("Segoe UI", 11)) 

style.configure("TRadiobutton", background="gray21",foreground="#ffffff", font=("Segoe UI", 10))
style.map("TRadiobutton",
    background=[('active', "#8F46B1")] # Color de fondo al pasar el mouse
)
style.configure("TFrame", background="gray21")
style.configure("TEntry", fieldbackground="gray21", background="gray21", foreground="#fff")

# Logo opcional (puedes poner la ruta de tu logo .png)
try:
    from PIL import Image, ImageTk
    logo_img = Image.open("logo_youtube.png").resize((60,60))
    logo = ImageTk.PhotoImage(logo_img)
    ttk.Label(ventana, image=logo, background="#f2f2f2").pack(pady=(10,0))
except Exception:
    pass

# Título principal
ttk.Label(ventana, text="Miusic😎", font=("Segoe UI", 16, "bold"), foreground="#b73ce7").pack(pady=(10,5))

# Etiqueta y campo para el enlace
ttk.Label(ventana, text="Pega el enlace del video de YouTube:").pack(pady=(10,2)) # Etiqueta 
entrada_url = tk.Entry(
    ventana,
    width=48,
    font=("Segoe UI", 10), # Fuente del campo de texto
    bg="gray21",         # Color de fondo igual a la ventana
    fg="#fff",           # Color del texto
    insertbackground="#ecddf1"  # Color del cursor
) # Campo de texto
entrada_url.pack(pady=5) # Espacio entre widgets

# Selector de tipo de descarga (audio o video)
opcion_tipo = tk.StringVar(value="audio") # Variable para almacenar la opción seleccionada
frame_opciones = ttk.Frame(ventana) # Crear un marco para las opciones
frame_opciones.pack(pady=10) # Espacio entre widgets
ttk.Label(frame_opciones, text="¿Qué deseas descargar?").pack(side=tk.LEFT, padx=5) 
ttk.Radiobutton(frame_opciones, text="Audio (mp3)🎶", variable=opcion_tipo, value="audio").pack(side=tk.LEFT, padx=5)
ttk.Radiobutton(frame_opciones, text="Video (mp4)🎬", variable=opcion_tipo, value="video").pack(side=tk.LEFT, padx=5)

# Botón para iniciar la descarga
boton_descargar = ttk.Button(ventana, text="Descargar📲", command=iniciar_descarga, style="TButton") # Crear botón
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", 
    font=("Segoe UI", 11, "bold"),
    foreground="#0c0a0a",      # Color del texto del botón
    background="#b73ce7"       # Color de fondo del botón
)
style.map("TButton",
    foreground=[('active', '#ffffff')], # Color del texto al pasar el mouse
    background=[('active', "#8b29b9")] # Color de fondo al pasar el mouse
)
boton_descargar.pack(pady=18, ipadx=10, ipady=3) # Espacio entre widgets

# Etiqueta para mostrar el estado o resultado
etiqueta_estado = ttk.Label(ventana, text="", font=("Segoe UI", 10, "italic"), foreground="#c1d2dd") # Etiqueta para mostrar el estado
etiqueta_estado.pack(pady=10) # Espacio entre widgets

# Pie de página
ttk.Label(ventana, text="Hecho con ♥ por el Brusco", font=("Segoe UI", 13), foreground="#888").pack(side=tk.BOTTOM, pady=5)

# Iniciar/visualizar la ventana
ventana.mainloop()