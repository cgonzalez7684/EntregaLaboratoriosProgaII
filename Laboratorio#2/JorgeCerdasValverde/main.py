lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado >= 1:
    # Imprimir una fila de asteriscos
    print(" * " * num_asteriscos)
    #Este codigo causa que el ciclo WHILE se encicle debido a que en el momento que lado es igual a 3 entramos al cuerpo del IF 
    #y se ejecuta el continue lo cual hace q la ejecucion vuelva al inicio del WHILE LOOP
    # if (lado == 3): 
    #     continue        
    
    #Este codigo en principio causaba que el ciclo WHILE se detuviera con la ejecucion del BREAK cuando lado era mayor a 5
    # if (lado > 5):
    #     break
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1 #Reducimos lado por 1 cada vez que corre el ciclo WHILE LOPP con el fin de detener el ciclo, cuando lado sea menor o igual a 1
