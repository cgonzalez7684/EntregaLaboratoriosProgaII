lista_espera = []

def agregar_avion(numero_vuelo):
    lista_espera.append(numero_vuelo)
    print("Avión agregado a la lista de espera.")

def mostrar_lista_espera():
    if len(lista_espera) > 0:
        print("Lista de espera de aviones:")
        for i, numero_vuelo in enumerate(lista_espera):
            print(f"{i+1}. {numero_vuelo}")
    else:
        print("No hay aviones en la lista de espera.")

def eliminar_avion(numero_vuelo):
    if numero_vuelo in lista_espera:               
        lista_espera.remove(numero_vuelo)
        print("Avión eliminado de la lista de espera.")
    else:
        print("El avión no se encontraba en la lista de espera.")

def buscar_avion(numero_vuelo):
    if numero_vuelo in lista_espera:
        posicion = lista_espera.index(numero_vuelo) + 1
        print(f"El avión {numero_vuelo} está en la posición {posicion} de la lista de espera.")
    else:
        print("El avión no se encuentra en la lista de espera.")

def mostrar_cantidad_aviones():
    cantidad_aviones = len(lista_espera)
    print(f"Hay {cantidad_aviones} aviones en la lista de espera.")

while True:
    print("\n¿Qué acción deseas realizar?")
    print("1. Agregar avión a la lista de espera")
    print("2. Mostrar lista de espera de aviones")
    print("3. Eliminar avión de la lista de espera")
    print("4. Buscar avión en la lista de espera")
    print("5. Mostrar cantidad total de aviones en la lista de espera")
    print("6. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        numero_vuelo = input("Ingrese el número de vuelo del avión: ")
        agregar_avion(numero_vuelo)
    elif opcion == "2":
        mostrar_lista_espera()
    elif opcion == "3":
        numero_vuelo = input("Ingrese el número de vuelo del avión que ha despegado: ")
        eliminar_avion(numero_vuelo)
    elif opcion == "4":
        numero_vuelo = input("Ingrese el número de vuelo del avión que desea buscar: ")
        buscar_avion(numero_vuelo)
    elif opcion == "5":
        mostrar_cantidad_aviones()
    elif opcion == "6":
        break
    else:
        print("Opción inválida. Por favor, ingresa un número del 1 al 6.")