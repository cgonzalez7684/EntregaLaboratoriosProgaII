from Funciones import agregar_fruta, mostrar_inventario,buscar_fruta_por_nombre,calcular_total_frutas,eliminar_fruta,inventario

def Menu():
    print("Opción 1: agregar fruta al inventario")
    print("Opción 2: mostrar inventario")
    print("Opción 3: buscar fruta fruta en el inventario")
    print("Opción 4: eliminar fruta del inventario")
    print("Opción 5: salir del menú")
    #Creo un try por si acaso se encuentra alguna excepción a la hora de correr el código
    try:
        #Uso un while para que se repita todas las veces que el usuario lo desee
        while True: 
            opc = input("Ingrese el número correspondiente: ")
            #si lo que ingrese el usuario es una letra le dirá que es una opción inválida y reiniciará el ciclo
            if (not(opc.isdigit())):
                print("Opcion inválida")
                continue
            #A i le asignamos el valor de opc para que opc pase a ser un int
            i = int(opc)
            if i == 1:
                agregar_fruta()
            elif i == 2:
                mostrar_inventario()
            elif i == 3:
                buscar_fruta_por_nombre()
            #Si el usuario selecciona esta opción se acabará el ciclo
            elif i == 4:
                eliminar_fruta()
            elif i ==5:
                break
            #Si el usuario ingresa un numéro diferente a los indicados se le dirá que es una opción invalida
            #Y se reiniciaria el ciclo
            else:
                print("Opcion inválida")
                continue     
    except BaseException:
        print("Finalizó el programa, presione cualquier tecla para cerrar la ventana...")
        input()
        
#Aquí ingreso el código de validación para que se reconozca este módulo como el principal
if __name__ == '__main__':
    Menu()

