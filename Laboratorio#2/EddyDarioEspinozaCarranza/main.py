lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir una fila de asteriscos
    print("*" * num_asteriscos *2)
#hacemos que en el print se multiplique en 2 para que se forme en cuadrado 
    lado=lado -1 
    # Decrementar el valor del lado para la siguiente fila
    if (lado ==2):
    
        continue        
    
    if (lado == 0):
        break
    # Decrementar el valor del lado para la siguiente fila
    
