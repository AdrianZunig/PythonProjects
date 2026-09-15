"""
Script para analizar la fortaleza de contraseñas con menú interactivo
"""

import string

def analizar_fortaleza_contrasena(contrasena):
    """Analiza la fortaleza de una contraseña."""
    
    resultados = {
        'contrasena': contrasena,
        'longitud': len(contrasena),
        'tiene_minusculas': False,
        'tiene_mayusculas': False,
        'tiene_numeros': False,
        'tiene_simbolos': False,
        'puntuacion': 0,
        'nivel_fortaleza': '',
        'recomendaciones': []
    }
    
    for caracter in contrasena:
        if caracter in string.ascii_lowercase:
            resultados['tiene_minusculas'] = True
        elif caracter in string.ascii_uppercase:
            resultados['tiene_mayusculas'] = True
        elif caracter in string.digits:
            resultados['tiene_numeros'] = True
        elif caracter in string.punctuation:
            resultados['tiene_simbolos'] = True
    
    puntos_longitud = min(40, len(contrasena) * 2.5)
    
    tipos_caracteres = 0
    if resultados['tiene_minusculas']:
        tipos_caracteres += 1
    if resultados['tiene_mayusculas']:
        tipos_caracteres += 1
    if resultados['tiene_numeros']:
        tipos_caracteres += 1
    if resultados['tiene_simbolos']:
        tipos_caracteres += 1
    
    puntos_variedad = tipos_caracteres * 10
    
    puntos_patrones = 0
    if not (contrasena.isalpha() or contrasena.isdigit()):
        puntos_patrones += 10
    if resultados['tiene_minusculas'] and resultados['tiene_mayusculas']:
        puntos_patrones += 5
    if resultados['tiene_numeros'] and (resultados['tiene_minusculas'] or resultados['tiene_mayusculas']):
        puntos_patrones += 5
    
    resultados['puntuacion'] = min(100, puntos_longitud + puntos_variedad + puntos_patrones)
    
    if resultados['puntuacion'] >= 80:
        resultados['nivel_fortaleza'] = "MUY FUERTE"
    elif resultados['puntuacion'] >= 60:
        resultados['nivel_fortaleza'] = "FUERTE"
    elif resultados['puntuacion'] >= 40:
        resultados['nivel_fortaleza'] = "MODERADA"
    elif resultados['puntuacion'] >= 20:
        resultados['nivel_fortaleza'] = "DÉBIL"
    else:
        resultados['nivel_fortaleza'] = "MUY DÉBIL"
    
    if len(contrasena) < 8:
        resultados['recomendaciones'].append("Aumentar la longitud a al menos 8 caracteres")
    if not resultados['tiene_mayusculas']:
        resultados['recomendaciones'].append("Incluir letras mayúsculas")
    if not resultados['tiene_numeros']:
        resultados['recomendaciones'].append("Incluir números")
    if not resultados['tiene_simbolos']:
        resultados['recomendaciones'].append("Incluir símbolos (!@#$%^&*, etc.)")
    
    return resultados

def mostrar_resultados(resultados):
    """Muestra los resultados del análisis."""
    
    print("\n" + "="*50)
    print(f"ANÁLISIS DE CONTRASEÑA: {resultados['contrasena']}")
    print("="*50)
    
    print(f"Longitud: {resultados['longitud']} caracteres")
    print(f"Minúsculas: {'Sí' if resultados['tiene_minusculas'] else 'No'}")
    print(f"Mayúsculas: {'Sí' if resultados['tiene_mayusculas'] else 'No'}")
    print(f"Números: {'Sí' if resultados['tiene_numeros'] else 'No'}")
    print(f"Símbolos: {'Sí' if resultados['tiene_simbolos'] else 'No'}")
    
    print(f"\nPuntuación: {resultados['puntuacion']}/100")
    print(f"Nivel: {resultados['nivel_fortaleza']}")
    
    if resultados['recomendaciones']:
        print("\nRecomendaciones:")
        for i, rec in enumerate(resultados['recomendaciones'], 1):
            print(f"  {i}. {rec}")
    
    print("="*50)

def mostrar_ejemplos():
    """Muestra ejemplos predefinidos."""
    
    print("\nEJEMPLOS DE CONTRASEÑAS")
    print("="*50)
    
    ejemplos = [
        ("holamundo", "8 minúsculas"),
        ("Python123ABC", "12 chars: mayúsculas, minúsculas, números"),
        ("P@ssw0rd!Seguro#", "16 chars: con símbolos"),
        ("123", "Contraseña débil")
    ]
    
    for contrasena, descripcion in ejemplos:
        print(f"\n{descripcion}:")
        resultados = analizar_fortaleza_contrasena(contrasena)
        mostrar_resultados(resultados)

def main():
    """Función principal con menú interactivo."""
    
    print("="*50)
    print("ANALIZADOR DE FORTALEZA DE CONTRASEÑAS")
    print("="*50)
    
    while True:
        print("\nMENÚ PRINCIPAL:")
        print("1. Analizar una contraseña")
        print("2. Ver ejemplos predefinidos")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            contrasena = input("Ingrese la contraseña a analizar: ").strip()
            if contrasena:
                resultados = analizar_fortaleza_contrasena(contrasena)
                mostrar_resultados(resultados)
            else:
                print("Error: No ingresó ninguna contraseña.")
        
        elif opcion == "2":
            mostrar_ejemplos()
        
        elif opcion == "3":
            print("\n¡Gracias por usar el analizador! Hasta luego.")
            break
        
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

# Este es el punto de entrada del programa
if __name__ == "__main__":
    main()