def par (numero):
    if numero < 2 :
        return False
    for i in range(1, numero):
        if numero % 2 != 0:
            return False
    return True
    
limit=int(input("Ingrese un numero para emplearlo como limite y evaluar los numeros pares dentro del limite "))
print("Números Pares hasta el límite", limit, ":")
for a in range(1, limit+1):
    if par(a):
        print(a)