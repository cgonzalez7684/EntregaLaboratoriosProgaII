inventario = []
#fui definiendo variables con los solicitado
def agregar_fruta():
    fruta = input("Ingrese el nombre de la fruta: ")
    inventario.append(fruta)
    print("Fruta agregada al inventario.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("Inventario de frutas:")
        for fruta in inventario:
            print(fruta)

def buscar_fruta_por_nombre():
    fruta_buscada = input("Ingrese el nombre de la fruta que desea buscar: ")
    if fruta_buscada in inventario:
        print("La fruta está en el inventario.")
    else:
        print("La fruta no está en el inventario.")

def calcular_total_frutas():
    total_frutas = len(inventario)
    print("El total de frutas en el inventario es:", total_frutas)

def eliminar_fruta():
    fruta_eliminada = input("Ingrese el nombre de la fruta que desea eliminar: ")
    if fruta_eliminada in inventario:
        cantidad = inventario.count(fruta_eliminada)
        print("Se encontraron", cantidad, "frutas", fruta_eliminada, "en el inventario.")
        confirmacion = input("¿Cuántas de estas frutas desea eliminar? ")
        confirmacion = int(confirmacion)
        if confirmacion <= cantidad:
            for i in range(confirmacion):
                inventario.remove(fruta_eliminada)
            print("Frutas eliminadas del inventario.")
        else:
            print("La cantidad ingresada es mayor a la cantidad disponible en el inventario.")
    else:
        print("La fruta no está en el inventario.")
#Main
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar fruta al inventario")
        print("2. Mostrar inventario")
        print("3. Buscar fruta por nombre")
        print("4. Calcular total de frutas")
        print("5. Eliminar fruta del inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_fruta()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_fruta_por_nombre()
        elif opcion == "4":
            calcular_total_frutas()
        elif opcion == "5":
            eliminar_fruta()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
menu()
