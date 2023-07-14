from typing import Self


class Avion:
    def __init___(self, numero_vuelo):
        self.mumero_vuelo=numero_vuelo
        
class Holdaviones:
     def __init__(self):
        self.aviones = []
        
     def addavion(self, avion):
        self.aviones.append(avion)
        
     def mostrarlista(self):
         if len(self.aviones)== 0:
            print("La lista esta vacia")
         else:
            for i, avion in enumerate(self.aviones):
                print(f"posicion {i+1}: Numero de vuelo - {avion.numero_vuelo}")
                
     def delete_avion(self, avion):
         if avion in self.aviones:   
             self.aviones.remove(avion)
             print(f"El avión con número de vuelo {avion.numero_vuelo} ha sido eliminado de la lista de espera.")     
         else:
            print("El avión no se encuentra en la lista de espera.")
     def find_avion(self, numero_vuelo):
         for i, avion in enumerate(self.aviones):
            if avion.numero_vuelo == numero_vuelo:
                print(f"El avión con número de vuelo {numero_vuelo} se encuentra en la posición {i + 1} de la lista de espera.")
                return
         print("El avión no se encuentra en la lista de espera.")

     def show_aviones(self):
        cantidad_aviones = len(self.aviones)
        print(f"Hay {cantidad_aviones} aviones en la lista de espera.")
Lista_espera =ListaEsperaAviones()

while True:
     print("---- MENÚ ----")
     print("1. Agregar avión a la lista de espera")
     print("2. Mostrar lista de espera de aviones")
     print("3. Eliminar avión de la lista de espera")
     print("4. Buscar avión en la lista de espera")
     print("5. Mostrar cantidad total de aviones en la lista de espera")
     print("6. Salir")

     opcion = input("Ingrese el número de opción: ")
     
     if opcion == "1":
        numero_vuelo = input("Ingrese el número de vuelo del avión: ")
        avion = Avion(numero_vuelo)
        lista_espera.agregar_avion(avion)
        print(f"El avión con número de vuelo {numero_vuelo} ha sido agregado a la lista de espera.")
     elif opcion == "2":
        lista_espera.mostrarlista()
     elif opcion == "3":
        numero_vuelo = input("Ingrese el número de vuelo del avión a eliminar: ")
        avion = Avion(numero_vuelo)
        lista_espera.deleteavion(avion)
     elif opcion == "4":
         numero_vuelo = input("Ingrese el número de vuelo del avión a buscar: ")
         lista_esperafindavion(numero_vuelo)
     elif opcion == "5":
        lista_espera.show_aviones()
     elif opcion == "6":
        break
     else:
        print("Opción inválida. Por favor, ingrese un número de opción válido.")
     print("Saliendo")