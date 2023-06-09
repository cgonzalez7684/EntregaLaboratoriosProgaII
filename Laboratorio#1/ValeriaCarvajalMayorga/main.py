def es_par(numero):
    '''Función para verificar si un número es par'''
   
    for i in range(0, numero+1):
        if i % 2 == 0:
            print(i)
    

limite = int(input("Ingrese el límite para evaluar números pares: "))

print("Números pares hasta el límite", limite, ":")

es_par(limite)

