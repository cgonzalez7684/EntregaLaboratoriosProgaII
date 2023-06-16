def es_par(numero):
    '''se verificar si un número es par'''
    if numero %2==0:
        '''si fuera par se imprime el numero'''
        print (numero)
        return True
    
    '''se le pide al usuario  el numero de limite para evaluar los numeros pares'''

limite = int(input("Ingrese el límite para evaluar números pares: "))

'''ciclo for para imprimir los numeros pares'''
print("Números pares hasta el límite", limite, ":")
for num in range(limite + 1):
      es_par(num)
