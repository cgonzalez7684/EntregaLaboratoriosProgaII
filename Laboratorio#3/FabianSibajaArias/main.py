def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)
etiqueta = "Elevar {0} a potencia {1} su resultado es {2}"
print(etiqueta.format(2,3,resultado))