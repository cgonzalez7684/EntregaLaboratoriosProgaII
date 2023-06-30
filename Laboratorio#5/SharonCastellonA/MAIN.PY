inventario = ["Manzna","Fresa"]

print("Para agregar una fruta al inventario digita: Agregar fruta")
print("Para ver el inventario digita: Ver inventario")
print("Para buscar una fruta digita: Buscar fruta")
print("Para ver el total de frutas digita: Total")
print("Digite Salir para terminar el programa\n")

while True: 
            opcion = input("Digite opcion: ")
            if (not(opcion.isdigit())):
                print("..") 
            n = str(opcion)       

            if n == "Agregar fruta":
                agregarfruta = input("Ingrese el nombre de la fruta a agregar: ")
                inventario.append(agregarfruta)
                print("Fruta agregada \n")
                
            elif n == "Ver inventario":
                for frutas in inventario:      
                 print(frutas)
                print("\nEste es su inventario\n")
                
            elif n == "Buscar fruta":
                buscarfruta = input("Ingrese el nombre de la fruta para ver si se encuentra en nuestro inventario: ")
                if buscarfruta in inventario:
                    print("La fruta", buscarfruta, "está en el inventario\n")
                else:
                    print("La fruta", buscarfruta, "no está en el inventario\n")
                    
            elif n == "Total":
                cantidadfrutas = len(inventario)
                print("La cantidad de frutas es: " ,cantidadfrutas, "\n")
                
            if n == "Salir":
                print("Saliendo del programa")    
                break
  