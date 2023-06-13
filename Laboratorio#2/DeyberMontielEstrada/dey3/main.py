def imprimir_cuadrado_filas(lado):
    for i in range(lado):
        for j in range(lado):
            print("* ", end="")
            if j == lado - 1:
                break
        print()

lado = int(input("Ingresa el tamaño del lado del cuadrado: "))

if lado < 1:
    print("El lado del cuadrado debe ser mayor o igual a 1.")
    exit()

imprimir_cuadrado_filas(lado)
