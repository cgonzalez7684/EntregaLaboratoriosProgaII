inventario=["fresa","naranja","maracuya"]

def agregar_fruta(): 
    fruta=input("Digite la fruta que desea agregar : ")
    inventario.append(fruta.lower()) #colocamos las letras en minusculas para evitar errores

def mostrar_frutas():
    for lista in inventario:
        print(lista)

def buscar_frutas():
    try:
        fruta=input("Digite la fruta que busca: ")
        buscar = fruta.lower()                              #ya que todo en la lista esta en minuscula, colocamos esto tambien para evitar problemas
        indice = inventario.index(buscar)           #utilizamos el index para localizar la fruta en la lista
        if (indice > 0):                                    #Se evalua la cantidad de frutas, si es mayor a 0 si esta en la lista, sino, no lo está
           print ("Ciertamente, la fruta está en la lista")
    except BaseException:                                   
        print ("La fruta que buscas no se encuentra en está lista")    
    
def calcular_frutas():
    total = len(inventario)                                  #utilizamos len para saber la cantidad de frutas que hay en la lista
    print("Cantidad de elementos {0}".format(total))
    
def eliminar_fruta():
    fruta = input("Ingrese el nombre de la fruta: ")
    buscar = fruta.lower()
    cantidad_fruta = inventario.count(buscar)         #utilizamos count para saber la cantidad de frutas que hay
    
    if (cantidad_fruta > 0 and cantidad_fruta < 2):   
        print ("Existen : {0} {1}" .format(cantidad_fruta, buscar))
        inventario.remove(buscar)
    elif (cantidad_fruta > 1):                               
        print ("Existen {0} de {1}" .format(cantidad_fruta, buscar))
        inventario.remove(buscar)
    else:                                                     #si no hay una fruta para eliminar, se muestra un mensaje de error
        print("No se encuentran : {0} en el inventario" .format(buscar))
    print("Inventario Disponible")
    mostrar_frutas() 