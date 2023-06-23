#define las variables y la operación que necesita
def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo
#Se ingresan los valores
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)
#se indica la posición de las valores y se  imprime
etiqueta = "Elevara {0} a la potencia {1} da como resultado {2}"

print(etiqueta.format(2,3,resultado))