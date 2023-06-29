inventario = []
#Comando necesario para agregar la fruta
def agregar_fruta():
    fruta = input("Ingrese el nombre de la fruta: ")
    inventario.append(fruta)
    print("Fruta agregada correctamente.")

#comando necesario para mostrar las frutas en el inventario
def mostrar_inventario():
    print("Inventario:")
    for fruta in inventario:
        print(fruta)

#Comando necesario para buscar las frutas por nombre dentro del inventario
def buscar_fruta_por_nombre():
    fruta = input("Ingrese el nombre de la fruta a buscar: ")
    if fruta in inventario:
        print("La fruta se encuentra en el inventario.")
    else:
        print("La fruta no se encuentra en el inventario.")

#Comando necesario para calcular el total de frutas en el inventario
def calcular_total_frutas():
    total_frutas = len(inventario)
    print("Total de frutas en el inventario:", total_frutas)

#Comando necesario para eliminar frutas del inventario
def eliminar_fruta():
    fruta = input("Ingrese el nombre de la fruta a eliminar: ")
    if fruta in inventario:
        cantidad = inventario.count(fruta)
        print("Cantidad de", fruta, "en inventario:", cantidad)
        confirmacion = input("¿Está seguro de eliminar todas las frutas de este tipo? (s/n): ")
        if confirmacion.lower() == "s":
            while fruta in inventario:
                inventario.remove(fruta)
            print("Fruta eliminada correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("La fruta no está en el inventario.")

while True:
    print("\n--- Verdulería ---")
    print("1. Agregar fruta")
    print("2. Mostrar inventario")
    print("3. Buscar fruta por nombre")
    print("4. Calcular total de frutas")
    print("5. Eliminar fruta")
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
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
