import Funciones as Funcion

def menu():
 print("1. Agregar fruta.")
 print("2. Ver inventario.")
 print("3. Buscar fruta.")
 print("4. Total Frutas.")
 print("5. Eliminar frutas.")
 print("6. Salir")
 
 while True:
     
    numero = input("Digite una opción")
    
    if (not(numero.isdigit())):
        print("Digite una opción")
        continue
    option = int(numero)
    
    if option == 1:
        
       Funcion.agregar_fruta()
       
    elif option == 2:
       
       Funcion.mostrar_inventario()
        
    elif option == 3:
        
        Funcion.buscar_fruta_por_nombre()
        
    elif option == 4:
        
        Funcion.calcular_total_frutas()
    
    elif option == 5:
        
        Funcion.eliminar_fruta()
    
    elif option == 6:
        break
    else:
        print("Opción no valida")
        
    if __name__ == '__main__':
        menu()

