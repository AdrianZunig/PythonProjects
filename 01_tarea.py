
# =============================== FUNCIONES ============================
def opcion1():
        valor1 = float(input("Digite un numero: "))
        valor2 = float(input("Digite otro numero: "))

        # Validacion para que no se divida entre 0
        if valor1 == 0 or valor2 == 0:
            print("No se puede realizar la operacion, saliendo...")
        else:
            div = valor1 / valor2 # operacion
            print("El resutado de la division es: ",div)
def opcion2():
    edad = int(input("Ingrese su edad: "))
    ingreso = int(input("Digite su ingrso mensual: "))

    if edad >= 16 and ingreso >= 500:
        print("Usted debe atributar impuestos 💸💸")
    else:
        print("Usted no debe atributar impuestos")
def opcion3():
    numero = input("Ingrese un número de 4 dígitos: ")
    # Verificar que tenga exactamente 4 dígitos
    if len(numero) == 4 and numero.isdigit():
        if numero == numero[::-1]:
            print("Capicúa")
        else:
            print("No lo es")
    else:
        print("Error: Debe ingresar exactamente 4 dígitos")
def opcion4():
    # Solicitar datos al usuario
    peso_libras = float(input("Ingrese su peso en libras: "))
    estatura_cm = float(input("Ingrese su estatura en centímetros: "))

    # Conversiones de unidades
    peso_kg = peso_libras * 0.453592  # Convertir libras a kilogramos
    altura_m = estatura_cm / 100       # Convertir centímetros a metros
    # Cálculo del IMC
    imc = peso_kg / (altura_m ** 2)

    # Mostrar resultados
    print("\n" + "=" * 50)
    print(f"Peso en kilogramos: {peso_kg:.2f} kg") # Mostrar con 2 decimales
    print(f"Valor de IMC: {imc:.2f}") # Mostrar con 2 decimales

    # Clasificación del IMC de acuerdo con la OMS
    print("Categoría: ", end="")
    if imc < 16:
        print("Criterio de ingreso")
    elif 16 <= imc < 16.9: # rango
        print("Infrapeso")
    elif 17 <= imc < 18.4: # rango
        print("Bajo peso")
    elif 18.5 <= imc < 24.9: # rango
        print("Peso normal")
    elif 25 <= imc < 29.9:  # rango
        print("Sobrepeso")
    elif 30 <= imc < 34.9: # rango
        print("Obesidad pre-mórbida")
    elif 35 <= imc < 39.9: # rango
        print("Obesidad mórbida")
    elif imc >= 40:
        print("Obesidad hipermórbida")
    print("=" * 50)
def opcion5():
    nume = int(input("Ingrese un numero del 1 a 12: "))
    if nume == 1:
        print("Enero")
    elif nume == 2:
        print("Febrero")
    elif nume == 3:
        print("Marzo")
    elif nume == 4:
        print("Abril")
    elif nume == 5:
        print("Mayo")
    elif nume == 6:
        print("Junio")
    elif nume == 7:
        print("Julio")
    elif nume == 8:
        print("Agosto")
    elif nume == 9:
        print("Septiembre")
    elif nume == 10:
        print("Octubre")
    elif nume == 11:
        print("Noviembre")
    elif nume == 12:
        print("Diciembre")
    else:
        print("El numero ingresado no es valido, saliendo...")
def opcion6():
    # Entrada del número
    numero = input("Ingrese un número de 4 dígitos: ")

    # Verificar que tenga exactamente 4 dígitos
    if len(numero) != 4 or not numero.isdigit():
        print("Error: Debe ingresar un número de 4 dígitos")
    else:
        # Convertir a enteros
        digito1 = int(numero[0])
        digito2 = int(numero[1])
        digito3 = int(numero[2])
        digito4 = int(numero[3])
        
        # Calcular los dos primeros y dos últimos dígitos
        primeros_dos = digito1 * 10 + digito2
        ultimos_dos = digito3 * 10 + digito4
        
        # Verificar si es FELIZ (primeros dos > últimos dos)
        es_feliz = primeros_dos > ultimos_dos
        
        # Verificar si es CRECIENTE (cada dígito > anterior)
        es_creciente = (digito1 < digito2) and (digito2 < digito3) and (digito3 < digito4)
        
        # Clasificar el número según las reglas
        if es_feliz and es_creciente:
            print("MUY FELIZ")
        elif es_feliz:
            print("FELIZ")
        elif es_creciente:
            print("CRECIENTE")
        else:
            print("INFELIZ")    
def opcion7():
    x = int(input("ingrese un valor X: "))
    y = int(input("ingrese un valor Y: "))
    w = int(input("ingrese un valor W: "))

    if x <= w <= y: # rango cerrado
        print("\nEl valor de W esta en el intervalo X y Y")
    else:
        print("\nEl valor de W no esta en el intervalo X y Y")
def opcion8():
    # Solicitar la hora exacta al usuario
    horas = int(input("Ingrese las horas (1-12): "))
    minutos = int(input("Ingrese los minutos (0-59): "))
    segundos = int(input("Ingrese los segundos (0-59): "))
    am_pm = input("¿AM o PM?: ").strip().upper()

    # Validar la entrada
    if horas < 1 or horas > 12 or minutos < 0 or minutos > 59 or segundos < 0 or segundos > 59 or am_pm not in ["AM", "PM"]:
        print("Entrada inválida. Por favor ingrese valores correctos.")
        return

    # Convertir la hora a formato 24 horas
    if am_pm == "AM":
        if horas == 12:
            horas_24 = 0
        else:
            horas_24 = horas
    else: # PM
        if horas == 12:
            horas_24 = 12
        else:
            horas_24 = horas + 12

    # Calcular los segundos transcurridos
    segundos_transcurridos = horas_24 * 3600 + minutos * 60 + segundos

    # Mostrar el resultado
    print(f"Han transcurrido {segundos_transcurridos} segundos en el día hasta esa hora.")

while True: # Bucle mostrar el menu hasta que el usuario decida salir
    # =============================== MENU ============================
    print( "\n======= Binevenido =======\n",
        "Que desea hacer:\n\n",
        "1) Division\n",
        "2) Atributar impuesto\n",
        "3) Capicúa\n",
        "4) El IMC\n",
        "5) Nombre del mes correspondiente\n",
        "6) Numero feliz\n",
        "7) Intervalo cerrado\n",
        "8) Segundos transcurridos\n",
        "0) Salir\n"
        )
    try: # Manejar error
        # Entrada de datos
        opcion = int(input("Digite la opcion: "))
        print("======================================\n")
    except ValueError: # Captura error
        print("Error: Entrada inválida. Por favor ingrese un número válido.\n")
        continue # volver al inicio del bucle

    # Condicional
    if opcion == 1:
        opcion1() # llamar funcion
    elif opcion == 2:
        opcion2() # llamar funcion
    elif opcion == 3:
        opcion3() # llamar funcion
    elif opcion == 4:
        opcion4() # llamar funcion
    elif opcion == 5:
        opcion5() # llamar funcion
    elif opcion == 6:
        opcion6() # llamar funcion
    elif opcion == 7:
        opcion7() # llamar funcion
    elif opcion == 8 :
        opcion8() # llamar funcion
    elif opcion == 0:
        print("Saliendo...\n")
        break # salir del bucle
    else: 
        print("La opcion marcada no es valida, intente de nuevo...\n")
        