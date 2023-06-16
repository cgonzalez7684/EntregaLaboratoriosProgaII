def elevarNumeroAlaPotencia2 (numero,potencia):
    calculo = numero**potencia
    return calculo


resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)

etiqueta = "Elevar {0} a la potencia {1} da como resultado {2}"

print(etiqueta.format(2,3,resultado)) #Cambio el valor del 2 que está en el medio por un 3.