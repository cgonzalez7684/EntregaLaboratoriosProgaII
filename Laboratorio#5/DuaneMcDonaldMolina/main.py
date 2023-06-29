Inventario = ["melon", "Fresa"]

print("Para el invetantario: agregar fruta")
print("Ver el inventario digite: inventario")
print("Para buscar una fruta: Buscar")
print("Total de frutas digite: Total")
print("Digite salir para terminar el programa\n")

while True:
        opcion = input("Digite opcion: ")
        if (not(opcion.isdigit())):
         print("..") 
        n = str(opcion)       

        if n == "Agregar fruta":
                agregarfruta = input("Ingrese la fruta que desea agregar: ")
                Inventario.append(agregarfruta)
                print("Fruta agregada \n")
                
        elif n == "inventario":
                for frutas in Inventario:      
                 print(frutas)
                 print("\nEste es su inventario\n")
                
        elif n == "Buscar":
            buscarfruta = input("Ingrese la fruta que desea buscar: ")
            if buscarfruta in Inventario:
                print("La fruta", buscarfruta, "está en el inventario\n")
            else:
                 print("La fruta", buscarfruta, "no está en el inventario\n")
                    
        elif n == "Total":
            cantidadfrutas = len(Inventario)
            print("La cantidad de frutas es: " ,cantidadfrutas, "\n")
                
        if n == "Salir":
                print("programa finalizado")    
                break
  