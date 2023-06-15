# Solicitar al usuario el límite superior
limite_superior = int(input("Ingrese el límite superior: "))

# Imprimir números pares hasta el número primo más cercano a 10
for num in range(2, limite_superior + 1, 2):
    print(num)

# Encontrar el número primo más cercano a 10
numero_primo_cercano = 0
for num in range(10, 1, -1):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        numero_primo_cercano = num
        break

# Imprimir el número primo más cercano a 10
print("El número primo más cercano a 10 es:", numero_primo_cercano)