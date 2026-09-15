import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import os

print("🔄 Cargando modelo MobileNetV2...")
model = MobileNetV2(weights='imagenet')
print("✅ Modelo cargado!")

def reconocer_objeto(ruta_imagen):
    try:
        # Verificar si el archivo existe
        if not os.path.exists(ruta_imagen):
            print(f"❌ Error: El archivo '{ruta_imagen}' NO existe")
            print("   Archivos disponibles:")
            for f in os.listdir('.'):
                if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                    print(f"   - {f}")
            return []
        
        # 1. Cargar imagen
        print(f"📸 Cargando imagen: {ruta_imagen}")
        img = cv2.imread(ruta_imagen)
        
        if img is None:
            print(f"❌ Error: No se pudo leer '{ruta_imagen}'")
            return []
        
        # 2. Redimensionar
        img = cv2.resize(img, (224, 224))
        
        # 3. Preparar para el modelo
        img_array = np.expand_dims(img, axis=0)
        img_array = preprocess_input(img_array)
        
        # 4. Hacer predicción
        print("🔍 Analizando imagen...")
        predicciones = model.predict(img_array, verbose=0)
        
        # 5. Decodificar resultados
        resultados = decode_predictions(predicciones, top=4)[0]
        
        # 6. Formatear salida
        objetos_detectados = []
        print("\n🎯 OBJETOS DETECTADOS:")
        for i, (_, nombre, prob) in enumerate(resultados, 1):
            print(f"   {i}. {nombre}: {prob:.1%}")
            objetos_detectados.append((nombre, float(prob)))
        
        return objetos_detectados
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        return []

if __name__ == "__main__":
    # Prueba automática
    test_img = "laptop1.jpg"
    if os.path.exists(test_img):
        objetos = reconocer_objeto(test_img)
    else:
        print("⚠️  Prueba: No hay laptop1.jpg, probando con otra...")
        # Buscar cualquier imagen
        imagenes = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if imagenes:
            objetos = reconocer_objeto(imagenes[0])
        else:
            print("❌ No hay imágenes en esta carpeta")