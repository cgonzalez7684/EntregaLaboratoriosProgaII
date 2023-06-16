lado = int(input("Ingrese la longitud del lado del cuadrado: "))

numero_asteriscos = lado

while lado > 0:
    print("* " * numero_asteriscos)

    if lado <= 1:
        break

    lado = lado - 1