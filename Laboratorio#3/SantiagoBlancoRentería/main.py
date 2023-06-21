def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo


resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)

etiqueta = "Elevar {0} a la potencia {1} da como resultado {2}"

#El error era en este print. Nada más cambié el número incorrecto(2) por el correcto(3).
print (etiqueta.format(2,3,resultado))