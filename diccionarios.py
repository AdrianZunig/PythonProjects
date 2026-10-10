'''
Diccionarios (key-value)
Un diccionario es una colección de pares clave-valor, optimizada para buscar por clave en O(1). 
Las claves deben ser inmutables (strings, números, tuplas).
'''

# Crear diccionarios
usuario = {
    "nombre": "Ana García", # 'clave: valor'
    "edad": 28,
    "activo": True,
    "puntaje": 1450
}

# Acceso por clave
print(usuario["nombre"])     # Ana García
print(usuario.get("edad"))   # 28

# .get() es más seguro — devuelve None (o un default) si la clave no existe
print(usuario.get("email"))          # None (no lanza KeyError)
print(usuario.get("email", "N/A"))   # "N/A" (valor por defecto)

# Modificar y agregar
usuario["edad"] = 29         # actualizar valor existente
usuario["email"] = "ana@ejemplo.com"  # agregar nueva clave

# Eliminar
del usuario["puntaje"]               # eliminar clave
email = usuario.pop("email")         # extraer y eliminar

# Iterar un diccionario
for clave in usuario:               # itera las claves
    print(clave, usuario[clave])

for clave, valor in usuario.items():  # itera pares
    print(f"{clave}: {valor}")

print(list(usuario.keys()))    # ["nombre", "edad", "activo"]
print(list(usuario.values()))  # ["Ana García", 29, True]

# Diccionario anidado
config = {
    "base_de_datos": {
        "host": "localhost",
        "puerto": 5432,
        "nombre": "mi_app"
    }
}
print(config["base_de_datos"]["puerto"])  # 5432
