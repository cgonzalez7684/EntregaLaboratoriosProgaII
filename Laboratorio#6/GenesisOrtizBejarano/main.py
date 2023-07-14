import funciones

#Se crea el menu para el sistema
def Main():
    
    try:
        while True:
            print("\nMenu")
            print("Opcion #1: Agregar un avion a la lista de espera.")
            print("Opcion #2: Mostar aviones en lista de espera")
            print("Opcion #3: Eliminar aviones de la lista de espera ")
            print("Opcion #4: Buscar un avión por número de vuelo ")
            print("Opcion #5: Mostrar la cantidad de aviones total en la lista de esepra")            
            print("Opcion #6: Salir del sistema\n") 
            tecla = input("Digitar opcion: ")
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)
            if i == 1:
                funciones.agregar_avion()
            elif i==2:                   
                funciones.imprimir_lista()                    
            elif i==3:
                funciones.eliminar_avion()
            elif i==4:
                funciones.buscar_avion()                       
            elif i==5:
                funciones.cantidad_aviones()                         
            elif i==6:
                break                
            elif i==9:
                print("to-do")
            else:
                print('Opcion invalida')
                continue 
    except BaseException:
        print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
        input()
    
if __name__ == '__main__':
    Main()