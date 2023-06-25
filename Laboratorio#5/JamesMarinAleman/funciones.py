inventario=["naranja","piña","aguacate"]


def agregar_fruta(): 
    fruta=input("Digite la fruta que desea agregar : ")#reviso la fruta
    inventario.append(fruta.lower())                   #agrego  la fruta con .append #para que todo se guarde en minusculas
    #print(inventario)#imprime en forma de lista
    print("-------------------------------------")
    
def Mostrar_Frutas():
    for lista in inventario:
        print(lista) 
    print("-------------------------------------")
    #print(inventario) #imprime en forma lineal
    
    
def buscar_frutas():
    try:
        fruta=input("Digite la fruta que sea buscar : ")    #pido la fruta y la guardo
        buscar = fruta.lower()                              #paso fruta a minusculas
        indice = inventario.index(buscar)           #index para comprobar si la fruta existe en la lista y Lower para buscar en minuscula
    
        if (indice > 0):                                    #Si es mayor a 0 existe , si devuelve 0 no existe
           print ("La fruta se encuentra en el inventario")
    except BaseException:                                   #si no se encuentra tirar error entonces le ponemos una excepcion
        print ("La fruta no se encuentra en el inventario")
    print("-------------------------------------")

def calcular_frutas():
    total = len(inventario)                                  #len() para saber la cantidad de elementos de la lista
    print("Cantidad de elementos {0}".format(total))     
    print("-------------------------------------")  
    
    

def eliminar_fruta():
    fruta = input("Ingrese el nombre de la fruta: ") #pido la fruta y la guardo
    buscar = fruta.lower()
    cantidad_fruta = inventario.count(buscar)         #count para saber la cantidad de frutas en una lista
    
    if (cantidad_fruta > 0 and cantidad_fruta < 2):           # 0 frutas
        print ("Existen : {0} {1}" .format(cantidad_fruta, buscar))
        inventario.remove(buscar)
    elif (cantidad_fruta > 1):                                # frutas
        print ("Existen {0} de {1}" .format(cantidad_fruta, buscar))
        inventario.remove(buscar)
    else:                                                     #si no hay fruta para  eliminar
        print("No se encuentran : {0} en el inventario" .format(buscar))
    print("------------------------------------------------")
    print("*** Inventario Actual ***")
    Mostrar_Frutas()
    print("------------------------------------------------")
    

