def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo
#se asiganan los valores a cada calculo 
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)
#se imprimen los valores 
etiqueta = "Elevar a {0} a la potencia {1} da como resultado {2}"

print(etiqueta.format(2,3,resultado))
