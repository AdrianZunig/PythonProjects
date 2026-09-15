
# GENERADOR DE CONTRASEÑAS
def gene_pasword():
    import string # utilizar distintos caracteres
    import random # generador aleatorio de datos
    print('\n============ Generador de contraseñas ==================')
    
    longitud = int (input('\nDigite el numero para la longitud de la contraseña: '))
    
    caracteres = string.ascii_letters + string.digits # letras M/m + numeros
    # metodo ''.join (concatenar)
    contraseña = ''.join(random.choice(caracteres) # random (forma aleatoria caracteres)
                        # bucle for, rango de contraseña
                        for i in range (longitud) # i = 0
                        )
    print('\nLa contraseña genera es:', contraseña)
    
# bucle, repetir el progrograma
while True:
    try: # manejo de errores
        gene_pasword()

        opcion = input("\n¿Desea salir? (si/no): ").lower() # lower() convierte a minusculas
        # condicional
        if opcion != 'no': # si la opcion es diferente a 'no' salir del programa
            print("Saliendo del programa...\n")
            break # salir del bucle

    except ValueError: # caapturar Error
        print('Error: entrada invalida, cargando...')
