# 1. lista "inventario" para almacenar las frutas.
inventario = []

# 2. función "agregar_fruta" para agregar una fruta al inventario.
def agregar_fruta():
    fruta = input("Ingrese el nombre de la fruta: ")
    inventario.append(fruta)
    print("Fruta agregada al inventario.")

# 3. función "mostrar_inventario" para mostrar el inventario de frutas.
def mostrar_inventario():
    print("Inventario de frutas:")
    for fruta in inventario:
        print(fruta)

# 4. función "buscar_fruta_por_nombre" para buscar una fruta en el inventario.
def buscar_fruta_por_nombre():
    fruta = input("Ingrese el nombre de la fruta a buscar: ")
    if fruta in inventario:
        print("La fruta está en el inventario.")
    else:
        print("La fruta no está en el inventario.")

# 5.  función "calcular_total_frutas" para calcular el total de frutas en el inventario.
def calcular_total_frutas():
    total_frutas = len(inventario)
    print("Total de frutas en el inventario:", total_frutas)

# 6.  función "eliminar_fruta" para eliminar una fruta del inventario.
def eliminar_fruta():
    fruta = input("Ingrese el nombre de la fruta a eliminar: ")
    if fruta in inventario:
        cantidad = inventario.count(fruta)
        confirmacion = input(f"Se encontraron {cantidad} {fruta} en el inventario. ¿Desea eliminarlas? (s/n): ")
        if confirmacion.lower() == 's':
            for _ in range(cantidad):
                inventario.remove(fruta)
            print("Fruta(s) eliminada(s) del inventario.")
        else:
            print("No se eliminó ninguna fruta del inventario.")
    else:
        print("La fruta no está en el inventario.")

# Ejecución del programa
while True:
    print("\n------ MENÚ ------")
    print("1. Agregar fruta al inventario")
    print("2. Mostrar inventario")
    print("3. Buscar fruta por nombre")
    print("4. Calcular total de frutas")
    print("5. Eliminar fruta del inventario")
    print("6. Salir del programa")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        agregar_fruta()
    elif opcion == '2':
        mostrar_inventario()
    elif opcion == '3':
        buscar_fruta_por_nombre()
    elif opcion == '4':
        calcular_total_frutas()
    elif opcion == '5':
        eliminar_fruta()
    elif opcion == '6':
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")