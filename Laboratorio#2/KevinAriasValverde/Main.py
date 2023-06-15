'''Correcion de errores en el codigo'''

lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado >= 1:
    # Imprimir una fila de asteriscos
    print("*" * num_asteriscos)
    
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1
