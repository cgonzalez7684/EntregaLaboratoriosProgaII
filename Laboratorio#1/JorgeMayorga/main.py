lado = int(input("Ingrese la longitud del lado del cuadrado: "))

num_asteriscos = lado

for i in range(lado):
    print(" *" * num_asteriscos)

    if (i == 2): 
        continue  
          
    
    if (i == lado - 1):
        break