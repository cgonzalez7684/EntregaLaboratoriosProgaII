lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 1:
    # Imprimir una fila de asteriscos
    print("*" * num_asteriscos)

    if (lado == 3):
        #continue        
    # break para el ciclo cuando termina de darse la condición
     if (lado > 5):
        break
    # Decrementar el valor del lado para la siguiente fila
    lado = lado -  1
