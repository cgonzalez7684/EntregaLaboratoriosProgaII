lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir una fila de asteriscos
    print("*" * num_asteriscos)

    #Hace que el ciclo se quede enciclado cuando lado es igual a 3
    #if (lado == 3):
        #continue        
    
    #Hace que el ciclo se detenga cuando la longitud del lado del cuadrado es mayor a 5
    #if (lado > 5):
     #   break
     
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1
