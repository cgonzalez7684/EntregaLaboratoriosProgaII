inventario = []

def agregar_fruta ():
    #Utilizo un input para pedirle al usuario la fruta que desea agregar
    fruta = input("Agregue una fruta al inventario: ")
    #con el método append() podemos agregar el elemento que deseemos a una lista en el último lugar de este
    inventario.append(fruta)
    
def mostrar_inventario():
    print(inventario)
    
def buscar_fruta_por_nombre():
    #Utilizo un try except porque si la fruta que el usuario ingresa no existe se crea una excepción
    try:
        #Utilizo un input para pedirle al usuario la fruta que desea encontrar
        nombre = input("Ingrese el nombre de la fruta: ")
        #Utilizo el método index() para saber si la fruta que busca el usuario se encuentra en la lista
        indice = inventario.index(nombre)
        #Si índice me retorna un número mayor o igual a 0, entonces el elemento existe en la lista
        if (indice >= 0):
                print ("La fruta sí se encuentra en el inventario")
    #Cuando se genere la excepción le indico al usuario que la fruta no se encuentra en el inventario
    except BaseException:
        print ("La fruta no se encuentra en el inventario")
        
def calcular_total_frutas():
    #Utilizo el método len() para saber la cantidad de elementos de la lista
    total = len(inventario)
    print("Cantidad de elementos {0}".format(total))
    
def eliminar_fruta():
    #Utilizo un input para pedirle al usuario la fruta que desea eliminar
    busqueda_fruta = input("Ingrese el nombre de la fruta: ")
    #Utilizo el método count() para saber cuántas veces aparece la fruta que ingresó el usuario en la lista
    cantidad_fruta = inventario.count(busqueda_fruta)
    #Resultado que no es plural
    if (cantidad_fruta > 0 and cantidad_fruta < 2):
        print ("Había una cantidad de {0} {1}" .format(cantidad_fruta, busqueda_fruta))
        inventario.remove(busqueda_fruta)
    #Resultado que sí es plural
    elif (cantidad_fruta > 1):
        print ("Había una cantidad de {0} {1}s" .format(cantidad_fruta, busqueda_fruta))
        inventario.remove(busqueda_fruta)
    #Resultado si no hay de la fruta que buscaba eliminar el usuario
    else:
        print("No hay {0}s en el inventario" .format(busqueda_fruta))