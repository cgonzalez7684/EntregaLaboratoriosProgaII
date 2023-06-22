def elevarNumeroAlaPotencia2(numero,potencia):
    calculo = numero ** potencia
    return calculo

resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 1)

etiqueta = " Elevar {2} a la potencia {1} da como resultado {2}"

print(etiqueta.format(2,1,resultado))