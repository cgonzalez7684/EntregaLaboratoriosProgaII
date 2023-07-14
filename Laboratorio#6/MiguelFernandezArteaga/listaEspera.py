

lista_espera = [] # Lista para almacenar los aviones.

def menu():
    try:
        while True:
            print("\nMenu")
            print("Opcion #1: Imprimir Lista de Espera.")
            print("Opcion #2: Agregar aviones a la lista de espera.")
            print("Opcion #3: Eliminar aviones de la lista de espera ")
            print("Opcion #4: Buscar un avión por número de vuelo ")
            print("Opcion #5: Mostrar la cantidad total de aviones ")            
            print("Opcion #6: Salir \n") 
            tecla = input("Digitar opcion: ")
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)
            if i == 1:
                imprimir_lista_espera()
            elif i==2:
                agregar_avion()                       
            elif i==3:
                eliminar_avion()
            elif i==4:
                buscar_avion()                       
            elif i==5:
                cantidad_aviones_espera()                         
            elif i==6:
                break                
            elif i==9:
                print("to-do")
            else:
                print('Opcion invalida')
                continue 
    except BaseException:
        print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
        input()

#Funcion para imprimir la lista de espera de aviones.
def imprimir_lista_espera():
    print("Lista de espera:")
    print("-----------------")
    if not lista_espera:
        print("No hay aviones en la lista de espera.")
    else:
        for avion in lista_espera:
            print(avion)
        cantidad_aviones_espera()

#Funcion para agregar los aviones a la lista de espera
def agregar_avion():
    numero_vuelo = input("Ingresa el número de vuelo del avión: ").upper()
    if numero_vuelo not in lista_espera:
        lista_espera.append(numero_vuelo)
        print("Avión agregado a la lista de espera.")
    else:
        print("El avión ya está en la lista de espera.")
                    
#Funcion para eliminar un avion de la lista de espera
def eliminar_avion():
    numero_vuelo = input("Ingresa el número de vuelo que ha despegado: ").upper()
    if numero_vuelo in lista_espera:
        lista_espera.remove(numero_vuelo)
        print("Avión eliminado de la lista de espera.")
    else:
        print("El avión no está en la lista de espera.")

#Funcion de busqueda de aviones, que escribe en pantalla el lugar en la lista
def buscar_avion():
    numero_vuelo = input("Ingresa el número de vuelo del avión: ").upper()
    if numero_vuelo in lista_espera:
        posicion = lista_espera.index(numero_vuelo)
        print(f"El avión con número de vuelo {numero_vuelo} se encuentra en la posición {posicion} de la lista de espera.")
        imprimir_lista_espera()
    else:
        print("El avión no está en la lista de espera.")
        
#Funcion para saber el total de aviones en la lista 
def cantidad_aviones_espera():
    print(f"Hay {len(lista_espera)} avion(s) en la lista de espera.")