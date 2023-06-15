'''lado = int(input("Ingrese la longitud del lado del cuadrado: "))

num_asteriscos = lado

while lado > 1:
    print("*" * num_asteriscos)

    if (lado == 3):
        continue

    if (lado > 5):
        break
    lado = lado+1'''

lado = int(input("Ingrese la longitud del lado del cuadrado: "))

num_asteriscos = lado

while lado > 0:
    print("* " * num_asteriscos)

    if lado <= 1:
        break

    lado = lado - 1
