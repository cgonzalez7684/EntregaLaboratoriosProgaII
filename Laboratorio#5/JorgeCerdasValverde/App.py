ejecutando = True
total_frutas_inventario = 0
inventario = ["manzana", "pera", "naranja"]

def agregar_fruta():
    print("Ingrese el nombre de la fruta que desea agregar al inventario: ")
    fruta = input()
    inventario.append(fruta.lower())

def mostrar_inventario():
    [print(fruta) for fruta in inventario]

def buscar_fruta_por_nombre():
    print("Ingrese el nombre de la fruta que desea buscar: ")
    fruta = input().lower()
    if fruta in inventario:
        print(f'{fruta} - se encuentra en el inventario')
    else:
        print(f'{fruta} no se encuentra en el inventario')

def calcular_total_frutas():
    total_frutas_inventario = len(inventario)
    print(f'Total de frutas en el inventario es de: {total_frutas_inventario}')

def eliminar_fruta():
    print(f'El total de frutas en el inventario es: {total_frutas_inventario}, desea eliminar una fruta del inventario? Y/N')
    opcion = input()
    if opcion.upper() == 'Y':
        print("Ingrese el nombre de la fruta que desea eliminar del inventario")
        fruta = input()
        inventario.remove(fruta.lower())


def mostrar_opciones():
    print("Opcion A: Agregar fruta al inventario")
    print("Opcion B: Muestra el inventario")
    print("Opcion C: Buscar fruta por nombre")
    print("Opcion D: Calcular el total de frutas en el inventario")
    print("Opcion E: Eliminar fruta del inventario")
    print("Opcion F: Salir del programa")

while(ejecutando):
    mostrar_opciones()
    opcion = input("Ingrese una opcion: ")

    if opcion == "A":
        agregar_fruta()
    elif opcion == "B":
        mostrar_inventario()
    elif opcion == "C":
        buscar_fruta_por_nombre()
    elif opcion == "D":
        calcular_total_frutas()
    elif opcion == "E":
        eliminar_fruta()
    elif opcion == "F":
        print("Terminando programa inventario")
        ejecutando = False  
    else:
        mostrar_opciones()
        opcion = input("Ingrese una opcion: ")
    