# Laboratorio 4
import inventario

def Main():
    try:
        while True:
            print("\nMenu")
            print("Opcion #1: Imprimir Inventario.")
            print("Opcion #2: Agregar Frutas.")
            print("Opcion #3: Buscador de frutas por nombre ")
            print("Opcion #4: Total de frutas ")
            print("Opcion #5: Eliminar fruta del inventario ")            
            print("Opcion #6: Salir \n") 
            tecla = input("Digitar opcion: ")
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)
            if i == 1:
                inventario.mostrar_inventario()
            elif i==2:
                inventario.agregar_fruta()                         
            elif i==3:
                inventario.buscar_fruta_por_nombre()
            elif i==4:
                print(f"El total de frutas en el inventario es: {inventario.calcular_total_frutas()}")                         
            elif i==5:
                inventario.eliminar_fruta()                         
            elif i==6:
                break                
            elif i==9:
                inventario.rellenar_inventario()
            else:
                print('Opcion invalida')
                continue 
    except BaseException:
        print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
        input()
if __name__ == '__main__':
    Main()
    