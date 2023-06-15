def imprimir_numeros_pares(limite):

    # La función recibe un límite como argumento e imprime los números pares
    # desde 0 hasta el límite (incluido).

    for i in range(limite + 1):
        if i % 2 == 0:
            print(i)


# Solicitar al usuario el límite
limite = int(input("Ingrese hasta que numero desea los numeros pares: "))

# Llamar a la función para imprimir los números pares
print("Los numeros pares son: ")
imprimir_numeros_pares(limite)
