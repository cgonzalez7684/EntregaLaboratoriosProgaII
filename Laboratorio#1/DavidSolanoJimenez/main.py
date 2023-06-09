def es_primo(numero):
    '''Función para verificar si un número es primo'''
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

limite = int(input("Ingrese el límite para evaluar números primos: "))

print("Números primos hasta el límite", limite, ":")
#2 ... 10 2-3-4-5
for num in range(2, limite + 1):
    if es_primo(num):
        print(num)
