# Definición de funciones

def guardar_avion(aviones, nombre, numVuelo):
    avion = {
        "nombre": nombre,
        "Numero de vuelo": numVuelo,
    }
    aviones.append(avion)

def ver_lista_espera_aviones(aviones):
    if len(aviones) == 0:
        print("No hay aviones en la lista de espera.")
    else:
        print("Lista de espera de aviones:")
        for index, avion in enumerate(aviones, start=1):
            print(f"Avión {index}:")
            print(f"  Nombre: {avion['nombre']}")
            print(f"  Numero de vuelo: {avion['Numero de vuelo']}")
            print()  # Agrega una línea en blanco para separar los aviones

def eliminar_avion(aviones, nombre_avion):
    indice_avion = None
    for index, avion in enumerate(aviones):
        if avion["nombre"] == nombre_avion:
            indice_avion = index
            break

    if indice_avion is not None:
        aviones.pop(indice_avion)
        print(f"Avión '{nombre_avion}' eliminado de la lista de espera.")
    else:
        print(f"No se encontró el avión '{nombre_avion}' en la lista de espera.")

def buscar_avion_por_numero_vuelo(aviones, numVuelo):
    encontrado = False
    for index, avion in enumerate(aviones, start=1):
        if avion["Numero de vuelo"] == numVuelo:
            print(f"El avión con número de vuelo '{numVuelo}' se encuentra en la posición {index} de la lista de espera.")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró ningún avión con número de vuelo '{numVuelo}' en la lista de espera.")

# Función del menú principal

def menu():
    aviones = []
    
    while True:
        # Mostrar opciones del menú
        print("Menú:")
        print("1. Agregar aviones")
        print("2. Lista de espera de aviones")
        print("3. Eliminar aviones")
        print("4. Buscar avion")
        print("5. Cantidad de aviones")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("Has seleccionado la opción 1")
            # Lógica para agregar aviones
            nombre = input("Ingrese el nombre del avión: ")
            numVuelo = input("Ingrese el número de vuelo del avión: ")
            guardar_avion(aviones, nombre, numVuelo)

        elif opcion == '2':
            print("Has seleccionado la opción 2")
            # Mostrar lista de espera de aviones
            ver_lista_espera_aviones(aviones)

        elif opcion == '3':
            print("Has seleccionado la opción 3")
            # Lógica para eliminar aviones
            nombre_avion = input("Ingrese el nombre del avión que desea eliminar: ")
            eliminar_avion(aviones, nombre_avion)

        elif opcion == '4':
            print("Has seleccionado la opción 4")
            # Lógica para buscar avión por número de vuelo
            numVuelo = input("Ingrese el número de vuelo del avión que desea buscar: ")
            buscar_avion_por_numero_vuelo(aviones, numVuelo)

        elif opcion == '5':
            print("Has seleccionado la opción 5")
            # Mostrar cantidad de aviones en la lista de espera
            print(f"Hay {len(aviones)} aviones en la lista de espera.")

        elif opcion.lower() == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el menú principal
menu()


        