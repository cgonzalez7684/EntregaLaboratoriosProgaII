
ListaDeEspera = []
contador = 1
print("Si llegó un nuevo avion, digita: Agregar")
print("Para ver la lista de aviones, digita: Ver lista")
print("Para eliminar un avión de la lista, digita: Eliminar")
print("Para buscar un avión en la lista, digita: Buscar")
print("Para ver el total de aviónes en lista de espera, digita: Total")
print("Digite ´Salir´ para finalizar el programa")

while True:
            opcion = input("Digite opcion: ")
            if (not(opcion.isdigit())):
                print("..") 
            n = str(opcion)
            
            if n == "Agregar":
                agregaravion = input("Ingrese el codigo de vuelo del nuevo avión:") 
                ListaDeEspera.append(agregaravion)
                print("Avión agregado con exito\n")
            
            elif n == "Ver lista":
                if len(ListaDeEspera) == 0:
                    print("La lista de espera está vacía.")
                else:
                    print("Lista de espera de aviones:")
                    for i, avion in enumerate(ListaDeEspera, start=contador):
                     print(f"{i}- {avion}")
                     
            elif n == "Eliminar":
                eliminaravion = input("Ingrese el código de vuelo del avión a eliminar: ")
                if eliminaravion in ListaDeEspera:
                    ListaDeEspera.remove(eliminaravion)
                    print("Avión eliminado de la lista de espera\n")
                else:
                 print("El avión no se encuentra en la lista de espera\n")
                                 
            elif n == "Buscar":
                buscaravion = input("Ingrese el código de vuelo del avión a buscar: ")
                if buscaravion in ListaDeEspera:
                    posicion = ListaDeEspera.index(buscaravion) + 1
                    print(f"El avión con código de vuelo {buscaravion} se encuentra en la posición {posicion} de la lista de espera\n")
                else:
                    print("El avión no se encuentra en la lista de espera\n")
            elif n == "Total":
                totaldeaviones = len(ListaDeEspera)
                print(f"La cantidad de aviones en la lista es {totaldeaviones}\n")
                
            if n == "Salir":
                print("Hasta pronto")
                break
                              
            
