def es_par(numero):
    """Funcion para ver si el numero es par"""
    if numero % 2 == 0:
            return True
    else:
            return False

# Se le solicita al usuario indicar el limite
limite = int(input("Digite el limite para evaluar los numeros pares: "))  

print("Numeros pares hasta el limite", limite, ":")
for num in range(1, limite + 1):
    if es_par(num):
        print(num)
        
          
          