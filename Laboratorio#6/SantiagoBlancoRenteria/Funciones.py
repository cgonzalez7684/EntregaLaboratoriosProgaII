ListaEspera = []

def agregar_avion ():
    avion = input("Agregue un avión a la lista de espera con su número de vuelo: ")
    ListaEspera.append(avion)
    
def mostrar_lista():
    print(ListaEspera)
    
def buscar_avion():
    try:
        num = input("Ingrese el numero de vuelo del avión: ")
        indice = ListaEspera.index(num)
        if (indice >= 0):
                print ("El avión se encuentra en la posición {0} de la lista de espera" .format(indice + 1))
    except BaseException:
        print ("El avión no se encuentra en la lista de espera")
        
def total_aviones():
    total = len(ListaEspera)
    print("La cantidad total de aviones en la lista de espera es de {0}".format(total))
    
            
def eliminar_avion():
    busqueda_avion = input("Ingrese el número de vuelo del avion: ")
    ListaEspera.remove(busqueda_avion)