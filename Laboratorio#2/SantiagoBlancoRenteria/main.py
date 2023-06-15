#Le pedimos al usuario que ingrese los datos
longLado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Creamos esta variable para controlar el número de asteriscos en cada fila
numAsteriscos = longLado

# Ciclo while para dibujar el cuadrado
while longLado > 0:
    # Imprimir una fila de asteriscos o con espacios vacios en el medio
    if longLado == numAsteriscos or longLado == 1:
        print("*" * numAsteriscos)
    else:
        print("" + " " * (numAsteriscos - 2) + "")

    # Decrementar el valor del lado para la siguiente fila
    longLado = longLado - 1