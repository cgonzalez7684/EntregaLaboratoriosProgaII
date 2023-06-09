lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir una fila de asteriscos
    print("*" * num_asteriscos)
    
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1
    
"""if (lado == 3):
        continue    El CONTINUE se utiliza para omitir la parte de un bucle
    
    if (lado > 5):
        break            El BREAK se utiliza para finalizar un bucle""" 