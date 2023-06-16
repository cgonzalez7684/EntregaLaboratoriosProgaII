def es_par(numero):
    return numero % 2 == 0

limite = int(input("Ingrese el límite para evaluar números: "))

print("Números pares hasta el límite", limite, ":")
for num in range(2, limite + 1):
    if es_par(num):
        print(num)
