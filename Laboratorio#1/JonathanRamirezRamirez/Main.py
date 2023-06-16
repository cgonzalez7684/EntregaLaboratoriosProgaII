def es_par(numero):
    if numero < 2:
        return True
    for i in range(2, numero):
        if numero % 2 == 0:
            return True
    return False
limite = int(input("Ingrese el límite para números pares: "))
print("Números pares hasta el límite", limite, ":")
for num in range(2, limite + 1):
    if es_par(num):
        print(num)
        