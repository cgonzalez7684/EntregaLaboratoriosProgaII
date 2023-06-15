lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 1:
    # Imprimir una fila de asteriscos
    print("* " * num_asteriscos)
    "este if indica que si el valor ingresado es igual a 3 ingresa al if"
   # if (lado == 3):
      #  continue   """     
    "este if indica que si el valor ingresado es mayor a 3 se detiene"
   # """if (lado > 5):
      #  break"""
    
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1