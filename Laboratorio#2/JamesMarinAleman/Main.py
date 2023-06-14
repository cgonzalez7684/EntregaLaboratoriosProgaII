"""
name = str (input("Digite su nombre... : "))
print ("Hola ",name , " es un placer")
"""

lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir una fila de asteriscos
    print(" * " * num_asteriscos)

    #si justo colocamos 3 esto continua infinitamente
    """
    if (lado == 3):
        continue        
    """
    #si es mayor a 10 se sale del programa
    if (lado > 10):
        break   
    
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1
