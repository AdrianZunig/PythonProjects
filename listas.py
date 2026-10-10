'''
Listas (mutables)
Una lista es una secuencia ordenada y mutable de elementos. 
Se define con corchetes [] y puede contener elementos de distintos tipos.
'''

# Crear listas
frutas = ["manzana", "pera", "uva"]
numeros = [1, 2, 3, 4, 5]
mezclada = [42, "texto", True, None, 3.14]  # tipos distintos
vacia = []

# Acceso por índice (empieza en 0, negativos desde el final)
print(frutas[0])    # manzana
print(frutas[-1])   # uva (último elemento)

# Slicing: [inicio:fin:paso]
print(numeros[1:4])   # [2, 3, 4]
print(numeros[::2])   # [1, 3, 5]  (cada 2 elementos)
print(numeros[::-1])  # [5, 4, 3, 2, 1]  (invertir)

# Modificar listas (son mutables)
frutas.append("mango")          # agregar al final
frutas.insert(1, "cereza")      # insertar en posición 1
frutas.extend(["kiwi", "lima"]) # agregar múltiples al final
frutas.remove("pera")           # eliminar por valor (primera ocurrencia)
del frutas[0]                   # eliminar por índice
ultimo = frutas.pop()           # extraer y eliminar el último

# Consultar listas
print(len(frutas))              # longitud
print("uva" in frutas)          # True — comprueba pertenencia
print(frutas.index("uva"))      # índice de "uva"
print(frutas.count("kiwi"))     # número de ocurrencias

# Ordenar
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2, 6]
numeros_desordenados.sort()              # ordena en el lugar (muta la lista)
ordenada = sorted([3, 1, 2])             # devuelve nueva lista ordenada
