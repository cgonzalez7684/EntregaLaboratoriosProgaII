def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo
#se le asigna los valores
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)
#se crea una etiqueta para saber que se va imprimir
etiqueta = "Elevar a {0} a la potencia {1} da como resultado {2}"
#asignamos la etiqueta con los valores
print(etiqueta.format(2,3,resultado))