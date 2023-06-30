#Lab#5 fruteria

inventario = []

def agregar_fruta ():
    fruta = input("Agregue una fruta:")
    inventario.append(fruta)
    print("La fruta",fruta, "se agrego")

def mostrar_inventario ():
    for fruta2 in inventario:
        print(inventario)
        
def buscar_fruta_por_nombre ():
    try:
        nombre = input("Ingrese el nombre de la fruta: ")
        indice = inventario.index(nombre)
        if (indice >= 0):
            print("La fruta se encuentra en el inventario")
    except BaseException:
        print("La fruta no se encuentra en el inventario")
        
def calcular_total_frutas ():
    cantidadfrutas = len(inventario)
    print("En el inventario hay {0} frutas".format(cantidadfrutas))
    
def eliminar_fruta ():
    
    frutabuscada = [nombrefruta]
    seEncontro = frutabuscada in inventario
    
    nombrefruta = input("Ingrese la fruta que desea eliminar: ")
    
    
    if nombrefruta not in inventario :
            print("La fruta no se encuentra en el inventario")
    
    if inventario[frutabuscada] < 0 :
         del inventario[frutabuscada]
         print("La fruta se elimino")
    

    eliminar = input("Cuantas frutas desea eliminar? ")
    Confirmar = int(eliminar)
    print("Se han eliminado {0} {1} (s) del inventario")
        

print("Opcion #1: Agregar fruta")
print("opcion #2: Mostrar inventario ")
print("Opcion #3: Buscar fruta por nombre")
print("Opcion #4: Total de frutas en el inventario")
print("Opcion #5: Eliminar una fruta")
print("Opcion #6: Salir del menu")
    
while True:
    
    tecla= input("Digite la opcion que desea: ")
    if(not(tecla.isdigit())):
        print("Digite un numero")
        continue
    i = int(tecla)
    
    if i == 1:
       agregar_fruta ()
        
    elif i ==2:
        mostrar_inventario()
        
    elif i ==3 :
        buscar_fruta_por_nombre ()
        
    elif i ==4 :
        calcular_total_frutas ()
        
    elif i ==5 :
        eliminar_fruta ()
        
    elif i ==6 :
        print("Se ha salido del sistema")
        break
    