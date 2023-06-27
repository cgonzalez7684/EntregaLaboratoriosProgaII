#Modulo para crear la lista de frutas del inventario
import random
# Lista para almacenar las frutas en el inventario
inventario = []

# Metodo para imprimir el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return 
    inventario.sort() 
    print("Inventario:")
    print("Nombre    | Cantidad")
    print("---------------------")
    for fruta in inventario:
        nombre = fruta[0]
        cantidad = fruta[1]
        print(f"{nombre:<10} | {cantidad}")
    print(f"Total: {calcular_total_frutas()}")

# Metodo para rellenar el inventario, solo para debug. :) 
def rellenar_inventario():
    frutas = ["Manzana", "Banana", "Naranja", "Pera", "Sandía", "Uva"]
    num_frutas = random.randint(0, 10)  # Genera un número aleatorio de frutas entre 5 y 10    
    for _ in range(num_frutas):
        fruta = random.choice(frutas)  # Selecciona una fruta aleatoria de la lista de frutas
        cantidad = random.randint(1, 20)  # Genera una cantidad aleatoria entre 1 y 20        
        # Buscar si la fruta ya existe en el inventario
        for item in inventario:
            if item[0] == fruta:
                item[1] += cantidad  # Sumar la cantidad al existente
                break
        else:
            inventario.append([fruta, cantidad])  # Agregar la fruta y cantidad al inventario    
    print("Inventario rellenado con frutas aleatorias.")

# Método para agregar una fruta al inventario
def agregar_fruta():
    while True:
        print("MENU AGREGAR FRUTAS")
        print("1. Agregar fruta")
        print("2. Salir")        
        opcion = input("Ingrese una opción: ")        
        if opcion == "1":
            nombre = input("Ingrese el nombre de la fruta: ")
            for fruta in inventario: # Buscar si la fruta ya existe en el inventario
                if fruta[0].lower() == nombre.lower():
                    manejar_fruta_existente(fruta)
                    break
            else:
                cantidad = int(input("Ingrese la cantidad de frutas: "))
                fruta = [nombre, cantidad]
                inventario.append(fruta) #Agregamos la fruta al inventario
                print("Fruta agregada al inventario.")
        elif opcion == "2":
            print("Saliendo del menú de agregar frutas.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")                         

# Metodo para buscar la fruta. 
def buscar_fruta_por_nombre():
    nombre_buscar = input("Ingrese el nombre de la fruta a buscar: ")
    for fruta in inventario:
        nombre = fruta[0]        
        if nombre.lower() == nombre_buscar.lower(): # Comparamos en minusculas para evitar duplicidad.
            print(f"Hay '{fruta[1]} {nombre_buscar}' en existencias en el inventario.")
            return None
    print(f"No hay existencias de: '{nombre_buscar}' en el inventario.")
    
# Funcion que retorna el total de frutas en el nventario
def calcular_total_frutas():
    total_frutas = 0
    for fruta in inventario:
        cantidad = fruta[1]
        total_frutas += cantidad    
    print(f"El total de frutas en el inventario es: {total_frutas}")

# Metodo para calcular el total de frutas
def calcular_total_frutas():
    total_frutas = 0
    for fruta in inventario:
        cantidad = fruta[1]
        total_frutas += cantidad    
    #print(f"El total de frutas en el inventario es: {total_frutas}")
    return total_frutas
  
# Metodo para eliminar frutas del inventario
def eliminar_fruta():
    nombre = input("Ingrese el nombre de la fruta a eliminar: ")    
    # Buscar la fruta en el inventario
    for fruta in inventario:
        if fruta[0].lower() == nombre.lower():
            manejar_fruta_existente(fruta,accion=3)
            return  
    print(f"No se encontró la fruta '{nombre}' en el inventario.")


# Función para manejar una fruta existente en el inventario
def manejar_fruta_existente(fruta, accion = 0):    
    if accion == 0:
      print(f"La fruta '{fruta[0]}' ya existe en el inventario.")      
      accion = validar_entero("¿Qué acción desea realizar? (1) - Agregar / (2) - Renombrar : ")
      if accion == 1:
          fruta[1] += validar_entero(f"Ingrese la cantidad de {fruta[0]} que desea agregar: ")
          print(f"Cantidad actualizada: {fruta[1]}")
      elif accion == 2:
          nuevo_nombre = input("Ingrese el nuevo nombre de la fruta: ")
          fruta[0] = nuevo_nombre
          fruta[1] += validar_entero(f"Ingrese la cantidad de {fruta[0]} que desea agregar / Digite (0) para omitir: ")
          print(f"Fruta renombrada a '{nuevo_nombre}' y cantidad actualizada: {fruta[1]}")
      else:
          print("Acción inválida. La fruta no fue modificada.")
          return
    elif accion == 3:
      cantidad_eliminar = validar_entero(f"Se encontraron {fruta[1]} unidades de '{fruta[0]}'."
                                      "Ingrese la cantidad a eliminar: ")
      if cantidad_eliminar == fruta[1]:
        inventario.remove(fruta)
        print("La fruta ha sido completamente eliminada del inventario.")
        return
      elif cantidad_eliminar > fruta[1]:
        print("La cantidad a eliminar es mayor que la cantidad disponible en el inventario.")
        return
      else:
        fruta[1] -= cantidad_eliminar
        print(f"Se eliminaron {cantidad_eliminar} unidades de '{fruta[0]}' del inventario.") 
        return
      
#validacion de enteros 
def validar_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Error: Ingrese un número entero válido.")
