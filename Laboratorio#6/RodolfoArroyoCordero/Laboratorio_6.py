lista_espera = []
ejecutando = True

def agregar_avion(self, numero_vuelo):
        avion = Avion(numero_vuelo)
        self.lista_espera.append(avion)
        print(
            f"Avion con numero de vuelo {numero_vuelo} agregado en lista de espera.")

def mostrar_lista_espera(self):
        if self.lista_espera:
            print("Lista de espera:")
            for avion in self.lista_espera:
                print(f"Numero de vuelo: {avion.numero_vuelo}")
        else:
            print("No hay aviones en espera.")

def despegar_avion_esperan(self, numero_vuelo):
        for avion in self.lista_espera:
            if avion.numero_vuelo == numero_vuelo:
                self.lista_espera.remove(avion)
                print(
                    f"Avion con numero de vuelo {numero_vuelo} fue eliminado de la lista de espera.")
                return
        print(
            f"No hay ningun avion con numero el numero de vuelo {numero_vuelo} en la lista de espera.")

def buscar_avion(self, numero_vuelo):
        for i, avion in enumerate(self.lista_espera):
            if avion.numero_vuelo == numero_vuelo:
                print(
                    f"El avion con el numero de vuelo {numero_vuelo} esta en la posicion {i+1} de la lista de espera.")
                return
        print(
            f"No se encontro ningun avion con el numero de vuelo {numero_vuelo} en la lista de espera.")

def mostrar_cantidad_aviones(self):
        cantidad = len(self.lista_espera)
        print(f"Hay {cantidad} aviones en la lista de espera.")

def mostrar_opciones():
        print("\nSistema de control de aviones")
        print("Opcion 1. Agregar un avion a la lista de espera")
        print("Opcion 2. Mostrar la lista de espera")
        print("Opcion 3. Eliminar un avion de la lista de espera")
        print("Opcion 4. Buscar un avion en la lista de espera")
        print("Opcion 5. Mostrar la cantidad de aviones en la lista de espera")
        print("Opcion 6. Salir")

mostrar_opciones()

while(ejecutando):
    opcion = input("Ingrese una opcion: ")
    if opcion == "A":
        agregar_avion()
    elif opcion == "B":
       mostrar_lista_espera()
    elif opcion == "C":
       buscar_avion()
    elif opcion == "D":
       despegar_avion_espera()
    elif opcion == "E":
        mostrar_cantidad_aviones()
    elif opcion == "F":
        print("Terminando programa inventario")
        ejecutando = False  
    else:
        mostrar_opciones()
        opcion = input("Ingrese una opcion: ")

     