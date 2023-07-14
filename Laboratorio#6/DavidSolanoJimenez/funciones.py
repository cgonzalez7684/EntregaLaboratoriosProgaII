aviones = []

#opcion 1 
def agregar_avion():
    vuelo = input("Ingrese el numero de vuelo: ")
    aviones.append(vuelo)  

#opcion 2    
def  mostrar_aviones_orden_llegada():
    for vuelo in aviones:
        print(vuelo)
 
#opcion 3        
def eliminar_avion():
     vuelo = input("Ingrese el nombre del vuelo a eliminar: ")
         
     if(vuelo in aviones):
         aviones.remove(vuelo)
         print("El vuelo {0} a sido eliminado".format(vuelo))
     else:
         print("EL vuelo no esta en lista")
         
#opcion 4     
def buscar_aviones():
    try:  
         nombre = input("ingrese el numero del vuelo a ubicar: ")
         indice = aviones.index(nombre)
         if (indice > 0):
            print("El avion si esta en espera en el espacio: " + str(indice))  
    except ValueError:
        print("El avion no se encuentra en espera")
        
#opcion 5        
def mostrar_total_aviones():
    totalAviones = len(aviones)
    print("El total de aviones en espera {0}".format(totalAviones))
            