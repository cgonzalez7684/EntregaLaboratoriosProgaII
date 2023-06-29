inventario = ["Pera","Uva"]

print("modificar el inventario: Agregar fruta")
print("ver el inventario digite: inventario")
print("Para buscar una fruta: Buscar")
print("total de frutas digita: Total")
print("Digite Salir para terminar el programa\n")

while True: 
            opcion = input("Digite opcion: ")
            if (not(opcion.isdigit())):
                print("..") 
            n = str(opcion)       

            if n == "Agregar fruta":
                agregarfruta = input("Ingrese la fruta que desea agregar: ")
                inventario.append(agregarfruta)
                print("Fruta agregada \n")
                
            elif n == "inventario":
                for frutas in inventario:      
                 print(frutas)
                print("\nEste es su inventario\n")
                
            elif n == "Buscar":
                buscarfruta = input("Ingrese la fruta que desea buscar: ")
                if buscarfruta in inventario:
                    print("La fruta", buscarfruta, "está en el inventario\n")
                else:
                    print("La fruta", buscarfruta, "no está en el inventario\n")
                    
            elif n == "Total":
                cantidadfrutas = len(inventario)
                print("La cantidad de frutas es: " ,cantidadfrutas, "\n")
                
            if n == "Salir":
                print("programa finalizado")    
                break
  
  