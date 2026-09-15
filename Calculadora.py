# Metodo/ Funcion
def valor_decimal():
    while True: # Bucle hasta que el usuario ingrese valores validos
        try: # manejar error
            # Pedir datos por consola
            num1 = float (input("\ningrese el primer valor: "))
            num2 =float (input("ingrese el segundo valor: "))
            return num1,num2 # Retorna los valores
        except ValueError: # Captura error
            print("\nError: Entrada inválida. Por favor ingrese números válidos.")
def valor_entero():
    while True: # Bucle hasta que el usuario ingrese valores validos
        try: # manejar error
            # Pedir datos por consola
            num3 = int (input("\nDigite la opcion: "))
            return num3 # Retorna el valor
        except ValueError: # Captura error
            print("\nError: Entrada inválida. Por favor ingrese un número válido.")
def suma():
    print("====== Sumar ======")
    num1,num2 = valor_decimal() # llamar metodo
    resultado = num1 + num2
    print("\nResultado de la suma: ",resultado,"\n")

def resta():
    print("====== Restar ======")
    num1,num2 = valor_decimal() # llamar metodo
    resultado = num1 - num2
    print("\nResultado de la resta: ",resultado,"\n")

def multiplicacion():
    print("====== Multiplicar ======")
    num1,num2 = valor_decimal() # llamar metodo
    resultado = num1 * num2
    print("\nResultado de la multiplicacion: ",resultado,"\n")

def division():
    print("====== Division y Residuo ======")
    num1, num2 = valor_decimal() # llamar metodo
    if num2 == 0:
        print("\nError: No se puede dividir entre cero.\n")
    else:
        resultado = num1 / num2
        print("\nResultado de la division: ",resultado)
        residuo = num1 % num2
        print("\nEl residuo de la divicion: ",residuo,"\n")

def potencia():
    print("====== Elevar un numero ======\n" ,
        "Nota: El primer valor es el numero a elevar \ny el segundo la potencia.")
    num1, num2 = valor_decimal() # llamar metodo
    resultado = num1 ** num2 # Potencia (elevar un numero)
    print("\nResultado de la potencia: ",resultado,"\n")
    
def menu():
    print("\n====== CALCULADORA ======")
    # MENU
    print("\n1) Suma",
        "\n2) Resta",
        "\n3) Multiplicacion",
        "\n4) Division y residuo",
        "\n5) Potencia",
        "\n0) Salir")
        
#-----------------------------------------------------------------------------      
def main(): # Función que cordina el flujo del programa
    while True: # Bucle mostrar el menu hasta que el usuario decida salir
        menu() # llamar metodo menu
        try: # manejar error
            # Solicitar opcion para condicion
            num3 = valor_entero() # llamar metodo valor_entero y obtener el valor retornado (num3)
        except ValueError: # Captura error
            print("\nError: Entrada inválida. Por favor ingrese un número válido.")
            continue # volver al inicio del bucle
        if num3 == 1:
            suma()
        elif num3 == 2:
            resta()
        elif num3 == 3:
            multiplicacion()
        elif num3 == 4:
            division()
        elif num3 == 5:
            potencia()
        elif num3 == 0:
            print("\nSaliendo de la calculadora...\n")
            exit() # Salir del programa
        else:
            print("\nError: Opción inválida. Por favor seleccione una opción del menú.\n")
    

if __name__ == "__main__": # Verificar si el script se está ejecutando directamente
    main() # Ejecutar la función principal del programa