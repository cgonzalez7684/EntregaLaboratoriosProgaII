import funciones as FN 

def Main():    #menu
    print("Opcion #1: Ingresar nuevo numero de vuelo a espera")   
    print("Opcion #2: Mostrar aviones en espera")
    print("Opcion #3: Eliminar avion de la lista de espera")
    print("Opcion #4: Buscar avion en la lista de espera")
    print("Opcion #5: Mostrar cantidad total de aviones") 
    print("Opcion #6: Salir")
    
    try:
        while True:
            tecla = input("Digite su numero de opcion: ")
            if not tecla.isdigit():
                print('Debe ser un numero')
                continue
            i = int(tecla)
            if i == 1:           
                #print("Ingrese el nombre de la fruta: ")
                FN.agregar_avion()
            elif i == 2:
                FN.mostrar_aviones_orden_llegada()
            elif i == 3:
                FN.eliminar_avion()
            elif i == 4:
                FN.buscar_aviones()
            elif i == 5:
                FN.mostrar_total_aviones()    
            elif i == 6:
                break
            else:
                print("Opcion invalida")
                continue
    except BaseException:
        print("Finalizo el programa, pulse tecla para cerrar")
        input()        

if __name__ == '__main__':
    Main()        