def es_pares(numero):
    #Funcion para evaluar si el numero ingresado es par
    if num % 2 == 0: #Aqui verificamos si el numero es divisible entre 2, si lo es, es par
        return True    
    else:
        return False
    
#Se le solicita al usuario indicar el limite
limite = int(input("Ingrese el límite para evaluar números pares: "))

#Se imprimen los numeros pares hasta el limite definido
print("Números pares hasta el límite", limite, ":")
for num in range(1, limite + 1):
    if es_pares(num):
        print(num)
