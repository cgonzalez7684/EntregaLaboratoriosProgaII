import funciones as FN

def Main():    #menu
    print("Opcion #1: Ingresar nueva fruta")   
    print("Opcion #2: Mostrar inventario")
    print("Opcion #3: Buscar fruta por nombre")
    print("Opcion #4: Eliminar fruta") 
    print("Opcion #5: Salir")
    
    try:
        while True:
            tecla = input("Digite su numero de opcion: ")
            if not tecla.isdigit():
                print('Debe ser un numero')
                continue
            i = int(tecla)
            if i == 1:           
                #print("Ingrese el nombre de la fruta: ")
                FN.agregar_fruta()
            elif i == 2:
                FN.mostrar_inventario()
            elif i == 3:
                FN.buscar_fruta_por_nombre()
            elif i == 4:
                FN.eliminar_fruta()
            elif i == 5:
                break
            else:
                print("Opcion invalida")
                continue
    except BaseException:
        print("Finalizo el programa, pulse tecla para cerrar")
        input()        
        
if __name__ == '__main__':
    Main()