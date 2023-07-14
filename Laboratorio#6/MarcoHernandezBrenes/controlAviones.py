
#Aqui defino  una clase llamada ControlAviones.
class ControlAviones:
# Aqui defino esto como un inicializador que se ejecuta cuando se crea una instancia de la clase ControlAviones.
# Voy a utlizar self para que los metodos de la clase interactúen con los atributos de la misma instancia de esa clase.
    def __init__(self):
# Aqui inicializo una lista vacía lista_espera que almacenará los números de vuelo de los aviones en espera.
        self.lista_espera = []
# En esta otra toma como argumento el número de vuelo del avión a agregar.
    def agregar_avion(self, numero_vuelo):
        self.lista_espera.append(numero_vuelo)
# agrego el número de vuelo a la lista de espera.
    def mostar_lista(self):
        for i, numero_vuelo in enumerate(self.lista_espera):
            print(f"{i + 1}. {numero_vuelo}")
# Este es un bucle que recorre cada avión en la lista de espera.
# Aqui imprimo el número de vuelo junto con su posición en la lista.
    def quitar_avion(self, numero_vuelo):
        if numero_vuelo in self.lista_espera:
            self.lista_espera.remove(numero_vuelo)

    def buscar_vuelo(self, numero_vuelo):
    # Aqui verifico si el número de vuelo dado se encuentra en la lista de espera.    
        if numero_vuelo in self.lista_espera:
            posicion = self.lista_espera.index(numero_vuelo) + 1
            print(f"El avión {numero_vuelo} está en la posición {posicion} de la lista de espera.")
        else:
            print(f"El avión {numero_vuelo} no se encuentra en la lista de espera.")

    def total_aviones(self):
        print(f"Total de aviones en la lista de espera: {len(self.lista_espera)}")
#Aqui creo la funcion main para manejar la lógica del programa principal.
def main():
    CA = ControlAviones()
    while True:
        print("\n1. Agregar avión a la lista de espera")
        print("2. Mostrar la lista de espera")
        print("3. Eliminar avión de la lista de espera")
        print("4. Buscar un avión por su número de vuelo")
        print("5. Mostrar el total de aviones en la lista de espera")
        print("6. Salir")
        option = input("Elige una opción: ")

        if option == '1':
            numero_vuelo = input("Introduce el número de vuelo: ")
            CA.agregar_avion(numero_vuelo)
        elif option == '2':
            CA.mostar_lista()
        elif option == '3':
            numero_vuelo = input("Introduce el número de vuelo del avión que ha despegado: ")
            CA.quitar_avion(numero_vuelo)
        elif option == '4':
            numero_vuelo = input("Introduce el número de vuelo a buscar: ")
            CA.buscar_vuelo(numero_vuelo)
        elif option == '5':
            CA.total_aviones()
        elif option == '6':
            break
        else:
            print("Opción inválida. Por favor elige una opción del 1 al 6.")

if __name__ == "__main__":
    main()
