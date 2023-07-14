class SistemaControlAviones:
    def __init__(self):
        self.lista_espera = []

    def agregar_avion(self, numero_vuelo):
        self.lista_espera.append(numero_vuelo)
        print(f"El avión con número de vuelo {numero_vuelo} ha sido agregado a la lista de espera.")

    def mostrar_lista_espera(self):
        if self.lista_espera:
            print("Aviones en lista de espera:")
            for i, avion in enumerate(self.lista_espera, 1):
                print(f"{i}. Número de vuelo: {avion}")
        else:
            print("No hay aviones en lista de espera.") 

    def eliminar_avion(self, numero_vuelo):
        if numero_vuelo in self.lista_espera:
            self.lista_espera.remove(numero_vuelo)
            print(f"El avión con número de vuelo {numero_vuelo} ha despegado y ha sido eliminado de la lista de espera.")
        else:
            print(f"No se encontró ningún avión con número de vuelo {numero_vuelo} en la lista de espera.")

    def buscar_avion(self, numero_vuelo):
        if numero_vuelo in self.lista_espera:
            posicion = self.lista_espera.index(numero_vuelo) + 1
            print(f"El avión con número de vuelo {numero_vuelo} se encuentra en la posición {posicion} de la lista de espera.")
        else:
            print(f"No se encontró ningún avión con número de vuelo {numero_vuelo} en la lista de espera.")

    def mostrar_cantidad_aviones(self):
        cantidad = len(self.lista_espera)
        print(f"La cantidad total de aviones en lista de espera es: {cantidad}")


def main():
    sistema = SistemaControlAviones()

    while True:
        print("\n--- Sistema de Control de Aviones ---")
        print("1. Agregar avión a lista de espera")
        print("2. Mostrar lista de espera")
        print("3. Eliminar avión de lista de espera")
        print("4. Buscar avión por número de vuelo")
        print("5. Mostrar cantidad total de aviones en lista de espera")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            numero_vuelo = input("Ingrese el número de vuelo del avión: ")
            sistema.agregar_avion(numero_vuelo)
        elif opcion == "2":
            sistema.mostrar_lista_espera()
        elif opcion == "3":
            numero_vuelo = input("Ingrese el número de vuelo del avión que ha despegado: ")
            sistema.eliminar_avion(numero_vuelo)
        elif opcion == "4":
            numero_vuelo = input("Ingrese el número de vuelo del avión a buscar: ")
            sistema.buscar_avion(numero_vuelo)
        elif opcion == "5":
            sistema.mostrar_cantidad_aviones()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
