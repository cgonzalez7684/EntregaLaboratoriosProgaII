inventario=[123,1234,12345] #se crea una lista

#  el avion

def agregar_avion(): 
    avion=input("Digite el avion que desea agregar : ")#reviso el avion
    inventario.append(avion)                  
    print(inventario)#imprime en forma de lista
    print("-------------------------------------")
    
def Mostrar_avion():
    print(" ** Lista de aviones en espera **")
    for lista in inventario:
        print(lista) 
    print("-------------------------------------")
    #print(inventario) #imprime en forma lineal



def eliminar_avion():
    avion = input("Ingrese el numero del avion: ") #pido el avion y lo guardo
    avion = input("Ingrese el numero del avion: ") #pido el avion y lo guardo
    N_avion = int(avion)
    for x in inventario:
        if N_avion == x:
            inventario.remove(N_avion)  
            print(x)  
        else:
            print("El AVION NO SE ENCUENTRA EN LA LISTA")
    print("------------------------------------------------")
    print("*** Inventario Actual ***")
    Mostrar_avion()
    print("------------------------------------------------")
    
    


def buscar_avion():
    try:
        avion=input("Digite el avion que sea buscar : ")    #pido la fruta y la guardo
        buscar = int(avion)                              #paso fruta a minusculas
        for x in inventario:
            if buscar == x:
                print("El avion se encuentra en la lista, Posicion : ",inventario.index(buscar)+1)
                #print(inventario.index(buscar)+1)
            else:
                print("El AVION NO SE ENCUENTRA EN LA LISTA")
    except BaseException:                                   #si no se encuentra tirar error entonces le ponemos una excepcion
        print ("La fruta no se encuentra en el inventario")
    print("-------------------------------------")



def calcular_vuelos():
    total = len(inventario)                                  #len() para saber la cantidad de elementos de la lista
    print("Cantidad de vuelos en lista de espera son :  {0}".format(total))     
    print("--------------------------------------------------------------")  
    