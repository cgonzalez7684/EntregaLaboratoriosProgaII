def iniciar_programa():
    # Corre el programa hasta que el usuario decida salir
    while True:
        print("\nMenú:")
        print("1. Contar letras 'a' en San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste")
        print("2. Reemplazar 'es' por 'ES' en el texto ingresado")
        print("3. Convertir texto ingresado a mayúsculas")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            contar_letras_a()
        elif opcion == "2":
            modificar_texto()
        elif opcion == "3":
            convertir_mayusculas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def contar_letras_a():
    # Cuenta la cantidad de letras 'a' en un texto predefinido
    texto_predefinido = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
    cantidad_a = texto_predefinido.count('a')
    print(f"El texto predefinido contiene {cantidad_a} letras 'a'.")

def modificar_texto():
    # Reemplaza 'es' por 'ES' en el texto ingresado por el usuario
    texto_usuario = input("Ingresa un texto: ")
    texto_modificado = texto_usuario.replace('es', 'ES')
    print(f"Texto modificado: {texto_modificado}")

def convertir_mayusculas():
    # Convierte el texto ingresado por el usuario a mayúsculas
    texto_usuario = input("Ingresa un texto: ")
    texto_mayusculas = texto_usuario.upper()
    print(f"Texto en mayúsculas: {texto_mayusculas}")

# Comprueba si el archivo actual es el punto de entrada principal del programa
if __name__ == "__main__":
    iniciar_programa()

