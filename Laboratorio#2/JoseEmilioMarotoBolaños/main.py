lado = int(input("Ingrese la longitud del lado del cuadraro: "))

# Variable para controlar el nuemero de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir un fila de asteriscos
    print("*" * num_asteriscos)
    
    # Decrementar el valor del lado para la siguiente fila 
    lado = lado - 2