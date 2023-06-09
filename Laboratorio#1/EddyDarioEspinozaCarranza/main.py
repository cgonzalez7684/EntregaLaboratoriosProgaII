limite = int(input("Ingrese el límite: "))

print("Números pares hasta el límite", limite, ":")

for numero in range(2, limite + 1, 2):
    print(numero) 
    # se utiliza un bucle for para iterar sobre los números desde 2 hasta el límite especificado por el usuario, incrementando en pasos de 2 en cada iteración