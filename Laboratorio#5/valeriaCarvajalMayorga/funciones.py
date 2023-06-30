#Creo una lista vacía para el inventario para almacenar frutas
listaInventario=[]

#Función para agregar frutas al inventario
def agregar_fruta (lista):
    fruta = input("Ingrese una fruta que desee añadir a inventatio: \n").upper() #Convierto las entradas a mayúscula para no tener diferencias de mayúsculas o minúsculas en una misma palabra/fruta
    lista.append(fruta)

#For simple para recorrer toda la lista del inventario    
def mostrar_inventario (lista):
    print("--------------------\nINVENTARIO\n--------------------")
    for inventario in lista:
        print(inventario)
    print("-------------------- \n")
              
def buscar_fruta_por_nombre (lista):
    fruta= input("Ingrese el nombre de la fruta:\n").upper()
    #Verfico si el dato ingresado está dentro de la lista
    if (fruta in lista) == True:
        print("La fruta {0} sí se encuentra en el inventario\n".format(fruta))
        
    else:
        print ("La fruta {0} no se encuentra en el inventario\n".format(fruta))
        

def calcular_total_frutas (lista= []):
        frutas=0
        for inventario in lista:
            frutas+=1
        print("----------------------------\nTotal de frutas:        {0} \n----------------------------\n".format(frutas))
        
def eliminar_fruta (lista):
    fruta= input("Ingrese el nombre de la fruta que desee elimiar:\n").upper()
    #Verfico si la fruta ingresada se encuentra en el inventatio
    if (fruta in lista) == True:
        
        cantidad = lista.count(fruta) #Realizo el conteo de la fruta ingresada
        print("----------------------------\n Cantidad de {0} en el inventario:  {1}\n----------------------------\n".format(fruta,cantidad))
        
        eliminar = int(input("Ingrese la cantidad que desee eliminar del invenatrio \n")) #Se toma la cantidad de elementos a eliminar
        #A continuación, se validad si la cantidad a eliminar no supera la cantidad existente en el inventario.
        if eliminar > cantidad:
            print("Lo sentimos, no se puede realizar la acción porque la cantidad ingresada supera la cantidad existente.\n")
        else:
            while (eliminar != 0):
                i = 0 #Variable para saber el indice de cada uno de los elementos de la lista:
                for producto in lista:
                    if producto == fruta:  #Repasando la lista ordenadamente, si es igual a la que ingresa el usuario, se elimina
                        del lista [i]
                        eliminar -= 1 #Resto elminar para completar la cantidad de elmininaciones que pide el usuario
                        break #Detengo el for, ya que al eliminar un elemento los indices varían y podría no elminiar lo deseado, así que vuelvo a recorrer la lista desde el inicio
                    i += 1 #Sumo i ya que me indica el indice de los elementos en las iteraciones del for
            
            
            cantidad = lista.count(fruta) #Realizo el conteo de la fruta ingresada nuevamente, para confirmale el usuario la cantidad actual después de la eliminación
            print("----------------------------\n Cantidad de {0} en el inventario:  {1}\n----------------------------\n".format(fruta,cantidad))
    else:
        print ("La fruta {0} no se encuentra en el inventario\n".format(fruta))

def menu_de_opciones (lista = listaInventario):
    opc =0
    while (opc !=6):
        print("__________________ menu de opciones __________________\n")
        print("1) Agregar al inventario")
        print("2) Mostrar inventario")
        print("3) Busacar fruta")
        print("4) Ver el total de frutas")
        print("5) Eliminar del inventario")
        print("6) Salir")
        
        opc = input("Ingrese una Opción \n")
        if (opc.isdigit()): #Verifico si la opción es numérica
            opc = int(opc) #Convierto el dato ingresado de Str a Int
            if opc == 1:
                agregar_fruta(lista)
            elif opc == 2:
                mostrar_inventario(lista)
            elif opc == 3:
                buscar_fruta_por_nombre(lista)
            elif opc == 4:
                calcular_total_frutas(lista)
            elif opc == 5:
                eliminar_fruta(lista)
            elif opc > 6: # Si el usuario ingresa un opción fuera del menu
                print("Opción inválida")
        else:
            print("Debe ingresar dígitos y no caracteres. Inténtelo de nuevo \n")