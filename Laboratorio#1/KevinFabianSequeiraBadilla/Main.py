  #KevinFabianSequeiraBadilla
 
  # Definir una función llamada "es_par" que verificará si un número es par o no
def es_par(numero):
    if numero % 2 == 0:  # Si el número es divisible por 2, es par
        return True
    else:
        return False

# Solicitar al usuario el límite hasta donde se desea evaluar los números pares
limite = int(input("Ingrese un número como límite para evaluar los números pares: "))

# Imprimir los números pares hasta el límite especificado
print("Números pares hasta el límite", limite, ":")

for i in range(1, limite + 1):
    if es_par(i):
        print(i)