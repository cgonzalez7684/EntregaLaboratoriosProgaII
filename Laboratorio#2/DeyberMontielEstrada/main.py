# bucle de for anidados para dibujar el cuadrado
def imprimir_cuadrado_filas(lado):
    for i in range(lado):
        for j in range(lado):
            print("* ", end="")
            if j == lado - 1:
                break
        print()

lado = int(input("ingrse la longitud del lado del cuadrado"))

if lado < 1: 
    #impresion del mensaje si el numero de lados es menor a 1
    print ("el lado debe de ser mayor o igual a 1")
    exit()

#impresion del cuadrado de asteriscos en filas
imprimir_cuadrado_filas(lado)
     