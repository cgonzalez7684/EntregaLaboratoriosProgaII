Listaespera = []

def agregarId():
    AgregarId = input("Ingrese el Id del avion: ")
    Listaespera.append(AgregarId)
    
def mostrar_lista():
    print(Listaespera)
        
def borrarId():
    Borrar = input("Digite el Id del avion que despego: ")
    if Borrar in Listaespera:
        Listaespera.remove(Borrar)
    else:
        print("El Id no se encuentra en lista de espera.")
            
def buscarId():
    buscar = input("Ingrese el Id que desea consultar: ")
    if buscar in Listaespera:
        posicion = Listaespera.index(buscar)
        print("El lugar del avion en espera es", posicion + 1)
    else:
        print("El Id que registro no se encuentra en lista de espera")
        
def Totalaviones():
    TotalId = len(Listaespera)
    print("El total de aviones en espera es de:", TotalId)
    
def salir():
    print("Saliendo del programa...")
    # Puedes agregar aquí cualquier código adicional que necesites antes de salir.
    exit()

def menu():
    print("1- Digite Id del avion")
    print("2- Observar lista de espera") 
    print("3- Eliminar Id") 
    print("4- Ver posicion de espera de los aviones")
    print("5- Observar el total de aviones")
    print("6- Salir del menu")
   
    while True:
        numero = input("Digite el número de opción: ")
       
        if not numero.isdigit():
            print("Digite una opción válida.")
            continue 
        
        option = int(numero)
   
        if option == 1:
            agregarId()
        elif option == 2:
            mostrar_lista()
        elif option == 3:
            borrarId()
        elif option == 4:
            buscarId()
        elif option == 5:
            Totalaviones()
        elif option == 6:
            salir()
        else:
            print("La opción no es permitida, ingrese una opción válida.")

menu()
