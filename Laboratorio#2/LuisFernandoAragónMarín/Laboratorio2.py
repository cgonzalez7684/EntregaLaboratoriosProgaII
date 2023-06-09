# Con la funcion input, ingresamos la longitud del lado del cuadrado, con int, el dado ingresado se convierte en la longitud del cuadro

longitud = int(input("Ingrese la longitud del lado del cuadrado: "))

# con nuestro bucle for, iteramos las filas del cuadradro, la variable i se usa como contador para el bucle y toma valores de 0 en adelante
for i in range(longitud):
    # Este for se encarga de imprimir la fila de asteriscos, la variable j funciona como contadore y toma valores de 0 para adelante. print imprime las dimensiones del cuadrado utilizando los asteriscos
    for j in range(longitud):
        print("**", end="")
    print()  