# Laboratorio 2

lado = int(input("Ingrese la longitud del lado del cuadrado: "))
# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado
# Bucle while para dibujar el cuadrado
while lado > 0:
    # Imprimir una fila de asteriscos
    print("*" * (num_asteriscos*2))    
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1
    '''
    Si el lado es igual al numero 3,
    continua el cilo "While" a la siguiente iteracion
    '''
    if (lado == 3):
        continue          
    '''
    Si el lado es igual a 0,
    Va a detener el ciclo 
    '''    
    if (lado == 0):
        break
  