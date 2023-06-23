def main():
    # La función main(): Esta es la función principal del programa. Aqui creo un bucle infinito while True, imprime un menú con cuatro opciones y solicita al usuario que elija una, asi eran los 
    # requisitos y dependiendo de la opción que elija el usuario, se ejecutará una función específica. Si el usuario introduce "4", se sale del bucle y el programa termina. 
    # Si se introduce un valor que no corresponda a ninguna opción, se imprime un mensaje de error y se vuelve a mostrar el menú, para eso puse la opcion de "break" con un mensaje
    # Imprimir el menú y solicitar una opción
    while True:
        print("\nMenú:")
        print("1. Contar letras 'a' en el texto que ya esta en el programa")
        print("2. Reemplazar 'es' por 'ES' en el texto ingresado")
        print("3. Convertir texto ingresado a mayúsculas")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            contar_a()
        elif opcion == "2":
            reemplazar_es()
        elif opcion == "3":
            a_mayusculas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def contar_a():
    #La función contar_a(): Esta función cuenta cuántas veces aparece la letra 'a' en un texto predefinido. 
    # Aqui utilice  el método count de la clase string  para contar las ocurrencias de 'a'. Después, imprime el resultado.
    # Contar cuántas veces aparece 'a' en el texto
    # Aqui dejo la explicacion de "count" https://barcelonageeks.com/funcion-de-lista-de-python-count/
    texto = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
    num_a = texto.count('a')
    print(f"El texto contiene {num_a} letras 'a'.")

def reemplazar_es():
    # La función reemplazar_es(): Esta función pide al usuario que introduzca un texto y luego reemplaza todas las ocurrencias de la cadena 'es' por 'ES'. 
    # Utiliza el método replace de la clase string  para hacer el reemplazo. Luego, imprime el texto modificado.
    # Solicitar texto al usuario y reemplazar 'es' por 'ES'
    # Aqui dejo la explicacion de "replace" https://j2logo.com/string-replace-python/
    texto = input("Ingresa un texto: ")
    texto_modificado = texto.replace('es', 'ES')
    print(f"Texto modificado: {texto_modificado}")

def a_mayusculas():
    # La función a_mayusculas(): Esta función pide al usuario que introduzca un texto y luego lo convierte todo a mayúsculas. 
    # Usa el método upper de la clase string  para hacer esta conversión. Luego, imprime el texto en mayúsculas.
    # Solicitar texto al usuario y convertirlo a mayúsculas
    # Aqui dejo la explicacion de "upper" https://programacionfacil.org/blog/los-metodos-de-string-upper-lower-capitalize-y-title-de-python/
    texto = input("Ingresa un texto: ")
    texto_mayusculas = texto.upper()
    print(f"Texto en mayúsculas: {texto_mayusculas}")
#NOTA: Entendiendo que hace la "f" antes de la cadena de texto? 
# En Python, una cadena de texto normalmente se escribe entre comillas dobles ("") o comillas simples (''). 
# Para crear f-strings, solo tienes que agregar la letra f o F mayúscula antes de las comillas.
# Aqui dejo la explicacion: https://www.freecodecamp.org/espanol/news/tutorial-de-f-strings-en-python-formato-de-cadenas-en-python-explicado-con-ejemplos/#:~:text=En%20Python%2C%20una%20cadena%20de,%22%20es%20una%20f%2Dstring.
if __name__ == "__main__":
    main()

# Que significa las lineas 55 & 56? 
# Qué significa __name__ == '__main__' en Python?
# Aqui dejo la explicacion: https://codecraftershub.com/que-significa-name-main-en-python/
