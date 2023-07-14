class Avion:
    def __init__(self, numero_vuelo):
        self.numero_vuelo = numero_vuelo
# Lista de los vuelos

class ControlAviones:
    def __init__(self):
        self.lista_espera = []
    def agregar_avion(self, numero_vuelo):    # Funcion para agregar aviones
        avion = Avion(numero_vuelo)
        self.lista_espera.append(avion)
        print(
            f"Avion con numero de vuelo {numero_vuelo} agregado a la lista de espera.")


    def ver_lista_espera(self): #Funcion para mostrar la lista
        if self.lista_espera:
            print("Lista de espera de aviones:")
            for avion in self.lista_espera:
                print(f"Numero de vuelo: {avion.numero_vuelo}")
        else:
            print("La lista está vacía.")

    def eliminar_avion(self, numero_vuelo): #Funcion para eliminar aviones
        for avion in self.lista_espera:
            if avion.numero_vuelo == numero_vuelo:
                self.lista_espera.remove(avion)
                print(
                    f"Avion con numero de vuelo {numero_vuelo} fue eliminado de la lista de espera.")
                return
        print(
            f"El avion con numero el numero de vuelo {numero_vuelo} no se encuentra en la lista de espera.")

    def buscar_avion(self, numero_vuelo): #Funcion para buscar aviones
        for i, avion in enumerate(self.lista_espera):
            if avion.numero_vuelo == numero_vuelo:
                print(
                    f"El avion con el numero de vuelo {numero_vuelo} esta en la posicion {i+1} de la lista de espera.")
                return
        print(
            f"El avion con el numero de vuelo {numero_vuelo} no se encuentra en la lista de espera.")


    def mostrar_cantidad_aviones(self): #Funcion para ver la cantidad de aviones
        cantidad = len(self.lista_espera)
        print(f"Hay {cantidad} aviones esperando.")



if __name__ == "__main__": #Menu principal para el usuario
    sistema = ControlAviones()

    while True:
        print("\nSistema de control de aviones")
        print("1. Agregar un avion a la lista")
        print("2. Mostrar la lista")
        print("3. Eliminar un avion de la lista")
        print("4. Buscar un avion en la lista")
        print("5. Mostrar la cantidad de aviones en la lista")
        print("6. Salir")

        opcion = input(
            "Escoge la opcion del menú: ")

#Opciones del menu
        if opcion == "1":
            numero_vuelo = input("Ingrese el numero de vuelo: ")
            sistema.agregar_avion(numero_vuelo)
        elif opcion == "2":
            sistema.ver_lista_espera()
        elif opcion == "3":
            numero_vuelo = input(
                "Ingrese el numero de vuelo que quiere borrar: ")
            sistema.eliminar_avion(numero_vuelo)
        elif opcion == "4":
            numero_vuelo = input(
                "Ingrese el numero de vuelo que quiere encontrar: ")
            sistema.buscar_avion(numero_vuelo)
        elif opcion == "5":
            sistema.mostrar_cantidad_aviones()
        elif opcion == "6":
            print("Te has salido del programa. Te estaremos esperando con chocolate caliente")
            break
        else:
            print("Opcion incorrecta. Tal vez escoger una de las opciones del menú sea una buena idea.") 
