lista_espera = []

def agregar_nemero_de_vuelo ():
    ANumero = input("Agregue el numero de vuelo:")
    lista_espera.append(ANumero)
    print()
    print("El numero de vuelo",ANumero, "se agrego")
    print()

def mostrar_vuelos ():
    for listaVuelos in lista_espera:
        print(lista_espera)
        
def buscar_vuelo_y_eliminar ():
        nombre = input("Ingrese el nombre del vuelo que desea eliminar: ")
        indice = lista_espera.remove(nombre)
        print("El vuelo",nombre, "se ha eliminado")
    
     
def buscar_vuelo_y_su_posicion ():
    espera = [lista_espera]
    numero_vuelo = input("Ingrese el numero de vuelo: ")
    
    if ():
        posicion = espera.index(numero_vuelo)
        print("El vuelo",numero_vuelo,"se en cuentra en la posicion",posicion,"de la lista de espera")
    else:
        print("El vuelo",numero_vuelo,"no se encuentra en la lista de espera")
        

def calcular_total_vuelos ():
    cantidadvuelos = len(lista_espera)
    print("En la lista de espera hay {0} vuelos".format(cantidadvuelos))
    
     
print("Opcion #1: Agregar numero de vuelo")
print("opcion #2: Mostrar vuelos ")
print("Opcion #3: Buscar el numero de vuelo y eliminarlo")
print("Opcion #4: Buscar la posicon de su numero de vuelo")
print("Opcion #5: Total de vuelos en la lista de espera")
print("Opcion #6: Salir del menu")
print()
    
while True:
    
    
    tecla= input("Digite la opcion que desea: ")
    print()
    
    if(not(tecla.isdigit())):
        print("Digite un numero")
        continue
    i = int(tecla)
    
    if i == 1:
       agregar_nemero_de_vuelo ()
        
    elif i ==2:
        mostrar_vuelos()
        
    elif i ==3 :
        buscar_vuelo_y_eliminar ()
        
    elif i ==4 :
        buscar_vuelo_y_su_posicion ()
        
    elif i ==5 :
        calcular_total_vuelos ()
        
    elif i ==6 :
        print("Se ha salido del sistema")
        break