

# def metodo (parametros) --------------------------------------------------------------------------
def suma(num1: float,num2: float) -> float:
    return num1 + num2 # regresar valores/resultado
# def metodo (parametros)
def resta(num1: float, num2: float) -> float:
    return num1 - num2 # regresar valores/resultado

def multiplicar(num1: float, num2: float) ->float:
    return num1 * num2

def dividir(num1: float, num2: float) -> float:
    if num2 == 0:
            print("\nError: No se puede dividir entre cero.\n")
    else:
        resultado = num1 / num2
        print("\nResultado de la division: ",resultado)
        residuo = num1 % num2
        print("\nEl residuo de la divicion: ",residuo,"\n")

def potencia(num1: float, num2: float) -> float:
    print('\nNota: El primer valor es el numero a elevar \ny el segundo la potencia.')
    # Potencia (elevar un numero)
    return num1 ** num2

def mostrar_menu():
    print('\n===== Calculador =====',
      '\n1) suma',
      '\n2) resta',
      '\n3) multiplicar',
      '\n4) dividir',
      '\n5) potencia/elevar nuero'
      '\n0) salir')
    
# bucle - repetir condicional -----------------------------------------------------------------------
while True:
    mostrar_menu() # llamar metodo
    try:
# variables ---------------------------------------------------------------------------------
        op = int(input('Eliga una opcion: '))
        val1 = float(input('\nPrimer número: '))
        val2 = float(input('Segundo número: '))
    except ValueError: 
        print('Eso no es un número. Intente de nuevo...')
        continue # volver al inicio del bucle

# condicional ---------------------------------------------------------------
    if op == 1:
        # almacenar valor y llamar metodo
        resultado = suma (val1,val2) # pasar (variables/parametros)
        print(f'\n{val1} + {val2} =',resultado)
    elif op == 2: 
        # almacenar valor y llamar metodo
        resultado = resta(val1,val2) # pasar (variables/parametros)
        print(f'\n{val1} - {val2} =',resultado)
    elif op == 3: 
        resultado = multiplicar(val1,val2)
        print(f'\n{val1} x {val2} =',resultado)
    elif op == 4:
        resultado = dividir(val1, val2)
        print(f'\n{val1} / {val2} =', resultado)
    elif op == 5:
        resultado = potencia(val1, val2)
        print(f'\n{val1} ^ {val2} =', resultado)
    else:
        print('\nOpcion invalida, cargando...')
        
        