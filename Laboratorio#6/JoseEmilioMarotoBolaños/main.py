def agregar_avion(lista_espera, numero_vuelo):
    lista_espera.append(numero_vuelo)
    print("Avión agregado a la lista de espera.")

def mostrar_lista(lista_espera):
    if len(lista_espera) == 0:
        print("La lista de espera está vacía.")
    else:
        print("Lista de espera de aviones:")
        for i, avion in enumerate(lista_espera, start=1):
            print(f"{i}. Avión {avion}")

def eliminar_avion(lista_espera, numero_vuelo):
    if numero_vuelo in lista_espera:
        lista_espera.remove(numero_vuelo)
        print("Avión eliminado de la lista de espera.")
    else:
        print("Avión no encontrado en la lista de espera.")

def buscar_avion(lista_espera, numero_vuelo):
    if numero_vuelo in lista_espera:
        posicion = lista_espera.index(numero_vuelo) + 1
        print(f"El avión {numero_vuelo} se encuentra en la posición {posicion} de la lista de espera.")
    else:
        print("Avión no encontrado en la lista de espera.")

def mostrar_cantidad(lista_espera):
    cantidad = len(lista_espera)
    print(f"La cantidad total de aviones en la lista de espera es: {cantidad}")

lista_espera = []

while True:
    print("\n Sistema de Control de Aviones")
    print("1. Agregar avión a la lista de espera")
    print("2. Mostrar lista de espera")
    print("3. Eliminar avión de la lista de espera")
    print("4. Buscar avión en la lista de espera")
    print("5. Mostrar cantidad total de aviones en la lista de espera")
    print("0. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        numero_vuelo = input("Ingrese el número de vuelo del avión: ")
        agregar_avion(lista_espera, numero_vuelo)
    elif opcion == "2":
        mostrar_lista(lista_espera)
    elif opcion == "3":
        numero_vuelo = input("Ingrese el número de vuelo del avión a eliminar: ")
        eliminar_avion(lista_espera, numero_vuelo)
    elif opcion == "4":
        numero_vuelo = input("Ingrese el número de vuelo del avión a buscar: ")
        buscar_avion(lista_espera, numero_vuelo)
    elif opcion == "5":
        mostrar_cantidad(lista_espera)
    elif opcion == "0":
        print("Saliendo del sistema")
        break
    else:
        print("Opción inválida ingrese un número válido.")