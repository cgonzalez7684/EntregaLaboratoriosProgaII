inventario = []

def agregar_fruta():
    fruta = input("Ingrese el nombre de la fruta a agregar: ")
    inventario.append(fruta)  
    
def  mostrar_inventario():
    for fruta in inventario:
        print(fruta)
    
def buscar_fruta_por_nombre():
    
    try:  
         nombre = input("ingrese el nombre de la fruta a buscar: ")
         indice = inventario.index(nombre)
         if (indice > 0):
            print("El producto si esta en inventario")   
    except BaseException:
        print("El producto no se encuentra en inventario")
        
def calcular_total_frutas():
    totalFrutas = len(inventario)
    print("El total de frutas en inventario {0}".format(totalFrutas))
    
def eliminar_fruta():
     fruta = input("Ingrese el nombre de la fruta a eliminar: ")
     contadorFruta = inventario.count(fruta)
     
     if(contadorFruta > 1):
         print("Existen {0} productos de ese nombre".format(contadorFruta))
         selection = int(input("cuantos elementos desea eliminar: "))
        
        
def eliminar_fruta():
    fruta = input("Ingrese el nombre de la fruta a eliminar: ")
    
    if fruta in inventario:
        inventario.remove(fruta)
    else:
        print("La fruta no esta en el inventario")