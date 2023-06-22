def elevarNumeroAlaPotencia2(numero,potencia):
    calculo = numero ** potencia
    return calculo

resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 4)

etiqueta = " Elevar {2} a la potencia {4} da como resultado {16}"

print(etiqueta.format(2,4,resultado))