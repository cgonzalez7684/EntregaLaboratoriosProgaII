def agregar_fruta(inventario):
    fruta= input("Por favor, ingrese el nombre de la fruta")
    inventario.append(fruta)
    print("Fruta agregada")
    
def mostrar_inventario(inventario):
    print("inventario: ")
    for fruta in inventario:
        print(fruta)
        
def buscar_fruta_por_nombre(inventario):
    fruta_buscar = input("Ingrese el nombre de la fruta a buscar: ")
    if fruta_buscar in inventario:
        print("La fruta", fruta_buscar, "se encuentra")
    else:
        print("La fruta", fruta_buscar, "no se encuentra.")
        
def calcular_total_frutas(inventario):
    total_frutas = len(inventario)
    print("Total de frutas en el inventario:", total_frutas)

def eliminar_fruta(inventario):
    fruta_delete = input("ingrese el nombre de la fruta que desee eliminar")
    if fruta_delete in inventario:
        cantidad_frutas = inventario.count(fruta_eliminar)
        confirmar = input ("se encontraron{}frutas'{}' en el inventario, desea eliminarlas?(S/N): ".format(ccantidad_frutas, frutas_delete))
    if confirmar.lower() == 's':
        inventario.remove(fruta_eliminar)
        print("Fruta eliminada del inventario.")
    else:
        print("La Fruta fue eliminada del inventario")
        
def main():
     inventario = []
     while True:
         print("Bienvenido al inventario")
         print("1. agregar fruta")
         print("2. Mostrar inventario")
         print("3.Buscar fruta")
         print("4.Calcular el total")
         print("5.Eliminar fruta")
         print("6.salir") 
         
         opcion = input("ingrese una opcion (1-6): ")
         
         if opcion == '1':
             agregar_fruta(inventario)
         elif opcion == '2':
            mostrar_inventario(inventario)
         elif opcion == '3':
            buscar_fruta_por_nombre(inventario)
         elif opcion == '4':
            calcular_total_frutas(inventario)
         elif opcion == '5':
            eliminar_fruta(inventario)
         elif opcion == '6':
            print("¡Hasta luego!")
            break
         else:
         print("Opcion invalida. Por favor, ingrese una opcion valida(1-6)")
if __name__ == "__main__":
    main()           
            
         