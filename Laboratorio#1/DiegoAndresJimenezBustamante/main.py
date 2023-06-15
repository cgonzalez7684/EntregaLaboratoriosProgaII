#Se crea una funcion para determinar si el numero digitado es par

def par (numero):
    #Se verifica que el numero sea par
    if numero < 2 :
        return False
    #Se imprime el numero si es par
    for i in range(1, numero):
        if numero % 2 != 0:
            return False
    return True
#Se le solicita al usuario digitar un numero para determinar la cantidad de numeros pares
limit=int(input("Ingrese un numero para determinar la cantidad de numeros pares "))
#Se realiza un ciclo para que imprima los numeros pares
print("Números Pares hasta el límite", limit, ":")
for a in range(1, limit+1):
    if par(a):
        print(a)