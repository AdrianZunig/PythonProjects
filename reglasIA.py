
def reglas():
    # Definición de hechos y reglas
    hechos = [ 
        "animal(fido)",
        "ladra(fido)",
        "muerde(fido)"
    ]
    reglas = [
        "R1: ladra(x) → canino(x)",
        "R2: canino(x) ∧ muerde(x) → peligroso(x)",
        "R3: peligroso(x) → recomendar(bozal, x)"
    ]
    encadenamiento_adelante = [
        "ladra → canino → muerde → peligroso → recomendar bozal",
        "recomendar(bozal, fido)"
    ]
    encadenamiento_atras = [
        "G0: recomendar bozal",
        "G1: (peligroso(fido) y muerde(fido))",
        "G2: (canino(fido) y ladra(fido))",
    
        "R1 → R2 → R3\n"
    ]

    texto = "\nHECHOS INICIALES (H):\n" + "\n".join("- " + h for h in hechos) # agregar hechos al texto
    texto += "\n\nREGLAS (R):\n" + "\n".join("- " + r for r in reglas) # agregar reglas al texto
    texto += "\n\nENCADENAMIENTO HACIA ADELANTE:\n" + "\n".join(encadenamiento_adelante) # agregar encadenamiento al texto
    texto += "\n\nENCADENAMIENTO HACIA ATRÁS:\n" + "\n".join(encadenamiento_atras)  # agregar encadenamiento al texto

    print(texto) # imprimir el texto

reglas() # llamar a la funcion