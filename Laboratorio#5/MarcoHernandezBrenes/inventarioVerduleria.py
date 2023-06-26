# Esta función la hice para que reciba un diccionario inventario como argumento. Le pide al usuario que ingrese el nombre de una fruta o verdura, 
# así como una cantidad para esa fruta o verdura. 
# Luego agrega la cantidad ingresada de la fruta o verdura al inventario.

def agregar_fruta_verdura(inventario):
    frutaVerdura = input("Ingrese el nombre de la fruta o verdura: ")
    cantidad = int(input(f"Ingrese la cantidad de  {frutaVerdura} : "))
# La línea inventario[frutaVerdura] = inventario.get(frutaVerdura, 0) + cantidad la uso  para agregar una cierta cantidad de una fruta o verdura al inventario.
# voy a explicarlo por partes, inventario.get(frutaVerdura, 0): El método get() de un diccionario de Python intenta obtener el valor de algo en especifico 
# Aqui intento obtener el valor de la frutaVerdura. Si la  frutaVerdura existe en el diccionario, el método get() devuelve su valor 
# (osea, la cantidad actual de esa fruta o verdura en el inventario). Si la fruta o verdura no existe, el método get() devuelve el segundo argumento que es preguntar por la cantidad 
#  
#inventario[frutaVerdura] = ...: Este valor calculado se asigna de nuevo al diccionario inventario en la clave frutaVerdura. Esto actualiza la cantidad de 
# frutaVerdura en el inventario.

    inventario[frutaVerdura] = inventario.get(frutaVerdura, 0) + cantidad
    
# Esta otra función recibe un diccionario inventario como argumento y luego itera sobre los elementos del inventario, 
# imprimiendo cada fruta o verdura con su correspondiente cantidad, hace la misma logica que explique anteriormente
def mostrar_inventario(inventario):
    for frutaVerdura, cantidad in inventario.items():
        print(f"Producto : {frutaVerdura}, Cantidad: {cantidad}")
# Esta función recibe un dicionario inventario como argumento y solicita al usuario el nombre de una fruta. 
# Luego verifica si la fruta está en el inventario e imprime un mensaje correspondiente.
def buscar_fruta_por_nombre(inventario):
    frutaVerdura = input("Ingrese el nombre de la fruta: ")
    if  frutaVerdura in inventario:
        print(f"La fruta {frutaVerdura} está en el inventario, revisa el inventario para ver la cantidad")
    else:
        print(f"La fruta {frutaVerdura} no está en el inventario.")
# Aqui llamo a la  función que recibe un diccionario inventario y luego suma todas las cantidades de las frutas y verduras en el inventario, imprimiendo el total.
def calcular_total_frutas_verduras(inventario):
    total = sum(inventario.values())
    print(f"El total de frutas/verduras en el inventario es {total}.")
# Aqui jalo el diccionario inventario y solicita al usuario que ingrese el nombre de una fruta. 
# Luego verifica si la fruta está en el inventario. Si está, le pide al usuario que indique cuántas unidades quiere eliminar. 
# Si la cantidad a eliminar es válida, la fruta se elimina del inventario. Si la cantidad no es válida, se imprime un mensaje de error.
def eliminar_fruta(inventario):
    frutaVerdura= input("Ingrese el nombre de la fruta: (Por favor escribir el producto tal y como aparece en el inventario) ") #Aqui le pido al usuario que escriba el producto tal y como sale en el inventario
    if  frutaVerdura in inventario: # Aqui reviso si la fruta o verdura ingresada por el usuario se encuentra en el inventario. La operación in en Python verifica si "algo" "está presente en un diccionario.
        # Aqui intento hacer una  referencia al valor asociado con la clave frutaVerdura en el diccionario inventario. En este caso, esa clave representa una fruta o verdura específica, y el valor asociado es la cantidad actual de esa fruta o verdura en el inventario.
        # Esto lo puedo hacer en python ya que python deja a las cadenas f en Python, son una forma de arreglar las cadenas para que puedan incluir expresiones entre llaves {} que se sustituyen por sus valores al imprimir.
        print(f"Actualmente tienes {inventario[frutaVerdura]} de {frutaVerdura} en el inventario.") 
        cantidad = int(input("¿Cuántas quieres eliminar? ")) #Aqui pido al usuario que introduzca cuántas unidades de la fruta o verdura quiere eliminar.
        if cantidad <= inventario[frutaVerdura]: # Verifica si la cantidad que el usuario quiere eliminar es menor o igual a la cantidad actual en el inventario.
            inventario[frutaVerdura] -= cantidad # Se resta la cantidad ingresada por el usuario a la cantidad actual en el inventario.
            if inventario[frutaVerdura] == 0:
                del inventario[frutaVerdura] # Si la cantidad de la fruta o verdura en el inventario llega a 0 después de la eliminación, la fruta o verdura se elimina completamente del diccionario.
        else:
            print("No puedes eliminar más frutas de las que tienes en el inventario.")
    else:
        print(f"La fruta {frutaVerdura} no está en el inventario.")
# Función principal que se ejecuta cuando se inicia el programa. Define un inventario vacío como un diccionario y luego entra en un ciclo que 
# presenta al usuario un menú de opciones para interactuar con el inventario. Dependiendo de la opción elegida por el usuario, se llama a la funcion que corresponde
def main():
    inventario = {}

    while True:
        print("\n1. Agregar fruta o verdura")
        print("2. Mostrar inventario")
        print("3. Buscar fruta/verdura por nombre")
        print("4. Calcular total de frutas/verduras")
        print("5. Eliminar fruta/verdura")
        print("6. Salir")
        opcion = input("Elija una opción: ")

        if opcion == '1':
            agregar_fruta_verdura(inventario)
        elif opcion == '2':
            mostrar_inventario(inventario)
        elif opcion == '3':
            buscar_fruta_por_nombre(inventario)
        elif opcion == '4':
            calcular_total_frutas_verduras(inventario)
        elif opcion == '5':
            eliminar_fruta(inventario)
        elif opcion == '6':
            break
        else:
            print("Por favor, elija una opción válida.")
# Ya esto lo habia comentando en el LAB4 pero lineas 72 & 73  al final del código verifica si el script se está ejecutando directamente. 
# Si es así, se llama a la función main(). Esta es una práctica común en Python para asegurar que cierto código solo se ejecute cuando un archivo se ejecuta directamente, y no cuando se importa como un módulo.
if __name__ == "__main__":
    main()
