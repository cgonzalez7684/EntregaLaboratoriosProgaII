def numeros_pares(limite):
    for i in range(2,limite+1,2):
        print(i)
        
limite = int(input("ingrese el numero limite para evaluar pares: "))
numeros_pares(limite)