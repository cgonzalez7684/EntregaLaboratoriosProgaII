# Lab2 KevinFabianSequeiraBadilla

lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir una fila de asteriscos
    # Se multiplica por 2 el numero de asteriscos para que se forme el cuadrado
    print("*" * num_asteriscos*1)
    # Decrementar el valor del lado para la siguiente fila y asi controlar el ciclo
    lado = lado - 1
    if (lado == 3):
        continue

    if (lado == 0):
        break
