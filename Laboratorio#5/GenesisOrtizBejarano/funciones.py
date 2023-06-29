
#Lista del inventario
inventario = [] 

    
    
def agregar_fruta():
    #Solicita la fruta
    fruta_agregar = input("Ingrese el nombre de la fruta que desea agregar al inventario: ")
    fruta_agregar.capitalize()
    #Agrega la fruta an inventario
    inventario.append(fruta_agregar)
    print("Se ingresó la fruta: {0} al inventario".format(fruta_agregar))
    print("\n")
    print("----------------------------------------------------------------------") 
    print("\n")  

def mostrar_inventario():
    #Recorrer la lista e imprimir las frutas
    print("Las frutas en el inventario son: \n")
    for frutas in inventario:
        print (frutas)
    print("\n")   
    print("----------------------------------------------------------------------")     
    print("\n")

def buscar_fruta_por_nombre():
    #Se solicita y se busca la fruta en el inventario, indica si se encuentra o no 
    fruta_buscada = input("Ingrese el nombre de la fruta que desea buscar: ")
    fruta_buscada.capitalize()
    
    se_encuentra = fruta_buscada in inventario
    print("Se encuentra la fruta {0} en el inventario?? Respueta: {1}".format(fruta_buscada,se_encuentra))
    print("\n")   
    print("----------------------------------------------------------------------")     
    print("\n")

def calcular_total_frutas():
    #Calcula cuantas frutas hay en total en el inventario
    total_frutas = len(inventario)
    print("Hay un total de  {0} frutas en el inventatio".format(total_frutas))
    print("\n")   
    print("----------------------------------------------------------------------")     
    print("\n")

def eliminar_fruta():
    fruta_eliminar = input("Ingrese el nombre de la fruta que desea eliminar: ")
    fruta_eliminar.capitalize()
    se_encuentra = fruta_eliminar in inventario
    contador = inventario.count(fruta_eliminar)
    
    if (se_encuentra):
        print("Existen {0} cantidad de {1} en el inventario \n".format(contador,fruta_eliminar))
        cantidad_eliminar= input ("Cuentas {0} desea eliminar del inventario: ".format(fruta_eliminar))
        
        if (cantidad_eliminar > 0):

            inventario.remove(fruta_eliminar)
            cantidad_eliminar = cantidad_eliminar -1
           

        print ("Se ha eliminado la fruta {0} del inventario".format(fruta_eliminar))
    else:
        print("La fruta {0} no se encuentra en el inventario".format(fruta_eliminar))
    print("\n")   
    print("----------------------------------------------------------------------")     
    print("\n")

