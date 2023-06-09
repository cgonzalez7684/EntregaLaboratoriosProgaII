"""Se crea una funcion donde se va a validar si es numero ingresado es par"""
def es_par(numero):
    """Se verifica si el numero es par"""
    if numero%2==0:
        """Si fuese par se imprime el numero"""
        print(numero)
    return True

"""Se le solicita al usuario el numero limite de hasta donde se van a evaluar los numeros pare"""
limite = int(input("Ingrese el limite para evaluar numeros pares"))

"""Se realiza un ciclo for para imprimir los numero pares"""
print("Numeros pares hasta el limite",limite, ":")
for numero in range(limite+1):
    es_par(numero)