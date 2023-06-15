side =  int(input("Acceda la longitud del lado del cuadrado:"))

#variable para controlar el numero asteriscos en cada fila
num_asterisk = side

#bucle while para dibujar el cuadrado
while side > 0:
    #imprimir una linea de asteriscos
    print("* " *num_asterisk) 
    
    #if (side == 3):
        #contine
    
    if (side==0):
        break
    #Decrementa el valor  lados para siguiente fila
    side -=1  
        