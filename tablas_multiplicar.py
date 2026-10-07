def tablasMulti():
    try: # manejo de Errores
        print("\n===== Tablas de multiplicar =====")
        # Entrada de datos por consola
        numero = int(input("\ningrese el numero de la tabla a consultar: "))

    except ValueError: # captura Error
        print("\nError: Entrada inválida. Por favor ingrese un número válido.\n")
        return # salir de la funcion
    # Bucle para mostrar la tabla de multiplicar
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}\n")

# ===================== MENU =========================
while True: # Bucle para repetir el programa
    tablasMulti() # llamar metodo
    opcion = input("¿Desea ver otra tabla? (s/n): ").lower() # lower() convierte a minusculas
    # condicional
    if opcion != 's': # si la opcion es diferente a 's' salir del programa
        print("Saliendo del programa...\n")
        break # salir del bucle

