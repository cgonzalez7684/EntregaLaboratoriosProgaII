def imprimir_cuadrado(lado):
    for i in range(lado):
        for j in range(lado):
            if i == 0 or i == lado - 1:
                print("* ", end="")
            else:
                if j == 0 or j == lado - 1:
                    print("* ", end="")
                else:
                    print("  ", end="")
        print()

lado = int(input("Ingresa el tamaño del lado del cuadrado: "))

if lado < 3:
    print("El lado del cuadrado debe ser mayor o igual a 3.")
    exit()

imprimir_cuadrado(lado)
