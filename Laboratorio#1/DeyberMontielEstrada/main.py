def es_par(numero):
    #logica para verificar numeros primos
    if numero < 2:
        return False
    for i in range(1,numero):
        if numero % 2 == 0:
            return True
    return False    

limite = int(input("ingrese el límite de números que desea evaluar"))

print("números primos hasta el límite", limite, ":" )
for num in range(2, limite +1):
    if es_par(num):
        print(num)