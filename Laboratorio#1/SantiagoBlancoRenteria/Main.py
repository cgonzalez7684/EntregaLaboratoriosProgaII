#Aquí pongo un input para que el usuario ingrese el límite hasta donde se calcularán los numeros pares
limite = int(input("Ingrese el límite para evaluar los números pares: ")) 

print("Números pares hasta el límite", limite, ":")

# se inicia en el numero dos hasta el limite y se va sumando 1
for num in range(2, limite + 1): 
    if num % 2 == 0: # Si el residuo es 0
        print(num)  # imprima el numero