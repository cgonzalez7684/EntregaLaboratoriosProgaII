# CodigoLab5Progra2KevinFabianSequeiraBadilla


# aca esta la parte que es para agregar una fruta al inventario
def agregar_fruta():
    nombre = input("Ingrese el nombre de la fruta: ")
    inventario.append(nombre)
    print("Fruta agregada al inventario.")


# esta es para mostrar todo el inventario
def mostrar_inventario():
    print("Inventario de la verdulería:")
    for fruta in inventario:
        print(fruta)


# esto es para buscar una fruta por su nombre
def buscar_fruta_por_nombre():
    nombre = input("Ingrese el nombre de la fruta a buscar: ")
    if nombre in inventario:
        print("La fruta", nombre, "se encuentra en el inventario.")
    else:
        print("La fruta", nombre, "no se encuentra en el inventario.")


# esto se usa para calcular el total de frutas en el inventario
def calcular_total_frutas():
    total = len(inventario)
    print("Total de frutas en el inventario:", total)


# aqui se elimina una fruta del inventario ( o todas )
def eliminar_fruta():
    nombre = input("Ingrese el nombre de la fruta a eliminar: ")
    if nombre in inventario:
        cantidad = inventario.count(nombre)
        print("Se tienen", cantidad, "frutas", nombre, "en el inventario.")

        confirmacion = input(
            "¿Desea eliminar todas las frutas " + nombre + "? (S/N): ")
        if confirmacion.upper() == "S":
            inventario[:] = [f for f in inventario if f != nombre]
            print("Frutas eliminadas del inventario.")
        else:
            while True:
                eliminar_cantidad = input(
                    "Ingrese la cantidad de frutas " + nombre + " a eliminar (0 para cancelar): ")
                if eliminar_cantidad.isdigit():
                    eliminar_cantidad = int(eliminar_cantidad)
                    if eliminar_cantidad > 0:
                        if eliminar_cantidad <= cantidad:
                            for _ in range(eliminar_cantidad):
                                inventario.remove(nombre)
                            print(eliminar_cantidad, "frutas", nombre,
                                  "eliminadas del inventario.")
                            break
                        else:
                            print(
                                "La cantidad ingresada supera la cantidad de frutas", nombre, "en el inventario.")
                    elif eliminar_cantidad == 0:
                        print("Eliminación cancelada.")
                        break
                    else:
                        print("La cantidad ingresada debe ser mayor a cero.")
                else:
                    print("Ingrese un numero valido.")
    else:
        print("La fruta", nombre, "no se encuentra en el inventario.")


# aqui esta el " menu "  ( esto es lo que el usuario ve )
inventario = []
while True:
    print("\n--- GESTION DE INVENTARIO DE VERDULERIA ---")
    print("1. Agregar fruta")
    print("2. Mostrar inventario")
    print("3. Buscar fruta por nombre")
    print("4. Calcular total de frutas")
    print("5. Eliminar fruta")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

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
        print("Hasta luego")
        break
    else:
        print("Opcion invalida. Por favor seleccione una opcion valida.")
