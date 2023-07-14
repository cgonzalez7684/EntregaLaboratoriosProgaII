#Lista de aviones
lista_aviones = []

#Funcion agregar
def agregar_avion(lista_aviones, num_vuelo):
    lista_aviones.append(num_vuelo)
    print("Se ha agregado el avión a la lista.")

#Funcion mostrar
def mostrar_lista(lista_aviones):
    if len(lista_aviones) == 0:
        print("La lista se encuentra vacía.")
    else:
        print("Lista de aviones:")
        for i, avion in enumerate(lista_aviones, start=1):
            print(f"{i}. Avión # {avion}")
            
#Funcion mostrar cantidad
def mostrar_cantidad(lista_aviones):
    cantidad = len(lista_aviones)
    print(f"La cantidad total de aviones en la lista es de: {cantidad}")

#Funcion eliminar
def eliminar_avion(lista_aviones, num_vuelo):
    if num_vuelo in lista_aviones:
        lista_aviones.remove(num_vuelo)
        print("Avión eliminado de la lista.")
    else:
        print("El avión no se encuentra en la lista.")

#Funcion buscar
def buscar_avion(lista_aviones, num_vuelo):
    if num_vuelo in lista_aviones:
        posicion = lista_aviones.index(num_vuelo) + 1
        print(f"El avión {num_vuelo} se encuentra en la posición {posicion} de la lista.")
    else:
        print("El avión no se encuentra en la lista.")

#Bucle Menu
while True:
    print("1- Agregar avión a la lista")
    print("2- Mostrar lista")
    print("3- Eliminar avión de la lista")
    print("4- Buscar avión en la lista")
    print("5- Mostrar cantidad total de aviones en la lista")
    print("6- Salir")
    opcion = input("Digite la opcion que desea: ")

    if opcion == "1":
        num_vuelo = input("Ingrese el número de vuelo del avión: ")
        agregar_avion(lista_aviones, num_vuelo)
    elif opcion == "2":
        mostrar_lista(lista_aviones)
    elif opcion == "3":
        num_vuelo = input("Ingrese el número de vuelo del avión a eliminar: ")
        eliminar_avion(lista_aviones, num_vuelo)
    elif opcion == "4":
        num_vuelo = input("Ingrese el número de vuelo del avión a buscar: ")
        buscar_avion(lista_aviones, num_vuelo)
    elif opcion == "5":
        mostrar_cantidad(lista_aviones)
    elif opcion == "6":
        exit()
        break
    else:
        print("Opción no válida, ingrese una opción válida.")