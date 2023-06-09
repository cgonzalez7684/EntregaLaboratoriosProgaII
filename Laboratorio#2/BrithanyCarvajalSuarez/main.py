def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_par(numero):
    return numero % 2 == 0

limite = int(input("Ingrese el límite para evaluar números: "))

print("Números pares hasta el límite", limite, ":")
for num in range(2, limite + 1):
    if es_par(num):
        print(num)
