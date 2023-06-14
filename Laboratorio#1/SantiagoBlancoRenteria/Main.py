#Aquí pongo un input para que el usuario ingrese el límite hasta donde se calcularán los numeros pares
limite = int(input("Ingrese el límite para evaluar los números pares: ")) 

print("Números pares hasta el límite", limite, ":")

# Se inicia con el numero dos hasta el límite 
for num in range(2, limite + 1): 
    # Si el residuo es 0 termina el ciclo
    if num % 2 == 0: 
        print(num)  