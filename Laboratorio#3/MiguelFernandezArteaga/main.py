# Laboratorio 3

def elevarNumeroAlaPotencia(numero, potencia):
    calculo = numero ** potencia
    return calculo

resultado = elevarNumeroAlaPotencia(numero=2, potencia=3)
etiqueta = "Elevar a {0} a la potencia {1} da como resultado {2}"
print(etiqueta.format(2,3,resultado))