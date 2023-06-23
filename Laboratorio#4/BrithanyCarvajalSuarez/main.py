def contar_letras_a(cadena):
    return cadena.count('a')

def reemplazar_es(texto):
    return texto.replace('es', 'ES')

def convertir_mayusculas(texto):
    return texto.upper()

while True:
    print("----- MENÚ ---------")
    print("a. Contar letras 'a'")
    print("b. Reemplazar 'es' por 'ES'")
    print("c. Convertir a mayúsculas")
    print("d. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == 'a':
        cadena = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
        cantidad_a = contar_letras_a(cadena)
        print("Cantidad de letras 'a':", cantidad_a)
    elif opcion == 'b':
        texto = input("Ingrese un texto: ")
        texto_modificado = reemplazar_es(texto)
        print("Texto modificado:", texto_modificado)
    elif opcion == 'c':
        texto = input("Ingrese un texto: ")
        texto_mayusculas = convertir_mayusculas(texto)
        print("Texto en mayúsculas:", texto_mayusculas)
    elif opcion == 'd':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
