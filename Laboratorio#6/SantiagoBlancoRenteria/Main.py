from Funciones import agregar_avion, mostrar_lista, buscar_avion, eliminar_avion, total_aviones, ListaEspera

def Menu():
    print("Opción 1: agregar avión a la lista de espera")
    print("Opción 2: mostrar aviones en la lista de espera")
    print("Opción 3: buscar posición del avion en la lista de espera")
    print("Opción 4: eliminar avión de la lista de espera")
    print("Opción 5: mostrar cantidad de aviones en la lista de espera")
    print("Opción 6: salir del menú")
    
    try:
        while True: 
            opc = input("Ingrese el número correspondiente: ")
            
            if (not(opc.isdigit())):
                print("Opcion inválida")
                continue
            i = int(opc)
            if i == 1:
                agregar_avion()
            elif i == 2:
                mostrar_lista()
            elif i == 3:
                buscar_avion()
            elif i == 4:
                eliminar_avion()
            elif i == 5:
                total_aviones()
            elif i == 6:
                break
            else:
                print("Opcion inválida")
                continue     
    except BaseException:
        print("Finalizó el programa, presione cualquier tecla para cerrar la ventana...")
        input()
        
if __name__ == '__main__':
    Menu()