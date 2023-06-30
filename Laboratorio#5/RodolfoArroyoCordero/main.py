#Laboratorio 5 Rodolfo Mauricio Arroyo Cordero

#

import Funcion

#
Continuar = True

def Opciones():
    print("Opcion 1: Agregar frutas al Inventario")
    print("Opcion 3: Buscar frutas por nombre")
    print("Opcion 4: Calcular el total de frutas en el Inventario")
    print("Opcion 5: Eliminar frutas del Inventario")
    print("Opcion 6: Salir del Inventario")

while(Continuar):
    Opciones()
    opcion = input("Ingrese una opcion: ")
    print

    if opcion == "1":
        Agregar_Fruta()
    elif opcion == "2":
        Buscar_Fruta_por_Fruta()
    elif opcion == "3":
        Eliminar_Fruta()
    elif opcion == "4":
        Mostrar_Inventario()
    elif opcion == "5":
        Calcular_Total_Frutas()
    elif opcion == "6":
        print("Desea salir del Inventario")
        Continuar = False
    
    