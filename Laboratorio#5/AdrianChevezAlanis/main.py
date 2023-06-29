InventarioFrutas = []

def introducirfruta():
    
    introducirFruta = input("Ingrese nombre de la fruta: ")
    InventarioFrutas.append(introducirFruta)
    
def mostrar_inventario():
    
    print(InventarioFrutas)
    
def buscarFruta():
    
    Busca = input("Ingrese el nombre de la fruta: " )
    Encuentra = Busca in InventarioFrutas
    print("Busca {0} en el inventario: Respuesta {1}".format(Busca,Encuentra))
    
def calcular_total_frutas():
    
    TotalFrutas = len(InventarioFrutas)
    print("El total de frutas es: {0}".format(TotalFrutas))
    
def eliminar_fruta():
    
    Eliminar = input("digite la fruta a eliminar: ")
    if Eliminar in InventarioFrutas:
            InventarioFrutas.remove(Eliminar)
    else:
            print("La fruta no se encuentra en el inventario")
    