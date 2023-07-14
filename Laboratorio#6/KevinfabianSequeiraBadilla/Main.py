# CodigoLab6Progra2KevinFabianSequeiraBadilla


class Avion:
    def __init__(self, numero_vuelo):
        self.numero_vuelo = numero_vuelo

# esto es la lista y ya


class SistemaControlAviones:
    def __init__(self):
        self.lista_espera = []

 # aqui esta la parte donde se agrega el avion ( la opcion 1 )
    def agregar_avion(self, numero_vuelo):
        avion = Avion(numero_vuelo)
        self.lista_espera.append(avion)
        print(
            f"Avion con numero de vuelo {numero_vuelo} agregado a la lista de espera.")


# esto es la opcion de mostrar la lista ( opcion 2 )

    def mostrar_lista_espera(self):
        if self.lista_espera:
            print("Lista de espera de aviones:")
            for avion in self.lista_espera:
                print(f"Numero de vuelo: {avion.numero_vuelo}")
        else:
            print("No hay aviones en la lista de espera.")


# aca esta lo que utilise para eliminar los aviones ( opcion 3 )


    def eliminar_avion(self, numero_vuelo):
        for avion in self.lista_espera:
            if avion.numero_vuelo == numero_vuelo:
                self.lista_espera.remove(avion)
                print(
                    f"Avion con numero de vuelo {numero_vuelo} fue eliminado de la lista de espera.")
                return
        print(
            f"No hay ningun avion con numero el numero de vuelo {numero_vuelo} en la lista de espera.")


# esta es la parte del codigo para buscar los aviones ( opcion 4 )

    def buscar_avion(self, numero_vuelo):
        for i, avion in enumerate(self.lista_espera):
            if avion.numero_vuelo == numero_vuelo:
                print(
                    f"El avion con el numero de vuelo {numero_vuelo} esta en la posicion {i+1} de la lista de espera.")
                return
        print(
            f"No se encontro ningun avion con el numero de vuelo {numero_vuelo} en la lista de espera.")


# esto de aca es para ver la cantidad de aviones ( opcion 5 )

    def mostrar_cantidad_aviones(self):
        cantidad = len(self.lista_espera)
        print(f"Hay {cantidad} aviones en la lista de espera.")


# esto es corazon del menu para el User
if __name__ == "__main__":
    sistema = SistemaControlAviones()

    while True:
        print("\nSistema de control de aviones")
        print("1. Agregar un avion a la lista de espera")
        print("2. Mostrar la lista de espera")
        print("3. Eliminar un avion de la lista de espera")
        print("4. Buscar un avion en la lista de espera")
        print("5. Mostrar la cantidad de aviones en la lista de espera")
        print("6. Salir")


# este ya es el menu que el User va a ver
# este es el mensaje que le da el sistema al User antes de las opciones
        opcion = input(
            "Elige la operacion que deseas realizar: ")

# estas son las opciones del menu
        if opcion == "1":
            numero_vuelo = input("Ingrese el numero de vuelo del avion: ")
            sistema.agregar_avion(numero_vuelo)
        elif opcion == "2":
            sistema.mostrar_lista_espera()
        elif opcion == "3":
            numero_vuelo = input(
                "Ingrese el numero de vuelo del avion que quiere eliminar: ")
            sistema.eliminar_avion(numero_vuelo)
        elif opcion == "4":
            numero_vuelo = input(
                "Ingrese el numero de vuelo del avion que quiere buscar: ")
            sistema.buscar_avion(numero_vuelo)
        elif opcion == "5":
            sistema.mostrar_cantidad_aviones()
        elif opcion == "6":
            print("((╯°□°）╯) Sistema cerrado...")

            break
        else:
            print("Opcion invalida. Por favor ingrese una opcion valida")
