def es_par(numero):
    '''Función para verificar si un número es par'''
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % 2 != 0:
            return False
    return True

#Ingresar el límite de los números que quiero evaluar
limite = int(input("Ingrese el límite para evaluar números pares: "))

#Imprimir números pares
print("Números pares hasta el límite", limite, ":")

#2 Relizar la veficación en el rango de números
for num in range(2, limite + 1):
    if es_par(num):
        print(num)
