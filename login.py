def obtener_credenciales():
    correo = input("Ingrese su correo electrónico: ").strip() # Eliminar espacios 
    contrasena = input("Digite su contraseña: ")
    return correo, contrasena 

def autenticar_usuario(usuarios_db, correo, contrasena):
    if correo not in usuarios_db: # Verificar si el correo existe en la base de datos
        return False # Si el correo no existe, la autenticación falla
    return usuarios_db[correo] == contrasena # La contraseña guardada en el diccionario para ese correo.
#-----------------------------------------------------------------------------------------------------------------------------
def main(): # Función que cordina el flujo del programa
    usuarios_registrados = { # diccionario que simula una base de datos de usuarios con correos y contraseñas
        'usuario1@gmail.com': 'usua1',
        'usuario2@gmail.com': 'usua2',
        'usuario3@gmail.com': 'usua3'
    }
    
    print("\n===== LOGIN =====")
    correo, contrasena = obtener_credenciales() # Guarda los dos valores retornados en dos variables.
    
    if autenticar_usuario(usuarios_registrados, correo, contrasena): # llama a la funcion, (se le pasan los argumentos necesarios) 
        print("\n✓ Bienvenido a su cuenta, ingresando...\n")
    else:
        print("\n✗ La cuenta o contraseña no existe, saliendo...\n")


if __name__ == "__main__": # Verificar si el script se está ejecutando directamente
    main() # Ejecutar la función principal del programa