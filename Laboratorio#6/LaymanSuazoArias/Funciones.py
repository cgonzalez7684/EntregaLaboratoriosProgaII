lista_de_espera = []

def agregar_avion():
    numero_de_vuelo = input("Ingrese el número de vuelo: ")
    avion = input("Ingrese el número del avión: ")
    lista_de_espera.append((numero_de_vuelo, avion))
    print("Avión agregado a la lista de espera.")
    
def mostrar_lista_de_espera():
    if len(lista_de_espera) > 0:
        print("Lista de espera:")
        for i in range(len(lista_de_espera)):
            numero_de_vuelo, avion = lista_de_espera[i]
            print(f"{i+1}. Avion: {avion}, Número de vuelo: {numero_de_vuelo}")
    else:
        print("No hay aviones en la lista de espera.")

def buscar_avion_por_numero():
    numero = input("Ingrese el número del avion: ")
    for i in range(len(lista_de_espera)):
        numero_de_vuelo, avion = lista_de_espera[i]
        if avion == numero:
            print (f"El avion sí se encuentra en la lista de espera en la posición {i+1}")
            return
    print ("El avion no se encuentra en la lista de espera")
        
def calcular_total_aviones():
    total = len(lista_de_espera)
    print("Cantidad de aviones en lista de espera: {0}".format(total))
    
def eliminar_avion():
    numero = input("Ingrese el número del avion: ")
    avion_a_eliminar = None
    for avion in lista_de_espera:
        if avion[1] == numero:
            avion_a_eliminar = avion
            break
    if avion_a_eliminar:
        lista_de_espera.remove(avion_a_eliminar)
        print(f"El avión {numero} ha sido eliminado de la lista de espera")
    else:
        print(f"No hay ningún avión con el número {numero} en la lista de espera")