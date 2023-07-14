#Creo una lista vacía para poder agregar los número de vuelos
avion=[]

#Función para agregar aviones por su número de vuelo
def agregar (avion):
    vuelo = input("Ingrese número de vuelo: \n")
    avion.append(vuelo)

#Método para recorrer y mostar la lista de aviones/vuelos   
def mostrar_lista (avion):
    print("--------------------Lista de aviones en espera de despegue--------------------")
    for vuelo in avion:
        print(vuelo)
    print("\n")
#Función para verificar si el primer avión en la lista ya sale de vuelo y eliminarlo de la lista   
def salida(avion):
    print("El primer avión de la lista es {0}. ¿Desea registrar su salida?".format(avion [0]))
    print("Presione 1 para confirmar o 0 para denegar")
    opc = input()
    if opc.isdigit():
        opc = int(opc)
        if (opc > 1) or (opc < 0):
            print("Opción no válida, intente de nuevo")
        else:
            if opc == 1:
                print("El avión {0} se ha eliminado de la lista de espera de despegue".format(avion [0]))
                del avion [0]
            else:
                print("El avión {0} continua en la lista de espera".format(avion [0]))
    else:
        print ("Debe ingresar un dígito y no un caracter")
        
#Método para buscar el avion y visualizar su posición       
def buscar(avion):
    busqueda = input("Ingrese número de avión / vuelo: ")
    #Verifico si lo digitado se encuentra en la lista de aviones:
    if (busqueda in avion) == True:
        for i in range (len(avion)):
            if avion [i] == busqueda:
                print("El avion {0} se encuentra en la lista en la posición {1}".format(busqueda, (i+1)))
    else:
        print("El número ingresado no existe dentro de la lista de espera de despegue")

#Método para ver la cantidad de aviones en espera para su vuelo
def cantidad(avion):
    print("La cantidad de aviones en espera de vuelo son: {0}".format(len(avion)))
    
def menu(lista = avion):
    opc =0
    while (opc !=6):
        print("__________________ Opciones de lista de espera de despegue __________________\n")
        print("1) Agregar avión en lista de espera")
        print("2) Mostrar lista de aviones en espera")
        print("3) Registrar salida del avión")
        print("4) Buscar avión en lista de espera")
        print("5) Ver la cantidad de aviones en espera")
        print("6) Salir")
        
        opc = input("Ingrese una Opción \n")
        if (opc.isdigit()): #Verifico si la opción es numérica
            opc = int(opc) #Convierto el dato ingresado de Str a Int
            if opc == 1:
                agregar(lista)
            elif opc == 2:
                mostrar_lista(lista)
            elif opc == 3:
                salida(lista)
            elif opc == 4:
                buscar(lista)
            elif opc == 5:
                cantidad(lista)
            elif opc > 6: # Si el usuario ingresa un opción fuera del menu
                print("Opción inválida")
        else:
            print("Debe ingresar dígitos y no caracteres. Inténtelo de nuevo \n")

menu()