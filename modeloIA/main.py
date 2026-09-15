'''Vamos a crear un asistente inteligente que haga dos cosas:
    1 Ver imágenes → Reconocer objetos (ej: silla, teléfono, libro, lámpara).
    2 Leer texto → Entender palabras clave (ej: "roto", "sucio", "no funciona").
    3 Combinar ambas → Dar recomendaciones como: "Si veo una silla rota y leo 'roto', sugiero 'reparar silla'".
=================================================================================================================='''

from vision import reconocer_objeto
from pln import extraer_palabras_clave
from reglas import generar_recomendacion
import os

def mostrar_archivos():
    """Muestra las imágenes disponibles en la carpeta"""
    print("\n📁 IMÁGENES DISPONIBLES:")
    imagenes = []
    for archivo in os.listdir('.'):
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            imagenes.append(archivo)
            print(f"   - {archivo}")
    
    if not imagenes:
        print("   ⚠️  No hay imágenes en esta carpeta")
        print("   Coloca aquí imágenes como 'laptop1.jpg', 'silla.jpg', etc.")
    
    return imagenes

def main():
    print("=" * 50)
    print("       ASISTENTE INTELIGENTE MULTIMODAL")
    print("=" * 50)
    
    # Mostrar archivos disponibles
    imagenes = mostrar_archivos()
    
    if not imagenes:
        print("\n❌ No hay imágenes para analizar.")
        print("   Por favor, coloca una imagen en esta carpeta y vuelve a intentar.")
        return
    
    # 1. SELECCIONAR IMAGEN
    print("\n" + "-" * 50)
    print("1️⃣  MÓDULO DE VISIÓN")
    print("-" * 50)
    
    # Usar la primera imagen por defecto
    ruta_imagen = imagenes[0]
    if len(imagenes) > 1:
        print(f"\nSe usará '{ruta_imagen}' (primera imagen encontrada)")
        print("Si quieres otra, edita el código main.py")
    else:
        print(f"\nAnalizando: {ruta_imagen}")
    
    # Procesar imagen
    objetos = reconocer_objeto(ruta_imagen)
    
    if not objetos:
        print("❌ No se pudieron detectar objetos. Intenta con otra imagen.")
        return
    
    # 2. PROCESAR TEXTO
    print("\n" + "-" * 50)
    print("2️⃣  MÓDULO DE PROCESAMIENTO DE LENGUAJE")
    print("-" * 50)
    
    # Ejemplos de texto para probar
    print("\n💡 Ejemplos para probar:")
    print("   - 'está roto y no funciona'")
    print("   - 'la silla está dañada'")
    print("   - 'sucio y manchado'")
    print("   - 'muy lento'")
    
    texto = input("\n📝 Describe el problema: ")
    
    if not texto.strip():
        texto = "roto"  # Valor por defecto para prueba
        print(f"⚠️  Usando texto por defecto: '{texto}'")
    
    palabras = extraer_palabras_clave(texto)
    print(f"🔑 Palabras clave detectadas: {palabras}")
    
    # 3. APLICAR REGLAS
    print("\n" + "-" * 50)
    print("3️⃣  MÓDULO DE REGLAS INTELIGENTES")
    print("-" * 50)
    
    recomendacion = generar_recomendacion(objetos, palabras)
    print(f"\n💡 RECOMENDACIÓN: {recomendacion}")
    
    print("\n" + "=" * 50)
    print("✅ ANÁLISIS COMPLETADO")
    print("=" * 50)

if __name__ == "__main__":
    main()