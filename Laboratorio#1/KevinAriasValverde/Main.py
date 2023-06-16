"""Äqui se verifica si el numero es par"""

def num_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

"""Aqui se solicita ingresar un limite para evaluar"""

limite = int(input("Ingrese limite de evaluacion para numeros pares: "))

print("Números pares hasta llegar al límite", limite, ":")
for num in range(2, limite + 1):
    if num_par(num):
        print(num)
        