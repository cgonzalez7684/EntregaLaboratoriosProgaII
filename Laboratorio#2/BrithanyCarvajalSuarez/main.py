lado = int(input("Ingrese la longitud del lado del cuadrado: "))

cantidad_asteriscos = lado

while lado > 0:
    print("* " * cantidad_asteriscos)

    if lado <= 1:
        break

    lado = lado - 1