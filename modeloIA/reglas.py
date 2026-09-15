def generar_recomendacion(objetos_detectados, palabras_clave):
    """
    Genera recomendaciones basadas en objetos detectados y palabras clave
    """
    # Diccionario de reglas: (objeto, palabra_clave) -> recomendación
    reglas = {
        # Sillas
        ("chair", "roto"): "Reparar o reemplazar la silla",
        ("chair", "rota"): "Reparar o reemplazar la silla",
        ("chair", "dañado"): "Reparar la silla o considerar comprar una nueva",
        ("chair", "sucio"): "Limpiar la silla con productos adecuados",
        
        # Laptops/Computadoras
        ("laptop", "roto"): "Llevar la laptop a servicio técnico",
        ("laptop", "no funciona"): "Revisar conexiones y reiniciar. Si persiste, llevar a soporte",
        ("laptop", "lento"): "Limpiar archivos temporales, desfragmentar disco y agregar más RAM",
        ("computer", "lento"): "Optimizar el sistema, cerrar programas innecesarios",
        
        # Teléfonos
        ("cell phone", "roto"): "Reparar pantalla o considerar reemplazo",
        ("cell phone", "no funciona"): "Cargar batería, reiniciar. Si no, llevar a reparación",
        
        # Libros
        ("book", "roto"): "Reparar con cinta adhesiva o encuadernar",
        ("book", "dañado"): "Preservar en un lugar seco o considerar reemplazo",
        
        # Muebles generales
        ("table", "roto"): "Reparar la mesa o reforzar patas",
        ("desk", "roto"): "Reparar el escritorio",
        
        # Electrodomésticos
        ("mouse", "no funciona"): "Limpiar el sensor, cambiar baterías o reemplazar",
        ("keyboard", "no funciona"): "Limpiar entre teclas, verificar conexión USB",
        ("screen", "roto"): "Reparar o reemplazar la pantalla",
        
        # Objetos varios
        ("bottle", "roto"): "Desechar con cuidado en contenedor de vidrio",
        ("cup", "roto"): "Usar otro vaso y desechar este con cuidado",
        ("car", "no funciona"): "Llamar a un mecánico para diagnóstico",
    }
    
    # Buscar coincidencias
    recomendaciones = []
    
    for objeto_nombre, _ in objetos_detectados:
        objeto_nombre = objeto_nombre.lower()
        
        for palabra in palabras_clave:
            palabra = palabra.lower()
            
            # Buscar coincidencia exacta
            if (objeto_nombre, palabra) in reglas:
                recomendaciones.append(reglas[(objeto_nombre, palabra)])
            
            # Buscar coincidencias parciales
            for regla_objeto, regla_palabra in reglas.keys():
                if regla_objeto in objeto_nombre and regla_palabra in palabra:
                    if reglas[(regla_objeto, regla_palabra)] not in recomendaciones:
                        recomendaciones.append(reglas[(regla_objeto, regla_palabra)])
    
    # Devolver resultados
    if recomendaciones:
        return " | ".join(recomendaciones[:3])  # Máximo 3 recomendaciones
    elif objetos_detectados:
        # Recomendación genérica si hay objetos pero no palabras clave específicas
        return f"Revisar el estado del objeto detectado: {objetos_detectados[0][0]}"
    else:
        return "No se pudo generar una recomendación específica. Verifica la imagen y descripción."

if __name__ == "__main__":
    # Prueba
    objetos_prueba = [("chair", 0.95), ("laptop", 0.87)]
    palabras_prueba = ["roto", "lento"]
    print("Prueba de reglas:")
    print(f"Objetos: {objetos_prueba}")
    print(f"Palabras: {palabras_prueba}")
    print(f"Recomendación: {generar_recomendacion(objetos_prueba, palabras_prueba)}")