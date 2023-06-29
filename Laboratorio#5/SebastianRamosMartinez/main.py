inventarioF=[]#lista de frutas
def eliminarF():
    elim=input(str("Ingrese el nombre de la fruta que desea eliminar: "))
    cant=elim in inventarioF
    if cant == True:
        montf=int(inventarioF.count(elim))#Cuenta la cantidad de frutas ingreasadas en el inventario
        print("En el inventario hay {0} \n".format(montf))
        cante=input(("\n¿Cuantas {0} desea eliminar? \n".format(elim)))
        cante=int(cante)
        if cante > montf:
            print("El numero indicado no es valido") 
        elif cante <= montf:
         totalE= montf-cante
         for i in range (totalE): 
          inventarioF.remove(elim)#elimina la fruta seleccuionada del inventario
        if totalE==0:
          while elim in inventarioF:
              inventarioF.remove(elim)
           
        print("El total de {0} es de {1}".format(elim, totalE))

def buscarF(): #busca la fruta en el inventario
    busq=input(str("\n Dijite el nombre de la fruta a buscar: "))
    busq1= busq in inventarioF
    if busq1 == True:#aca realiza la comparacion de lo buscado con lo que hay en la lista inventario
        print(" \n En el inventario sí hay {0}\n".format(busq))
    else:
        print("\n No se encontro {0} en el inventario \n".format(busq))    
        
def contF():#Cuenta la cantidad total de frutas usando la funcion len
    cantfrutas=len(inventarioF)
    print("\n Cantidad de frutas {0} \n".format(cantfrutas))  
      

def mostrarF():
    for frutas in inventarioF:#muentra en inventrio de frutas agregadas por el usuario
        print(frutas)

def agregarF():#define la funcion de agregar fruta]\
    frutan=input(str(" \n Dijite el nombre de la fruta a agregar: \n "))
    inventarioF.append(frutan)#agrega la fruta dijitada por el usuario
    
while True:
        print("""\nElija una de las siguientes opciones\n
            1.Agregar fruta 
            2.Mostrar frutas del inventario
            3.Buscar fruta del inventario 
            4.Contar el total de frutas en el inventario
            5.Eliminar fruta del inventario
            6.Salir del programa""")
            
        opc=input("\nIngrese una opcion: ")
           
        if (not(opc.isdigit())):#Si se ingresa un numero erroneo se muestra el mensaje
            print("Debe digitar un numero ")
            continue
        nop=int(opc)
        if nop==1: 
                    agregarF()
        elif nop==2:
                print("\n frutas en el inventario\n")
                mostrarF()
        elif nop==3:
                buscarF()
        elif nop==4:
                contF()
        elif nop==5:
                eliminarF()
        elif nop ==6:
            print("\nSaliendo del programa")
            break          
        else:
            print("\nOpcion invalida")
            continue