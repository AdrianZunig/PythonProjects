import nltk
import ssl

# Configurar SSL para evitar errores
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Descargar datos de NLTK solo si no existen
try:
    nltk.data.find('tokenizers/punkt_tab')
    print("✅ Datos NLTK ya descargados")
except LookupError:
    print("📥 Descargando datos NLTK (primera vez, puede tardar)...")
    nltk.download('punkt_tab', quiet=False)
    print("✅ Datos NLTK descargados!")

from nltk.tokenize import word_tokenize

# Palabras clave expandidas
palabras_clave = [
    # Español
    "roto", "rota", "rotos", "rotas",
    "dañado", "dañada", "dañados", "dañadas",
    "sucio", "sucia", "sucios", "sucias",
    "no funciona", "no sirve", "falla", "fallando",
    "descompuesto", "descompuesta", "averiado", "averiada",
    "lento", "lenta", "lentos", "lentas",
    "manchado", "manchada", "rayado", "rayada",
    "quemado", "quemada",
    
    # Inglés (por si acaso)
    "broken", "damaged", "dirty", "not working", 
    "slow", "cracked", "stained", "malfunctioning"
]

def extraer_palabras_clave(texto):
    if not texto or not texto.strip():
        return []
    
    texto = texto.lower().strip()
    
    # 1. Tokenizar
    tokens = word_tokenize(texto)
    
    # 2. Buscar palabras individuales
    encontradas = []
    for palabra in tokens:
        if palabra in palabras_clave:
            encontradas.append(palabra)
    
    # 3. Buscar frases de 2 palabras
    palabras_texto = texto.split()
    for i in range(len(palabras_texto) - 1):
        frase = f"{palabras_texto[i]} {palabras_texto[i+1]}"
        if frase in palabras_clave and frase not in encontradas:
            encontradas.append(frase)
    
    return list(set(encontradas))  # Eliminar duplicados

# Función de prueba
if __name__ == "__main__":
    print("=== PRUEBA PLN ===")
    texto = input("Escribe un problema (ej: 'la laptop está rota'): ")
    claves = extraer_palabras_clave(texto)
    print(f"\n🔑 Palabras clave encontradas: {claves}")