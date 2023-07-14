vuelos = [] # creo una lista vacia 

def menu(): # creo un menu para interactuar con el usuario
    print("#1 Agregar numero de vuelo ")
    print("#2 Mostrar lista de espera de los aviones ")
    print("#3 Eliminar vuelo que ya despegó ")
    print("#4 Buscar numero de vuelo ")
    print("#5 Mostrar cantidad de vuelos en la lista de espera ")
    print("#6 Salir","\n")

def agregar_vuelo():
    vuelo = input("Ingrese un numero de vuelo: ")
    numerico = vuelo.isnumeric()
    
    if numerico:
        vuelo = int(vuelo)
        vuelos.append(vuelo)
    else:
        print("Lo siento solo puede asignarle numeros a los vuelos") 
        print("\n")
    
def mostrar_vuelos():
    print("La lista de vuelos que hay, es la siguiente: ")
    for numero_vuelo in vuelos:
        print(numero_vuelo)

def eliminar_vuelo():
    vuelo = input("Elimine el numero de vuelo que ya despegó: ")
    numerico = vuelo.isnumeric()
    
    if numerico:
        vuelo = int(vuelo)
        try:
            despegue = vuelos.index(vuelo) 
            if despegue >=0:
                vuelos.remove(vuelo)
                print("Se elimino con exito el vuelo {0} de la lista ".format(vuelo))
        except  :
            print("No tenemos el vuelo # {0} en la lista".format(vuelo))
        print("\n")
    else:
        print("Lo siento solo puede ingresar numeros para eliminar vuelos") 
        print("\n")
    
    
def busqueda_de_vuelo():
    vuelo = input("Ingrese el numero de vuelo que de sea buscar: ")
    numerico = vuelo.isnumeric()
    if numerico:
        vuelo = int(vuelo)
        try:
            busqueda_vuelo = vuelos.index(vuelo)
            if busqueda_vuelo >=0:
                print("El vuelo numero {0} se encuentra en la posición {1}".format(vuelo,busqueda_vuelo+1))   
        except:
            print("No tenemos el vuelo {0} en la lista".format(vuelo))
            print("\n") 
    else:
        print("Lo siento solo puede ingresar numeros para buscar el vuelo") 
        print("\n")
    
    
    
def cantidad_de_vuelos():
    cantidad_vuelos = len(vuelos)
    print("La cantidad de vuelos que hay en espera son: {0}".format(cantidad_vuelos))
    
def Datos_de_entrada():
    while True:
        menu()
        opcion = input("Ingrese una opcion del menu: ")
        if(not(opcion.isdigit())):
            print("Opcion invalida debe digitar un numero","\n")
            continue
        i = int(opcion)
        
        if i == 1:
            agregar_vuelo()
        
        elif i == 2:
            mostrar_vuelos()
            print("\n")
            
        elif i == 3:
            eliminar_vuelo()
            print("\n")
        elif i == 4:
            busqueda_de_vuelo()
            print("\n") 
        elif i == 5:
            cantidad_de_vuelos()
            print("\n") 
        elif i > 6:
            print("Opcion invalida debe ingresar una de las opciones del menu","\n")
        else:
            break