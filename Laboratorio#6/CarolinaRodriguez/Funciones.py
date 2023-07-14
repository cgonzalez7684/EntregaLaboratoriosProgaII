ListaDeEspera = []

def agregar_ID():
    
    AgregarID = input("Ingrese el ID del avión: ")
    ListaDeEspera.append(AgregarID)

def mostrar_lista():
    
    print(ListaDeEspera)

def borrar_ID():
    
    Borrar = input("Digite el ID del avión que ya ha despegado: ")
    if Borrar in ListaDeEspera:
        ListaDeEspera.remove(Borrar)
    else:
        print("El ID no se encuentra en lista de espera.")

def buscar_ID():
    
    Buscar = input("Ingrese el ID que desea consultar:")
    if Buscar in ListaDeEspera:
        Posicion = ListaDeEspera.index(Buscar)
        print("La posición del avión en espera es:", Posicion + 1)
    else:
        print("El ID que indica no se encuentra en la lista de espera.")
    
def total_aviones():
    
    TotalID = len(ListaDeEspera)
    print("El total de aviones en espera es de: {0}".format(TotalID))