def contar_letras_a():
    cadena = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
    cantidad = cadena.count("a")
    print("Cantidad de letras 'a':", cantidad)

def reemplazar_es():
    texto = input("Ingrese un valor de texto: ")
    if "es" in texto:
        nuevo_texto = texto.replace("es", "ES")
        print("Texto modificado:", nuevo_texto)
    else:
        print("El texto no contiene 'es'.")

def convertir_a_mayusculas():
    texto = input("Ingrese un valor de texto: ")
    texto_mayusculas = texto.upper()
    print("Texto en mayúsculas:", texto_mayusculas)

while True:
    print("--- Menú ---")
    print("1. Contar letras 'a'")
    print("2. Reemplazar 'es' por 'ES'")
    print("3. Convertir a mayúsculas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        contar_letras_a()
    elif opcion == "2":
        reemplazar_es()
    elif opcion == "3":
        convertir_a_mayusculas()
    elif opcion == "4":
        print("¡Hasta la proxima!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
