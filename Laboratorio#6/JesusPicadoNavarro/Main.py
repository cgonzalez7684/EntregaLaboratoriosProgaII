vuelos=[]#Lista vacia

def agregarvuelo():#define la funcion de agregar vuelo]\
    vuelonew=input(str(" \n Dijite el numero del vuelo: \n "))#le pide al usuario dijitar el nombre del vuelo
    vuelos.append(vuelonew)#agrega el vuelo por el usuario

def mostrarvuelos():
    for vuel in vuelos:#muentra en la lista de vuelos
        print(vuel)
       
    
def buscarvuelo(): #busca el vuelo
    busq=input(str("\n Dijite el numero del vuelo a buscar: "))
    busq1= busq in vuelos
    if busq1 == True:#aca realiza la comparacion de lo buscado con lo que hay en la lista 
        print(" \n sí hay vuelo {0}\n".format(busq))
    else:
        print("\n No se encontro el vuelo {0}  \n".format(busq))
    
    
def contvuelos():#cuenta la cantidad total de vuelos usando la funcion len
    cantvuelos=len(vuelos)
    print("\n Cantidad de vuelos {0} \n".format(cantvuelos))  
    

def eliminar():#elimina el vuelo ingresado por el usurio
    elim=input(str("Dijite el nombre del vuelo que desea eliminar: "))#ingreso del vuelo a eliminar
    cant=elim in vuelos#cuenta la cantidad de vuelos en el inventario
    if cant == True:
        montvu=int(vuelos.count(elim))#cantidad de frutas ingresadas en el inventario
        print("En la lista de vuelos esta el vuelo {0} \n".format(elim))
        cante=input(("\n¿Cuantos vuelos {0} desea eliminar? \n".format(elim)))
        cante=int(cante)#pregunta cuantos vuelos va a eliminar 
        if cante >montvu:
            print("El numero indicado no es valido") #si el usurio selecciona una cantidad mayor a la que hay en el inventario no lo dejara restar el vuelo
        elif cante <= montvu:#resta de vuelo mayor a 1
         totalem= montvu-cante
         for i in range (totalem): 
          vuelos.remove(elim)#eliminael vuelo seleccionado 
        if totalem==0:#de ser cero elimina totalmente el vuelo
          while elim in vuelos:
              vuelos.remove(elim)
           
        print("El total de vuelos {0} es de {1}".format(elim, totalem))
    


 #Menu de opciones para el usuario

  
# #Prueba el codigo y en caso de error finaliza la ejecucion del codigo
try:
        #mientras se cumpla correctamente las opciones que se le brinden al usuario el codigo estara en bucle
    while True:
        print("\nElija una de las siguientes opciones\n"
          "\n 1.Agregar vuelo "
          "\n 2.Mostrar vuelos añadidas a la lista de aviones"
          "\n 3.Buscar vuelo en la lista de aviones "
          "\n 4.contar el total de vuelos"
          "\n 5.Eliminar vuelo"
          "\n 6.Salir del programa")
            
        opc=input("\ndigite una opcion: ")
            #En caso de dijitar uan letra mostrara un error
        if (not(opc.isdigit())):
            print("Debe digitar un numero ")
            continue
        nop=int(opc)
        #If anidado para ejecutar cada metod
        if nop==1: 
                    agregarvuelo()
        elif nop==2:
                print("\n El vuelo en espera es el: \n")
                mostrarvuelos()
        elif nop==3:
                buscarvuelo()
        elif nop==4:
                contvuelos()
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
