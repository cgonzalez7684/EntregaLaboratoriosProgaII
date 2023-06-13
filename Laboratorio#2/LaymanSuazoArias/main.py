lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir una fila de asteriscos o con espacios en blanco en el medio
    if lado == num_asteriscos or lado == 1:
        print("*" * num_asteriscos)
    else:
        print("*" + " " * (num_asteriscos - 2) + "*")

    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1
