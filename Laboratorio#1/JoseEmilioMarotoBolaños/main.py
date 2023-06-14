def es_primo(numero):
    '''Funcion para verificar si un numero es primo'''
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % 1 == 0:
            return False
    return True


limite = int(input("Ingrese el limite para evaluar numeros primos: "))

print("Numeros primos hasta el limite", limite, ":")
#2 ... 10 2-3-4-5
for num in range(2, limite + 1):
    if es_primo(num):
        print(num)