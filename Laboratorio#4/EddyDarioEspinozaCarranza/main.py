#PROFE ESTE ES EL LAB 4, ME EQUIVOQUE AL ENVIARLE EL MENSAJE.
def contar_letras_a(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() == 'a':
            contador += 1
    return contador

def reemplazar_texto(texto, buscar, reemplazar):
    return texto.replace(buscar, reemplazar)

def convertir_mayusculas(texto):
    return texto.upper()

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Contar letras 'a'")
    print("2. Reemplazar texto")
    print("3. Convertir a mayúsculas")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

# Función principal
def main():
    cadena = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
    opcion = mostrar_menu()

    while opcion != '4':
        if opcion == '1':
            cantidad_a = contar_letras_a(cadena)
            print(f"La cadena '{cadena}' tiene {cantidad_a} letras 'a'")
        elif opcion == '2':
            texto = input("Ingrese un texto: ")
            buscar = "es"
            reemplazar = "ES"
            texto_modificado = reemplazar_texto(texto, buscar, reemplazar)
            print(f"Texto original: {texto}")
            print(f"Texto modificado: {texto_modificado}")
        elif opcion == '3':
            texto = input("Ingrese un texto: ")
            texto_mayusculas = convertir_mayusculas(texto)
            print(f"Texto original: {texto}")
            print(f"Texto en mayúsculas: {texto_mayusculas}")
        else:
            print("Opción inválida. Por favor, ingrese nuevamente.")

        opcion = mostrar_menu()

    print("¡Hasta luego!")

# Llamada a la función principal
main()
