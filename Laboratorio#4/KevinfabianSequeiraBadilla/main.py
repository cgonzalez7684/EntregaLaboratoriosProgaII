# Kevin Fabian Sequeira Badilla

def contar_letras_a(cadena):
    # aca usamos el metodo "count" para contar las ocurrencias de la letra 'a'
    cantidad = cadena.count('a')
    return cantidad


def reemplazar_texto(cadena):
    # aca se use el metodo "replace" para reemplazar 'es' por 'ES'
    nueva_cadena = cadena.replace('es', 'ES')
    return nueva_cadena


def convertir_a_mayusculas(cadena):
    # aca use el metodo "upper" para convertir toda la cadena a mayusculas
    nueva_cadena = cadena.upper()
    return nueva_cadena

# esta es la funcion principal que muestra el menu y maneja las opciones del usuario


def main():
    cadena = "San Jose; Cartago; Puntarenas; Heredia; Limon; Alajuela; Guanacaste"

    while True:
        # aca esta el menu
        print("Menú:")
        print("1. Contar letras 'a'")
        print("2. Reemplazar texto")
        print("3. Convertir a mayúsculas")
        print("4. Salir")

        opcion = input("Ingrese el numero de opcion: ")

        if opcion == '1':
            # esto es para contar las letras 'a'
            cantidad_a = contar_letras_a(cadena)
            print(f"La cantidad de letras 'a' es: {cantidad_a}\n")

        elif opcion == '2':
            # esto es para reemplazar texto
            texto = input("Ingrese un texto: ")
            nuevo_texto = reemplazar_texto(texto)
            print(f"El texto modificado es: {nuevo_texto}\n")

        elif opcion == '3':
            # esta es la opcion para convertir a mayusculas
            texto = input("Ingrese un texto: ")
            texto_mayusculas = convertir_a_mayusculas(texto)
            print(f"El texto en mayusculas es: {texto_mayusculas}\n")

        elif opcion == '4':
            # esto es para salir del programa
            print("Hasta luego :v")
            break

        else:
            print("Opcion invalida. Por favor, ingrese una opcion valida.\n")


# esta es la llamada a la función principal ( sin esto no funka )
main()
