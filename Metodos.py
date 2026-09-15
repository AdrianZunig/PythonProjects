'''CREACION DE METODOS'''
def valor_entero():
    num1 = int(input("Digite un numero entero: ")) # entrda de datos
    return num1    
         
def valor_decimal():
    num2 = float(input("Digite un numero decimal: ")) # entrada de datos
    return num2

def binario():
    # convertir numero a binario
    print("\n====== NUMERO A BINARIO ======\n")
    num1 = valor_entero() # llamar metodo valor_entero y obtener el valor retornado (num1)
    num1 = bin (num1) # Convertir a binario
    print("El valor del numero a binario es: ",num1)                     
    
def redondear():
    print("\n====== REDONDEAR UN VALOR ======\n")
    num2 = valor_decimal() # llamar metodo valor_decimal y obtener el valor retornado (num2)
    print("El valor redondeado es: ",round(num2)) # round (redondear decimal)

def main():
    while True: # Bucle mostrar el menu hasta que el usuario decida salir
        try: # manejo de Error
            print("\n======= Binevenido =======\n",
                "1) Numnero a binario\n",
                "2) Redondear decimal\n",
                "0) Salir\n"
                )
            
            # Entrada de datos
            num1 = valor_entero() # llamar metodo valor_entero y obtener el valor retornado (num1)
            opcion = num1 # Guardar el valor de num1 en la variable opcion para usar

            # CONDICIONAL       
            if opcion == 1:
                binario() # llamar metodo1
            elif opcion == 2:
                redondear() # llamar metodo2
            elif opcion == 0:
                print("Saliendo del programa...\n")
                break # salir del bucle
            else:
                 print('Opcion no encontrada, cargando...')

        except ValueError: # capturar Error
             print('Error: entrada invalida, cargando...')
             #return # salir de la funcion

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__": 
    main() # Ejecutar la función principal del programa