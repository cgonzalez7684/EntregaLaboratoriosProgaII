inventario = []
#Funcion Agregar
def agregar_fruta():
    fruta = input("Ingrese el nombre de la fruta: ")
    inventario.append(fruta)
    print("Fruta agregada correctamente.")


#Funcion Mostrar
def mostrar_inventario():
    print("Inventario:")
    for fruta in inventario:
        print(fruta)


#Funcion de busqueda
def buscar_fruta_por_nombre():
    fruta = input("Ingrese el nombre de la fruta a buscar: ")
    if fruta in inventario:
        print("Se ha encontrado la fruta.")
    else:
        print("Fruta no disponible.")


#Funcion para el total de frutas
def calcular_total_frutas():
    total_frutas = len(inventario)
    print("Total de frutas en el inventario:", total_frutas)


#Funcion Eliminar
def eliminar_fruta():
    fruta = input("Ingrese la fruta que desea eliminar: ")
    if fruta in inventario:
        cantidad = inventario.count(fruta)
        print("Cantidad de", fruta, "en inventario:", cantidad)
        confirmacion = input("¿Está seguro de desea eliminar la fruta? (s/n): ")
        if confirmacion.lower() == "s":
            while fruta in inventario:
                inventario.remove(fruta)
            print("Fruta eliminada correctamente.")
        else:
            print("Cancelado.")
    else:
        print("La fruta no está en el inventario.")

while True:
    print("1. Agregar fruta")
    print("2. Mostrar inventario")
    print("3. Buscar fruta")
    print("4. Calcular cantidad de frutas")
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
        break
    else:
        print("Opción no valida.")