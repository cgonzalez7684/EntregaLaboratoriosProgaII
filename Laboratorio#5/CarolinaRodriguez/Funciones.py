InventarioFrutas = []

def agregar_fruta():
    
    AgregarFruta = input("Ingrese la fruta: ")
    InventarioFrutas.append(AgregarFruta)
    
def mostrar_inventario():
    
    print(InventarioFrutas)
    
def buscar_fruta_por_nombre():
    
    Busca = input("Ingrese el nombre de la fruta a buscar: " )
    Encuentra = Busca in InventarioFrutas
    print("Busca {0} en el inventario: Respuesta {1}".format(Busca,Encuentra))
    
def calcular_total_frutas():
    
    TotalFrutas = len(InventarioFrutas)
    print("El total de frutas es: {0}".format(TotalFrutas))
    
def eliminar_fruta():
    
    Eliminar = input("Indique la fruta que desea borrar: ")
    if Eliminar in InventarioFrutas:
            InventarioFrutas.remove(Eliminar)
    else:
            print("La fruta no se encuentra en el inventario")
