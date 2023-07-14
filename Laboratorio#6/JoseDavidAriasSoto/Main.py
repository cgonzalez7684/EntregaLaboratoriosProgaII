# Crear una lista vacía para almacenar los aviones en espera
lista_espera = []

while True:
    comando = input("Ingrese un comando: ")

    # Agrega el avión a la lista de espera
    if comando.startswith("agregar"):
        numero_vuelo = input("Ingrese el número de vuelo: ")
        lista_espera.append(numero_vuelo)
        print("Vuelo", numero_vuelo, "agregado a la lista de espera.")

    # Muestra el avion en la lista de espera de aviones
    elif comando == "mostrar":
        print("Lista de espera:")
        for indice, numero_vuelo in enumerate(lista_espera):
            print(indice + 1, "-", numero_vuelo)

    # Elimina el avión de la lista de espera
    elif comando.startswith("eliminar"):
        numero_vuelo = input("Ingrese el número de vuelo: ")
        if numero_vuelo in lista_espera:
            lista_espera.remove(numero_vuelo)
            print("Vuelo", numero_vuelo, "eliminado de la lista de espera.")
        else:
            print("El vuelo", numero_vuelo, "no está en la lista de espera.")

    # Busca el avión en la lista de espera
    elif comando.startswith("buscar"):
        numero_vuelo = input("Ingrese el número de vuelo: ")
        if numero_vuelo in lista_espera:
            posicion = lista_espera.index(numero_vuelo) + 1
            print("El vuelo", numero_vuelo, "se encuentra en la posición", posicion, "en la lista de espera.")
        else:
            print("El vuelo", numero_vuelo, "no está en la lista de espera.")

    # enseña la cantidad total de aviones en la lista de espera
    elif comando == "cantidad":
        cantidad = len(lista_espera)
        print("Número total de vuelos en la lista de espera:", cantidad)

    # Salir del bucle principal
    elif comando == "salir":
        break

    # Comando desconocido
    else:
        print("Comando desconocido")
