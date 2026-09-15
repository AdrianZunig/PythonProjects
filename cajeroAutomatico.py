'''Cajero Automático 
    1) poder depositar, retirar y consultar saldo.
    2) usuario y la contraseña bloqueada después de 3 intentos fallidos.
    3) repetir el menú hasta que el usuario decida salir.
    4) debe ser en inglés.
'''

print("\n====== ATM ======")
# Datos del usuario
usuario1 = 'adrian'
contraseña1 = '123'

# Contador de intentos
intentos = 0
max_intentos = 3

# cantidad de billetes disponibles (fuera del metodo para que no se reinicien)
billetes_1000 = int(10)
billetes_500 = int(10)
billetes_200 = int(10)
billetes_100 = int(10)
billetes_50 = int(10)
billetes_20 = int(10)
billetes_10 = int(10)

# Bucle para permitir hasta 3 intentos de acceso
while intentos < max_intentos: # Condicional

    def retiro():
            # para usar las variables globales dentro del metodo
            global billetes_1000, billetes_500, billetes_200, billetes_100, billetes_50, billetes_20, billetes_10
            # variables para contar los billetes a entregar
            entregar_1000 = int(0)
            entregar_500 = int(0)
            entregar_200 = int(0)
            entregar_100 = int(0)
            entregar_50 = int(0)
            entregar_20 = int(0)
            entregar_10 = int(0)
            # Copiamos los billetes disponibles para trabajar con ellos
            disponibles_1000 = billetes_1000
            disponibles_500 = billetes_500
            disponibles_200 = billetes_200
            disponibles_100 = billetes_100
            disponibles_50 = billetes_50
            disponibles_20 = billetes_20
            disponibles_10 = billetes_10
            # Variable para ir restando la cantidad solicitada
            resto = retirar # cantidad a retirar
            
            # Primero usamos billetes de $1000 (el más grande)
            while resto >= 1000 and disponibles_1000 > 0:
                entregar_1000 += 1
                disponibles_1000 -= 1
                resto -= 1000

            # Luego usamos billetes de $500
            while resto >= 500 and disponibles_500 > 0:
                entregar_500 += 1
                disponibles_500 -= 1
                resto -= 500

            # Luego usamos billetes de $200
            while resto >= 200 and disponibles_200 > 0:
                entregar_200 += 1
                disponibles_200 -= 1
                resto -= 200
            
            # Luego usamos billetes de $100
            while resto >= 100 and disponibles_100 > 0:
                entregar_100 += 1
                disponibles_100 -= 1
                resto -= 100
            # Luego usamos billetes de $50
            while resto >= 50 and disponibles_50 > 0:
                entregar_50 += 1
                disponibles_50 -= 1
                resto -= 50
            # Luego usamos billetes de $20
            while resto >= 20 and disponibles_20 > 0:
                entregar_20 += 1
                disponibles_20 -= 1
                resto -= 20
            # Finalmente usamos billetes de $10
            while resto >= 10 and disponibles_10 > 0:
                entregar_10 += 1
                disponibles_10 -= 1
                resto -= 10

            # Verificamos si pudimos completar el retiro
            if resto == 0:
                # Actualizamos los billetes disponibles
                billetes_1000 -= entregar_1000
                billetes_500 -= entregar_500
                billetes_200 -= entregar_200
                billetes_100 -= entregar_100
                billetes_50 -= entregar_50
                billetes_20 -= entregar_20
                billetes_10 -= entregar_10
                
                # Mostramos el resultado exitoso
                print(f"\n✅ Successful withdrawal: ${retirar}")
                print("Bills delivered:")
                
                # Solo mostramos los billetes que se entregaron
                if entregar_1000 > 0:
                    print(f"- {entregar_1000} bill(s) of $1000")
                if entregar_500 > 0:
                    print(f"- {entregar_500} bill(s) of $500")
                if entregar_200 > 0:
                    print(f"- {entregar_200} bill(s) of $200")
                if entregar_100 > 0:
                    print(f"- {entregar_100} bill(s) of $100")
                if entregar_50 > 0:
                    print(f"- {entregar_50} bill(s) of $50")
                if entregar_20 > 0:
                    print(f"- {entregar_20} bill(s) of $20")
                if entregar_10 > 0:
                    print(f"- {entregar_10} bill(s) of $10")
                '''
                # Mostramos el nuevo saldo
                print(f"\nNew available balance:")
                print(f"- $1000: {billetes_1000} bills")
                print(f"- $500: {billetes_500} bills")
                print(f"- $200: {billetes_200} bills")
                print(f"- $100: {billetes_100} bills")
                print(f"- $50: {billetes_50} bills")
                print(f"- $20: {billetes_20} bills")
                print(f"- $10: {billetes_10} bills")
                '''
            else:
                # No se pudo completar el retiro con los billetes disponibles
                print("\n❌ Unable to process the withdrawal with the available bills.\n")
    
    # entardad de datos por consola
    usuario = input("\nEnter your username: ")
    contraseña = input("Enter your password: ")

    # Verifica si usuario y contraseña son correctos
    if usuario == usuario1 and contraseña == contraseña1:
        
        while True: # mostrar menu hasta que el usuario decida salir
            print("\n==== Welcome to the ATM ====")
            print("\nWhich operation would you like to perform: \n",
              "1) Deposit\n",
              "2) Withdraw\n",
              "3) Check Balance\n",
              "4) Exit\n")
            # manejo de error al maracar opcion inexistente en el menu
            try: 
                opcion = int(input()) # entrada de datos por consola
            except ValueError: # manejo de error si no es un numero
                print("Invalid option. Please try again.")
                continue # vuelve al inicio del bucle
            
            if opcion == 1:
                print("\n====== DEPOSIT ======")
                deposito = float(input("\nEnter the amount: "))
                print("Deposit successful.\n")

            elif opcion == 2:
                print("\n===== WITHDRAW ======")
                retirar = float(input("\nEnter the amount to withdraw: "))
                retiro() # llamar metodo

            elif opcion == 3:
                print("\n===== CHECK BALANCE =====")
                # Mostrar saldo real y dinero disponible en billetes
                total_billetes = (
                    billetes_1000 * 1000 +
                    billetes_500 * 500 +
                    billetes_200 * 200 +
                    billetes_100 * 100 +
                    billetes_50 * 50 +
                    billetes_20 * 20 +
                    billetes_10 * 10
                )
                print(f"\nYour current balance is: ${total_billetes}")
            
            elif opcion == 4:
                print("Exiting ATM...\n")
                break # sale del menu y termina el programa
            else:
                print("Invalid option. Please try again.\n")

        break # Sale del bucle si el usuario y contraseña son correctos

    else:
        intentos += 1 # Incrementa el contador de intentos
        print("Incorrect username or password.")
        if intentos == max_intentos:  # comparando intentos
            print("\nAccount locked.\n")
        
            

