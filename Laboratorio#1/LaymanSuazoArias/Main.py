limite = int(input("Ingrese el límite para evaluar números pares: ")) #Input para ingresar el limite hasta donde se calcularan los numeros pares

print("Números pares hasta el límite", limite, ":")

for num in range(2, limite + 1): # se inicia en el numero dos hasta el limite y se va sumando 1
    if num % 2 == 0: # Si el residuo es 0
        print(num)  # imprima el numero