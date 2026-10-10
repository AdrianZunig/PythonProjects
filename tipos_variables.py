'''python permite el tipado dinamico: una misma variable 
   puede contener diferentes tipos de datos. 
'''
print("\n===== TIPO DE DATOS =====") # Imprimir mensaje
valor = input("Ingrese un numero: ") # Solicitar valor input = string
print("\nel valor ingresado es un:",type(valor)) # indica el tipo de dato
print("\nValores ya definidos:") # Imprimir mensaje
valor1 = 1
valor2 = 2.4
cadena = 'hola BB'
valor3 = True

print('-'*40) # Repetir un string con *
print(type(valor1)) # indica el tipo de dato
print(valor1) # imprimir varaiable
print(type(valor2)) # indica el tipo de dato
print(valor2) # imprimir varaiable
print(type(cadena)) # indica tipo de variable
print(cadena) # imprimir variable
print(type(valor3))
print(valor3)# imprimir el valor

print('\n===== Conctenar y repetir un str =====')
# Concatenar strings con +
saludo = "Hola" + ", " + "mundo" + "!"
print(saludo)   # Hola, mundo!

# Repetir un string con *
linea = "-" * 20
print(linea)    # --------------------