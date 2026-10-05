
# GENERADOR DE CONTRASEÑAS
def gene_pasword():
    import string # utilizar distintos caracteres
    import random # generador aleatorio de datos
    print('\n============ Generador de contraseñas ==================')
    # manejo de errores
    try:
        longitud = int (input('\nDigite el numero para la longitud de la contraseña: '))
    
        
        caracteres = string.ascii_letters + string.digits # letras M/m + numeros
        # metodo ''.join (concatenar)
        contraseña = ''.join(random.choice(caracteres) # random (forma aleatoria caracteres)
                            # bucle for, rango de contraseña
                            for i in range (longitud) # i = 0
                            )
        print('\nLa contraseña genera es:', contraseña)
    except ValueError: # capturando el error
            print('Error: entrada invalida, cargando...')

def menu():
    print('\n====== Bienvenido =======\n',
              '¿Que desea realizar hoy?\n',
              '1) Generar una contraseña.\n',
              '2) ...')
    try: # manejo de Error
        op = int(input()) # entrda de opcion menu
        return op # retornar valor
    except ValueError: # capturar Error
        print('Error: entrada invalida, cargando...')
       
# bucle, repetir el progrograma
while True:
    op = menu() # retornar valor de metodo menu() y llamar al metodo

    # condicional menu
    if op == 1:
        gene_pasword() # llamar metodo
    elif op == 0:
         print('Saliendo del programa...')
         break # salir del bucle
    else:
        print("Opción no válida, intenta de nuevo.")