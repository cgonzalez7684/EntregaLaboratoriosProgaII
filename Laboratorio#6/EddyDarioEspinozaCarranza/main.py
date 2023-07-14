class ControlAviones:
    def __init__(self):
        self.lista_espera = []

    def agregar_avion(self, numero_vuelo):
        self.lista_espera.append(numero_vuelo)
        print("Avión {} agregado a la lista de espera.".format(numero_vuelo))

    def mostrar_lista_espera(self):
        print("Lista de espera de aviones:")
        for i, avion in enumerate(self.lista_espera, start=1):
            print("{}. {}".format(i, avion))

    def eliminar_avion(self, numero_vuelo):
        if numero_vuelo in self.lista_espera:
            self.lista_espera.remove(numero_vuelo)
            print("Avión {} eliminado de la lista de espera.".format(numero_vuelo))
        else:
            print("Avión {} no encontrado en la lista de espera.".format(numero_vuelo))

    def buscar_avion(self, numero_vuelo):
        if numero_vuelo in self.lista_espera:
            posicion = self.lista_espera.index(numero_vuelo) + 1
            print("El avión {} está en la posición {} de la lista de espera.".format(numero_vuelo, posicion))
        else:
            print("Avión {} no encontrado en la lista de espera.".format(numero_vuelo))

    def mostrar_cantidad_aviones(self):
        cantidad = len(self.lista_espera)
        print("Cantidad total de aviones en la lista de espera: {}".format(cantidad))


# Función principal para ejecutar el programa
def main():
    control_aviones = ControlAviones()

    while True:
        print("\n--- Sistema de Control de Aviones ---")
        print("1. Agregar avión a la lista de espera")
        print("2. Mostrar lista de espera")
        print("3. Eliminar avión de la lista de espera")
        print("4. Buscar avión en la lista de espera")
        print("5. Mostrar cantidad total de aviones en espera")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            numero_vuelo = input("Ingrese el número de vuelo del avión: ")
            control_aviones.agregar_avion(numero_vuelo)
        elif opcion == "2":
            control_aviones.mostrar_lista_espera()
        elif opcion == "3":
            numero_vuelo = input("Ingrese el número de vuelo del avión a eliminar: ")
            control_aviones.eliminar_avion(numero_vuelo)
        elif opcion == "4":
            numero_vuelo = input("Ingrese el número de vuelo del avión a buscar: ")
            control_aviones.buscar_avion(numero_vuelo)
        elif opcion == "5":
            control_aviones.mostrar_cantidad_aviones()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")