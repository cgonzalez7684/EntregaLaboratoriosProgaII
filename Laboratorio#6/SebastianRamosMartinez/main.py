listaV=["D26", "F45", "E32"]
def agregarV():
    avion=input(str(" \n Ingrese el numero de vuelo: \n "))
    listaV.append(avion)
    
def eliminarV():
    elim=input(str("Ingrese el numero de vuelo que desea eliminar: "))
    elim1=elim in listaV
    listaV.remove(elim)
    if elim1 == True:
       print("Se ha podido eliminar correctamente el vuelo")
       listaV.remove(elim)  
    else:
        print("\n No se encontro {0} en la lista de espera \n".format(elim))   


def buscarV(): 
    i=1
    busq=input(str("\n Dijite el numero de vuelo que desea buscar: "))
    busq1= busq in listaV
    if busq1 == True:
        for avion in listaV:
            
            if avion == busq:
                print("Si se encuentra el vuelo numero",avion,"y esta en la posicion", i ) 
            i+=1    
    else:
        print("\n No se encontro {0} en la lista de espera \n".format(busq))   
        
def contV():
    cantVuelos=len(listaV)
    print("\n La cantidad actual de vuelos en espera son de {0} \n".format(cantVuelos))  
      

def mostrarV():
    i=1
    for avion in listaV:
        
        print(i,".",avion)
        i+=1
        
while True:
        print("""\nElija una de las siguientes opciones\n
            1.Agregar vuelo a la lista de espera
            2.Mostrar vuelos
            3.Buscar vuelos en espera
            4.Contar la cantidad de vuelos en espera
            5.Eliminar vuelo
            6.Salir del programa""")
            
        opc=input("\nIngrese una opcion: ")
           
        if (not(opc.isdigit())):
            print("Debe digitar un numero ")
            continue
        s=int(opc)
        if s==1: 
                agregarV()
        elif s==2:
                mostrarV()
        elif s==3:
                buscarV()
        elif s==4:
                contV()
        elif s==5:
                eliminarV()
        elif s==6:
            print("\nPrograma finalizado")
            break          
        else:
            print("\nOpcion invalida")
            continue