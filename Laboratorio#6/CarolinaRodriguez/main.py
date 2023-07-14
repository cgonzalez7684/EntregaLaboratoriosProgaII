import Funciones as FN

def menu():
    print("SISTEMA DE CONTROL DE AVIONES.")
    print("1- Agregar ID del avión en espera.")
    print("2- Desplegar lista de espera.")
    print("3- Borrar ID.")
    print("4- Ver posición de un avión en espera.")
    print("5- Ver total de aviones en espera.")
    print("6- Salir.")
    
    while True:
        
        numero = input("Digite una opción")
        
        if (not(numero.isdigit())):
            print("Digite una opción")
            continue
        option = int(numero)
        
        if option == 1:
            
            FN.agregar_ID()
        
        elif option == 2:
            
            FN.mostrar_lista()
        
        elif option == 3:
            
            FN.borrar_ID()
        
        elif option == 4:
            
            FN.buscar_ID()
            
        elif option == 5:
            
            FN.total_aviones()
        
        elif option == 6:
            break
        else:
            print("La opción no es válida, vuelva a intentarlo.")
            
if __name__ == '__main__':
    menu()
            