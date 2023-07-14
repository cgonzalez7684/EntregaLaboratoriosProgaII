from Funciones import agregar_avion, mostrar_lista_de_espera, buscar_avion_por_numero, calcular_total_aviones, eliminar_avion

def Menu():
    while True:
        print(" *** Control De Aviones ***")
        print("1: agregar avion a la lista de espera")
        print("2: mostrar lista de espera")
        print("3: buscar avion en la lista de espera")
        print("4: eliminar avion de la lista de espera")
        print("5: calcular total de aviones en espera")
        print("6: salir del menú")
        while True:
            opc = input("Ingrese el número de la accion que desea realizar:  ")
            if opc.isdigit() and 1 <= int(opc) <= 6:
                break
            print("Opcion inválida, intente de nuevo.")
        
        i = int(opc)
        if i == 1:
            agregar_avion()
            print("")
        elif i == 2:
            mostrar_lista_de_espera()
            print("")
        elif i == 3:
            buscar_avion_por_numero()
            print("")
        elif i == 4:
            eliminar_avion()
            print("")
        elif i ==5:
            calcular_total_aviones()
            print("")
        elif i ==6:
            print("Saliendo del sistema de control de aviones.")
            break
        else:
            print("Opcion inválida")

if __name__ == '__main__':
    Menu()
