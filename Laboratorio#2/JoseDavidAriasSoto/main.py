# Ingresar la longitud del lado del cuadrado
longitud_lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Imprimir cuadrado de asteriscos
for i in range(longitud_lado):
    for j in range(longitud_lado):
        print("*", end=" ")
    print()