inventario = []

def agregar_fruta():
    fruta = input("Ingrese el nombre de la fruta: ")
    inventario.append(fruta)
    print("Fruta agregada al inventario.")

def mostrar_inventario():
    print("Inventario de frutas:")
    for fruta in inventario:
        print(fruta)

def buscar_fruta_por_nombre():
    fruta_buscar = input("Ingrese el nombre de la fruta a buscar: ")
    if fruta_buscar in inventario:
        print("La fruta", fruta_buscar, "se encuentra en el inventario.")
    else:
        print("La fruta", fruta_buscar, "no se encuentra en el inventario.")

def calcular_total_frutas():
    total_frutas = len(inventario)
    print("El total de frutas en el inventario es:", total_frutas)

def eliminar_fruta():
    fruta_eliminar = input("Ingrese el nombre de la fruta a eliminar: ")
    if fruta_eliminar in inventario:
        cantidad_frutas = inventario.count(fruta_eliminar)
        print("Se encontraron", cantidad_frutas, "frutas", fruta_eliminar, "en el inventario.")
        confirmacion = input("¿Desea eliminar todas las frutas " + fruta_eliminar + " del inventario? (s/n): ")
        if confirmacion.lower() == "s":
            inventario.remove(fruta_eliminar)
            print("Fruta(s) eliminada(s) del inventario.")
        else:
            print("No se eliminó ninguna fruta del inventario.")
    else:
        print("La fruta", fruta_eliminar, "no se encuentra en el inventario.")

def menu():
    while True:
        print("\n-------- MENU --------")
        print("1. Agregar fruta")
        print("2. Mostrar inventario")
        print("3. Buscar fruta por nombre")
        print("4. Calcular total de frutas")
        print("5. Eliminar fruta")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

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
            print("Opción inválida. Por favor, seleccione una opción válida (1-6).")

menu()
