aviones_espera = []
ejecutando = True

def agregar_avion_espera():
    print("Ingrese el numero de vuelo del avion:\n")
    avion = input()
    aviones_espera.append(avion)
    print("El avion ha sido agregado a la lista de espera")

def mostrar_aviones_espera():
    for avion in aviones_espera:
        print(f"Avion con numero de vuelo: {avion}")

def buscar_avion_espera():
    print("Ingrese el numero de vuelo del avion:")
    numero_vuelo = input()
    for avion in aviones_espera:
        if avion == numero_vuelo:
            return print(f"Avion con numero de vuelo {numero_vuelo} esta en la posicion {aviones_espera.index(avion + 1)}")
    print("Avion no encontrado")

def despegar_avion_espera():
    print("Ingrese el numero de vuelo del avion que acaba de despegar:")
    avion = input()
    aviones_espera.remove(avion)
    print("El avion ha sido removido de la lista de espera")

def contar_aviones_espera():
    print(f"La cantidad de aviones en lista de espera es de: {len(aviones_espera)}")
    [print(avion) for avion in aviones_espera]

def mostrar_opciones():
    print("Opcion A: Agregar avion a lista de espera")
    print("Opcion B: Mostrar aviones en lista de espera")
    print("Opcion C: Buscar avion por nombre")
    print("Opcion D: Despegar avion")
    print("Opcion E: Contar aviones en lista de espera")
    print("Opcion F: Salir del programa")


mostrar_opciones()

while(ejecutando):
    opcion = input("Ingrese una opcion: ")
    if opcion == "A":
        agregar_avion_espera()
    elif opcion == "B":
       mostrar_aviones_espera()
    elif opcion == "C":
       buscar_avion_espera()
    elif opcion == "D":
       despegar_avion_espera()
    elif opcion == "E":
        contar_aviones_espera()
    elif opcion == "F":
        print("Terminando programa inventario")
        ejecutando = False  
    else:
        mostrar_opciones()
        opcion = input("Ingrese una opcion: ")