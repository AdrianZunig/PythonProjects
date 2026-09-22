import yt_dlp
import os

# Metodo
def descargar_musica(url,carpeta="Songs"): # pasamos parametros
    try:# manejo de Errores
        if not os.path.exists(carpeta): # Crear carpeta si esta no existe
            os.makedirs(carpeta)

        # Descargar contenido (solo audio)
        opciones = {
            'format' : 'bestaudio/best',# audio en la mejor calida disponible
            'outtmpl' : f'{carpeta}/%(title)s.%(ext)s', # guardar musica con titulo del video
            'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extraer el audio
                'preferredcodec': 'mp3',  # Convierte a formato MP3
                'preferredquality': '192',  # Calidad del audio (192 kbps)
            },
            {  # Añade metadatos
                'key': 'FFmpegMetadata',  # Inserta metadatos básicos
            },
            {  # Añade la portada del video
                'key': 'EmbedThumbnail',  # Requiere ffmpeg
                'already_have_thumbnail': False,
            },
        ],
        'writethumbnail': True,  # Descargar thumbnail
        }
        print("Descargando audio de youtube...\n")
        
        # iniciar descarga de la url 
        with yt_dlp.YoutubeDL(opciones) as ydl: 
            ydl.download([url])
            print("Descarga completa!!!\n")
        
    # capturando Error
    except Exception as e:
        print(f"ocurrio un error : {e}")
        
if __name__ == "__main__":
    while True:
        url = input("\nPege su enlace del video: ") # entrada de datos 
        descargar_musica(url) # llamar metodo (pasar variable)
        opcion = input("¿Desea descargar otra canción? (s/n): ").lower() # opcion para repetir
        if opcion != 's': # si la opcion es diferente a 's' salir del programa
                print("Saliendo del programa...")
                break # salir del bucle

'''
Actualizacion de "yt_dlp"
 
    ingresar a terminal = ctrl+Mayus+ñ
    ejecutar comando = pip install -U yt-dlp
    vereficar instalacion = yt-dlp --version

    NOTA: la actualización de "yt_dlp" puede ayudar a solucionar errores si el codigo 
    no descarga el audio.
'''