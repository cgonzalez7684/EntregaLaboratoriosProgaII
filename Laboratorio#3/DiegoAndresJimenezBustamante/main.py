
#Aquí definimos lo que queremos hacer definiendo las variables y utilizando la formula 
def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo
#Se le asignan los valores a calcular 
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)
#Aquí se imprimen los valores a calcular y el resultado
etiqueta = "Elevar a {0} a la potencia {1} da como resultado {2}"

print(etiqueta.format(2,3,resultado))