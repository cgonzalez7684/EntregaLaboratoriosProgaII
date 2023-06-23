inventario = [] # creo una lista vacia 
def menu(): # creo un menu para interactuar con el usuario
    print("#1 Agregar frutas ")
    print("#2 Mostrar el inventario ")
    print("#3 Busque frutas por su nombre ")
    print("#4 Calcular el total de frutas ")
    print("#5 Elimar frutas ")
    print("#6 Salir","\n")
    
def agregar_fruta(): # creo una funcion que solicite al usuario una fruta y agregarla al inventario
    
    fruta = (input("Ingrese una fruta: "))
    numerico = fruta.isnumeric() # uso la funcion isnumeric que me dice si lo que digito es numerico (esto para darle mas funcionabilidad)
    if numerico: 
        print("Opcion invalida no puede digitar numeros dentro de la lista de frutas","\n")
    else:
        inventario.append(fruta)
        print("\n")
    
def mostrar_invantario(): # creo una funcion que me muestre el inventario 
    cantidad_frutas = len(inventario) # uso la funcion len para saber la cantidad de elementos de la lista
    if cantidad_frutas <= 0:
        print("El inventario se encuestra vacio","\n")
    else:
        for cantidad in inventario: # uso un for para que me recorra el inventario y lo muestre por pantalla
            print(cantidad)
        print("\n")    
    
def buscar_fruta_por_nombre(): # creo una funcion que solicita al usuario el nombre de una fruta y lo muestre por pantalla si esta o no 
    fruta = input("Ingrese el nombre de la fruta que desea buscar: ")
    numerico = fruta.isnumeric()# uso la funcion isnumeric que me dice si lo que digito es numerico (esto para darle mas funcionabilidad)
    if numerico:
        print("Opcion invalida no puede buscar numeros dentro de la lista de frutas","\n")
    else:
        try: # uso un try para que me capture si hay algun error ya que el metodo index arroja un error si no encuentra un elemento en su indice
            busqueda = inventario.index(fruta)
            if (busqueda >= 0):
                print("Si tenemos {0} en el inventario".format(fruta))
        except BaseException:
            print("No tenemos {0} en el inventario".format(fruta))
        print("\n")
    
def calcular_total_frutas(): # creo una funcion que cuente y muestre el total de frutas por pantalla
    cantidad_frutas = len(inventario)
    print("La cantidad de frutas que hay en el inventario son: {0}".format(cantidad_frutas),"\n")
    
def eliminar_fruta():
    fruta = input("Ingrese el nombre de la fruta que desea eliminar: ")
    numerico = fruta.isnumeric() # uso la funcion isnumeric que me dice si lo que digito es numerico (esto para darle mas funcionabilidad)
    if numerico:
            print("Opcion invalida no puede buscar numeros dentro de la lista de frutas","\n")
    else:
        try:  # uso un try para que me capture si hay algun error ya que el metodo index arroja un error si no encuentra un elemento en su indice
            busqueda = inventario.index(fruta)
            if(busqueda >=0 ):
                cant_inventario = inventario.count(fruta) # utilizo la funcion count que me indica la cantidad de elementos que coincida con el indice que le pasemos
                print("La cantidad de {0} que hay en el inventario es {1}".format(fruta,cant_inventario))
                eliminar = int(input("Cuantas {0} va a eliminar: ".format(fruta)))
                print("\n")
                for i in range(eliminar): # creo un for que me haga un recorrido en un rango especifico(dado por el usuario)
                    inventario.remove(fruta)
                    print("Se eliminaron con exito las {0} {1} ".format(eliminar,fruta))
        except BaseException:
            print("No tenemos {0} en el inventario".format(fruta))
        print("\n")
        
def datos(): # creo una funcion que me captura los detos que le pido al usuario para interactuar con el y con el programa
    while True:
        menu()
        opcion = input("Elija una opción del menu: ")
        if(not(opcion.isdigit())):
            print("Opcion invalida debe digitar un numero","\n")
            continue
        x = int(opcion)
        if x == 1:
            agregar_fruta()
        elif x == 2:
            mostrar_invantario()
        elif x == 3:
            buscar_fruta_por_nombre()
        elif x == 4:
            calcular_total_frutas()
        elif x == 5:
            eliminar_fruta()
        elif x > 6:
            print("Opcion invalia debe ingresar una de las opciones del menu","\n")
        else:
            break



