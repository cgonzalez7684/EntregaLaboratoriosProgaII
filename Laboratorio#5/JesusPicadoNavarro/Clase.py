inventario=[]#Lista vacia

def agregarfruta():#define la funcion de agregar fruta]\
    frutanew=input(str(" \n Dijite el nombre de la fruta a agregar: \n "))#le pide al usuario dijitar el nombre de la fruta a agregar
    inventario.append(frutanew)#agrega la fruta dijitada por el usuario

def mostrarinventario():
    for frutas in inventario:#muentra en inventrio de frutas agregadas por el usuario
        print(frutas)
       
    
def buscarfruta(): #busca la fruta en el inventario
    busq=input(str("\n Dijite el nombre de la fruta a buscar: "))
    busq1= busq in inventario
    if busq1 == True:#aca realiza la comparacion de lo buscado con lo que hay en la lista inventario
        print(" \n En el inventario sí hay {0}\n".format(busq))
    else:
        print("\n No se encontro {0} en el inventario \n".format(busq))
    
    
def contfrutas():#cuenta la cantidad total de frutas usando la funcion len
    cantfrutas=len(inventario)
    print("\n Cantidad de frutas {0} \n".format(cantfrutas))  
    

def eliminar():#elimina la fruta ingresada por el usurio
    elim=input(str("Dijite el nombre del producto que desea eliminar: "))#ingreso de futa a eliminar
    cant=elim in inventario#cuenta la cantidad de la fruta en el inventario
    if cant == True:
        montfru=int(inventario.count(elim))#cantidad de frutas ingresadas en el inventario
        print("En el inventario hay {0} \n".format(montfru))
        cante=input(("\n¿Cuantas {0} desea eliminar? \n".format(elim)))
        cante=int(cante)#pregunta cuantas frutas va a eliminar 
        if cante > montfru:
            print("El numero indicado no es valido") #si el usurio selecciona una cantidad mayor a la que hay en el inventario no lo dejara restar la fruta
        elif cante <= montfru:#resta de fruta mator a 1
         totalem= montfru-cante
         for i in range (totalem): 
          inventario.remove(elim)#elimina la fruta seleccuionada del inventario
        if totalem==0:#de ser cero elimina totalmente la fruta del inventario
          while elim in inventario:
              inventario.remove(elim)
           
        print("El total de {0} es de {1}".format(elim, totalem))
    


 #Menu de opciones para el usuario

#def cod():   
# #Prueba el codigo y en caso de error finaliza la ejecucion del codigo
def cod():
 try:
        #mientras se cumpla correctamente las opciones que se le brinden al usuario el codigo estara en bucle
    while True:
        print("\nElija una de las siguientes opciones\n"
          "\n 1.Agregar fruta "
          "\n 2.Mostrar frutas añadidas al inventario"
          "\n 3.Buscar fruta en el inventario "
          "\n 4.contar el total de frutas en el inventario"
          "\n 5.Eliminar fruta del inventario"
          "\n 6.Salir del programa")
            
        opc=input("\ndigite una opcion: ")
            #En caso de dijitar uan letra mostrara un error
        if (not(opc.isdigit())):
            print("Debe digitar un numero ")
            continue
        nop=int(opc)
        #If anidado para ejecutar cada metod
        if nop==1: 
                    agregarfruta()
        elif nop==2:
                print("\n frutas en el inventario\n")
                mostrarinventario()
        elif nop==3:
                buscarfruta()
        elif nop==4:
                contfrutas()
        elif nop==5:
                eliminar()
        elif nop ==6:
            print("\nSaliendo del programa")
            break          
        else:#si se selecciona un numero mayor a 6 da error y muestra el mensaje
            print("\nOpcion invalida")
            continue
 except BaseException:#en caso de error finaliza la ejecucion del proegrama
        print("\nFinalizo el programa, presione una tecla para cerrar la ventana ")
        input()
