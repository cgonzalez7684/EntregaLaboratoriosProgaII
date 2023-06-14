lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable pára controlar el numero de asteriscos en cada fila
num_asteristicos = lado

# Bucle while para dibujar el cuadrado
while lado > 1:
    # Imprimir una fila de asteriscos
    print("*" * num_asteristicos)
    
    if (lado ==3):
        continue
    
    if(lado > 5):
        break
    # Decrementar el valor del lado para la siguente fila
    lado = lado + 1
    