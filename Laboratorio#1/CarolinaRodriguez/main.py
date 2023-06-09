def es_par(numero):
    '''evaluar si el número es par'''
    if numero %2 == 0:
            return True
    else:
            return False 
'''Pedir el limite'''
limite = int(input ("Indique el límite: "))
'''Imprime los números'''
print("Numeros pares: ", limite, ":")

for num in range(1, limite + 1):
    if es_par(num):
        print(num)   
