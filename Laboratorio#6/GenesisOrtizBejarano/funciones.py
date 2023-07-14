lista_espera = [] 

#Agregar los aviones a la lista de espera.
def agregar_avion():
    vuelo = input("Ingresa el número de vuelo del avión a agregar: ").upper()
    #Verifica si el vuelo esta dentro de la lista si no esta lo agrega
    if vuelo in lista_espera:
        print("El avión ya está en la lista de espera.")
    else:
        lista_espera.append(vuelo)
        print("Avión ha sido agregado a la lista de espera.")


#Imprimir la lista de espera de aviones.
def imprimir_lista():
    print("La lista de aviones en espera:")
    print("-----------------")
    #Verifica si hay aviones
    if not lista_espera:
        print("No hay aviones en la lista de espera.")
    else:
        for avion in lista_espera:
            print(avion)
        cantidad_aviones()


                    
#Eliminar un avion de la lista de espera
def eliminar_avion():
    vuelo = input("Ingresa el número de vuelo a eliminar: ").upper()
    if vuelo in lista_espera:
        lista_espera.remove(vuelo)
        print("El avión eliminado de la lista de espera.")
    else:
        print("El avión no está en la lista de espera.")

#Busca los aviones en la lista de espera
def buscar_avion():
    vuelo = input("Ingresa el número de vuelo del avión: ").upper()
    if vuelo in lista_espera:
        posicion = lista_espera.index(vuelo)
        print(f"El avión con número de vuelo {0} se encuentra en la posición {1} de la lista de espera.")
        imprimir_lista()
    else:
        print("El avión no está en la lista de espera.")
        
#Funcion para saber el total de aviones en la lista 
def cantidad_aviones():
    print(f"Hay {len(lista_espera)} aviones en la lista de espera a despegar.")